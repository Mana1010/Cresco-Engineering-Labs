"""Build the Engineering Labs weekly update video from script.json.

Needs: ffmpeg, Python with `pillow` and `edge-tts`, and Segoe UI (from /mnt/c/Windows/Fonts).
Usage (from this folder):  python build.py            # build everything
                           python build.py 05-filter  # rebuild only that scene, then re-join
Same layout as the Week 1 video: navy cards, a 1920x960 content area, a blue line and a
caption band underneath.
"""

import asyncio
import json
import subprocess
import sys
from pathlib import Path

import edge_tts
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
WORK = HERE / "work"
W, H, CONTENT_H, FPS = 1920, 1080, 952, 30
FONT_DIR = Path("/mnt/c/Windows/Fonts")

BG = (12, 24, 57)
PANEL_TOP, PANEL_BOTTOM = (12, 35, 73), (11, 53, 101)
BLUE = (30, 144, 230)
LABEL_BLUE = (56, 150, 240)
WHITE = (255, 255, 255)
VALUE = (226, 233, 245)
GREY = (165, 180, 205)
DIVIDER = (38, 71, 113)
PANEL_X0, PANEL_X1 = 106, 1812
LEFT, VALUE_X, RIGHT = 364, 656, 1556


def font(bold=False, size=30):
	return ImageFont.truetype(str(FONT_DIR / ("segoeuib.ttf" if bold else "segoeui.ttf")), size)


def wrap(draw, text, fnt, width):
	lines, line = [], ""
	for word in text.split():
		test = f"{line} {word}".strip()
		if draw.textlength(test, font=fnt) <= width:
			line = test
		else:
			lines.append(line)
			line = word
	lines.append(line)
	return lines


def base_frame():
	"""Navy background, the gradient panel, the blue line and the caption band."""
	img = Image.new("RGB", (W, H), BG)
	panel = Image.new("RGB", (PANEL_X1 - PANEL_X0, CONTENT_H))
	pw, ph = panel.size
	px = panel.load()
	for y in range(ph):
		for x in range(pw):
			t = min(1.0, (x / pw) * 0.35 + (y / ph) * 0.65)
			px[x, y] = tuple(round(a + (b - a) * t) for a, b in zip(PANEL_TOP, PANEL_BOTTOM))
	img.paste(panel, (PANEL_X0, 0))
	ImageDraw.Draw(img).rectangle([0, 955, W, 963], fill=BLUE)
	return img


def card(scene, meta, out):
	img = base_frame()
	d = ImageDraw.Draw(img)
	rows = scene.get("rows", [])
	y = 292 if rows else 340
	d.rectangle([LEFT, y, LEFT + 88, y + 5], fill=BLUE)
	y += 40
	x = LEFT
	for ch in scene["label"]:  # letter-spaced label
		d.text((x, y), ch, font=font(True, 22), fill=LABEL_BLUE)
		x += d.textlength(ch, font=font(True, 22)) + 5
	y += 50
	for line in wrap(d, scene["title"], font(True, 68), RIGHT - LEFT + 80):
		d.text((LEFT, y), line, font=font(True, 68), fill=WHITE)
		y += 82
	d.text((LEFT, y + 2), scene["subtitle"], font=font(False, 30), fill=GREY)
	y += 74
	for label, value in rows:
		d.text((LEFT, y), label, font=font(True, 27), fill=LABEL_BLUE)
		for line in wrap(d, value, font(False, 27), RIGHT - VALUE_X):
			d.text((VALUE_X, y), line, font=font(False, 27), fill=VALUE)
			y += 37
		y += 21
	d.line([LEFT, 800, RIGHT, 800], fill=DIVIDER, width=2)
	d.text((LEFT, 828), meta["footer_left"], font=font(False, 21), fill=GREY)
	fr = font(False, 21)
	d.text((RIGHT - d.textlength(meta["footer_right"], font=fr), 828), meta["footer_right"], font=fr, fill=GREY)
	img.save(out)


def overlay(meta, out):
	"""Transparent layer for recording scenes: side bars, blue line, caption band, notice pill."""
	img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
	d = ImageDraw.Draw(img)
	d.rectangle([0, 960, W, 963], fill=BLUE + (255,))
	d.rectangle([0, 964, W, H], fill=BG + (255,))
	fnt = font(False, 25)
	tw = d.textlength(meta["notice"], font=fnt)
	# Top, in the empty part of the portal header: the bottom-right corner holds the pagination.
	x1, y0 = 1490, 26
	d.rounded_rectangle([x1 - tw - 32, y0, x1, y0 + 44], radius=6, fill=(22, 30, 48, 235))
	d.text((x1 - tw - 16, y0 + 7), meta["notice"], font=fnt, fill=WHITE + (255,))
	img.save(out)


def run(cmd):
	subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def duration(path):
	out = subprocess.run(
		["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
		capture_output=True, text=True, check=True,
	)
	return float(out.stdout.strip())


def caption_chunks(text):
	"""Split at sentence ends and commas; merge fragments shorter than 20 characters."""
	parts, cur = [], ""
	for ch in text:
		cur += ch
		if ch in ".,?!" and len(cur.strip()) > 0:
			parts.append(cur.strip())
			cur = ""
	if cur.strip():
		parts.append(cur.strip())
	merged = []
	for p in parts:
		if merged and (len(p) < 20 or len(merged[-1]) < 20) and len(merged[-1]) + len(p) < 70:
			merged[-1] += " " + p
		else:
			merged.append(p)
	return merged


def ass_time(t):
	h, rem = divmod(t, 3600)
	m, s = divmod(rem, 60)
	return f"{int(h)}:{int(m):02d}:{s:05.2f}"


def write_ass(text, start, speech, out):
	chunks = caption_chunks(text)
	total = sum(len(c) for c in chunks)
	lines, t = [], start
	for c in chunks:
		dur = speech * len(c) / total
		safe = c.replace("{", "(").replace("}", ")")
		lines.append(f"Dialogue: 0,{ass_time(t)},{ass_time(t + dur)},Cap,,0,0,0,,{safe}")
		t += dur
	out.write_text(
		"[Script Info]\nScriptType: v4.00+\nPlayResX: 1920\nPlayResY: 1080\n\n"
		"[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, BackColour, Bold, "
		"Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, "
		"Alignment, MarginL, MarginR, MarginV, Encoding\n"
		"Style: Cap,Segoe UI,40,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,2,120,120,34,1\n\n"
		"[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
		+ "\n".join(lines) + "\n"
	)


async def tts(text, voice, out):
	await edge_tts.Communicate(text, voice).save(str(out))


def speak(text, voice, out):
	"""Make the voice-over, reusing it if the text hasn't changed; the free service fails now and
	then, so retry a few times."""
	import time

	stamp = out.with_suffix(".txt")
	if out.exists() and stamp.exists() and stamp.read_text() == text:
		return
	for attempt in range(6):
		try:
			asyncio.run(tts(text, voice, out))
			stamp.write_text(text)
			return
		except edge_tts.exceptions.NoAudioReceived:
			time.sleep(3 + attempt * 3)
	raise RuntimeError(f"text-to-speech failed for {out.name}")


def build_scene(scene, meta, rec_len):
	sid = scene["id"]
	audio = WORK / f"{sid}.mp3"
	speak(scene["text"], meta["voice"], audio)
	speech = duration(audio)
	lead = 0.4
	ass = WORK / f"{sid}.ass"
	out = WORK / f"{sid}.mp4"
	audio_in = ["-i", str(audio)]
	audio_filter = f"[1:a]adelay={int(lead * 1000)}:all=1,apad[a]"
	if scene["kind"] == "card":
		length = lead + speech + 1.0
		png = WORK / f"{sid}.png"
		card(scene, meta, png)
		write_ass(scene["text"], lead, speech, ass)
		run([
			"ffmpeg", "-y", "-loop", "1", "-framerate", str(FPS), "-i", str(png), *audio_in,
			"-filter_complex", f"[0:v]ass={ass.name}:fontsdir=/mnt/c/Windows/Fonts,format=yuv420p[v];{audio_filter}",
			"-map", "[v]", "-map", "[a]", "-t", f"{length:.3f}",
			"-c:v", "libx264", "-preset", "medium", "-crf", "18", "-c:a", "aac", "-b:a", "160k", "-ar", "48000",
			str(out.name),
		])
	else:
		start = scene["start"]
		end = scene["end"] if scene["end"] is not None else rec_len
		seg = end - start
		length = max(seg, lead + speech + 0.6)
		pad = max(0.0, length - seg)
		write_ass(scene["text"], lead, speech, ass)
		rec = (HERE / meta["recording"]).resolve()
		# Crop the browser's address bar (64px at 1440p), fit the page into 1920x960 on navy.
		vf = (
			f"[0:v]trim={start}:{end},setpts=PTS-STARTPTS,fps={FPS},crop=iw:ih-64:0:64,"
			f"scale=-2:960:flags=lanczos,pad=1920:1080:(ow-iw)/2:0:color=0x0c1839,"
			f"tpad=stop_mode=clone:stop_duration={pad:.3f}[rec];"
			f"[rec][2:v]overlay=0:0,ass={ass.name}:fontsdir=/mnt/c/Windows/Fonts,format=yuv420p[v];{audio_filter}"
		)
		run([
			"ffmpeg", "-y", "-i", str(rec), *audio_in, "-i", "overlay.png",
			"-filter_complex", vf, "-map", "[v]", "-map", "[a]", "-t", f"{length:.3f}",
			"-c:v", "libx264", "-preset", "medium", "-crf", "18", "-c:a", "aac", "-b:a", "160k", "-ar", "48000",
			str(out.name),
		])
	print(f"{sid}: {duration(out):.1f}s (speech {speech:.1f}s)")


def main():
	meta = json.loads((HERE / "script.json").read_text())
	WORK.mkdir(exist_ok=True)
	only = set(sys.argv[1:])
	import os
	os.chdir(WORK)
	overlay(meta, WORK / "overlay.png")
	rec_len = duration((HERE / meta["recording"]).resolve())
	for scene in meta["scenes"]:
		if not only or scene["id"] in only:
			build_scene(scene, meta, rec_len)
	parts = WORK / "parts.txt"
	parts.write_text("".join(f"file '{s['id']}.mp4'\n" for s in meta["scenes"]))
	final = (HERE / meta["output"]).resolve()
	run([
		"ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "parts.txt",
		"-c:v", "libx264", "-preset", "medium", "-crf", "20", "-c:a", "aac", "-b:a", "160k",
		"-movflags", "+faststart", str(final),
	])
	print(f"done: {final} ({duration(final):.1f}s)")


if __name__ == "__main__":
	main()
