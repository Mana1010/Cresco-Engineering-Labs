# Content for the Frappe UI inventory report (see build_report.py).
# Each entry is one row in the summary table and one detail section.
# "available": Yes = frappe-ui has a dedicated component for it (possibly combined with other
# frappe-ui components and Tailwind layout classes); No = it has to be built (custom component,
# external library, or a per-instance CSS override).

DOCS = "https://ui.frappe.io/docs/"

COMPONENTS = [
    {
        "id": "1", "name": "Pills / badges", "file": "badge.png",
        "used_in": "Tools Registry cards, calculation details modal",
        "frappe": "Badge",
        "available": "Yes", "fit": "Out of the box", "effort": "Low",
        "gap": "Themes are fixed to gray, blue, green, amber, red and violet. The POC colours map closely: "
               "API → blue, Approved → green, version → gray, autonomous → violet. Icons go in the #prefix slot.",
        "recommendation": "Use Badge as-is.",
        "docs": [DOCS + "components/badge"],
        "code": """<script setup>
import { Badge } from 'frappe-ui'
import LucideArrowLeftRight from '~icons/lucide/arrow-left-right'
import LucideZap from '~icons/lucide/zap'
</script>

<template>
  <div class="flex flex-wrap gap-1.5">
    <Badge theme="blue" label="API">
      <template #prefix><LucideArrowLeftRight class="size-3" /></template>
    </Badge>
    <Badge theme="green" label="Approved" />
    <Badge theme="gray" label="v2.1" />
    <Badge theme="violet" label="autonomous-capable">
      <template #prefix><LucideZap class="size-3 text-amber-600" /></template>
    </Badge>
  </div>
</template>""",
    },
    {
        "id": "2", "name": "Metrics dashboard (composite)", "file": "bar_and_graph.png",
        "used_in": "Engineering Labs Home / Metrics",
        "frappe": "NumberCard, BarChart, Alert, List, Progress",
        "available": "Yes", "fit": "Compose", "effort": "Medium",
        "gap": "Mostly covered by the charts module. Exceptions: the coloured quota bars (Progress has no colour "
               "option, see 2f), the two-number \"124 pass / 18 returned\" headline (2b) and the status dots (2g). "
               "Broken down in 2a–2g below.",
        "recommendation": "Build the page from the charts module plus List and Alert. Add two small custom pieces "
                          "(quota bar, outcome headline).",
        "docs": [DOCS + "charts/numbercard", DOCS + "charts/barchart", DOCS + "charts/dashboard"],
        "code": """<script setup>
import { Alert } from 'frappe-ui'
import { NumberCard, BarChart } from 'frappe-ui/charts'

const toolPopularity = [
  { tool: 'Wind Pressure (Excel)', runs: 82 },
  { tool: 'CheckWind (API)', runs: 61 },
  { tool: 'Climate Zone', runs: 47 },
]
</script>

<template>
  <div class="grid grid-cols-4 gap-3">
    <NumberCard title="Calculations (30d)" :value="318"
                :delta="22" delta-suffix="%" delta-caption="vs prior 30 days" />
    <!-- …three more NumberCards (see component 3) -->
  </div>

  <div class="grid grid-cols-2 gap-4 mt-4">
    <BarChart title="Tool popularity (last 30 days)" :data="toolPopularity"
              x="tool" y="runs" horizontal />
    <div class="space-y-2">
      <Alert theme="amber" title="LAB-2026-0129 · Kooringal Warehouse"
             description="Wind pressure V_R entered manually — no CheckWind run on this project." />
    </div>
  </div>
</template>""",
        "subs": [
            {"id": "2a", "name": "KPI cards (calculations, users, runs, reports)", "frappe": "NumberCard",
             "available": "Yes", "fit": "Out of the box", "effort": "Low",
             "gap": "value, delta (▲ 22%), deltaCaption and the #caption slot cover every line of the card."},
            {"id": "2b", "name": "Review outcome headline (124 pass · 18 returned)", "frappe": "— (none)",
             "available": "No", "fit": "Custom", "effort": "Low",
             "gap": "Two coloured numbers side by side with a caption; NumberCard shows one value. A few lines of "
                    "markup with Tailwind text colours."},
            {"id": "2c", "name": "Horizontal bars (returns by reason, tool popularity)", "frappe": "BarChart (horizontal)",
             "available": "Yes", "fit": "Compose", "effort": "Low",
             "gap": "BarChart supports horizontal. One colour per category (red / orange / slate) needs each category "
                    "as its own series (splitBy) with seriesConfig colours, which should be checked visually."},
            {"id": "2d", "name": "Key–value lists (top corrected fields, timeliness)", "frappe": "List",
             "available": "Yes", "fit": "Compose", "effort": "Low",
             "gap": "A two-column List (label | value), or plain markup."},
            {"id": "2e", "name": "Consistency flag callouts (amber)", "frappe": "Alert (theme amber)",
             "available": "Yes", "fit": "Out of the box", "effort": "Low",
             "gap": "Alert's title and description map to the reference line and the message."},
            {"id": "2f", "name": "External API quota bars (orange / green)", "frappe": "Progress",
             "available": "No", "fit": "Custom", "effort": "Low",
             "gap": "Progress exists, but its bar colour is fixed to gray (no theme or colour prop). The design colours "
                    "each bar by usage, so it needs a small custom bar or a CSS override of Progress internals."},
            {"id": "2g", "name": "External API health rows (status dot, latency)", "frappe": "List",
             "available": "Yes", "fit": "Compose", "effort": "Low",
             "gap": "Rows via List; the green dot is a small span (no dedicated status-dot component)."},
        ],
    },
    {
        "id": "3", "name": "KPI stat boxes", "file": "boxes.png",
        "used_in": "Calculation Catalogue / Projects overview",
        "frappe": "NumberCard",
        "available": "Yes", "fit": "Out of the box", "effort": "Low",
        "gap": "The coloured value (green / orange / indigo) uses the color prop; captions use the #caption slot or "
               "deltaCaption. The card border and shadow follow frappe-ui's own card style.",
        "recommendation": "Use NumberCard from frappe-ui/charts.",
        "docs": [DOCS + "charts/numbercard"],
        "code": """<script setup>
import { NumberCard } from 'frappe-ui/charts'
</script>

<template>
  <div class="grid grid-cols-4 gap-3">
    <NumberCard title="First-time pass (30d)" value="87%" color="#059669">
      <template #caption>124 of 142 reviewed</template>
    </NumberCard>
    <NumberCard title="Consistency flags" value="3 open" color="#d97706">
      <template #caption>parameter lineage</template>
    </NumberCard>
    <NumberCard title="Calculations (30 days)" :value="318" color="#6366f1"
                :delta="22" delta-suffix="%" delta-caption="vs prior 30 days" />
    <NumberCard title="Autonomous runs" :value="44">
      <template #caption>no engineer touch</template>
    </NumberCard>
  </div>
</template>""",
    },
    {
        "id": "4", "name": "Breadcrumb", "file": "breadcrumb.png",
        "used_in": "Page header (project detail)",
        "frappe": "Breadcrumbs",
        "available": "Yes", "fit": "Out of the box", "effort": "Low",
        "gap": "None. items[] accepts label and route; the last item is the current page.",
        "recommendation": "Use Breadcrumbs (optionally inside PageHeader).",
        "docs": [DOCS + "components/breadcrumbs", DOCS + "components/pageheader"],
        "code": """<script setup>
import { Breadcrumbs } from 'frappe-ui'

const items = [
  { label: 'Projects', route: '/projects' },
  { label: 'Thornbury Townhouses — Lot 42' },
]
</script>

<template>
  <Breadcrumbs :items="items" />
</template>""",
    },
    {
        "id": "5", "name": "Action buttons", "file": "buttons.png",
        "used_in": "Project / calculation page actions",
        "frappe": "Button",
        "available": "Yes", "fit": "Theme", "effort": "Low",
        "gap": "Variants (solid, subtle, outline, ghost) and icons are built in. Button themes are only gray, blue, "
               "green and red, so the POC's purple/indigo primary colour needs a one-time brand override in the "
               "Tailwind theme (or use theme=\"blue\").",
        "recommendation": "Use Button. Agree the primary brand colour and set it once in the Tailwind config.",
        "docs": [DOCS + "components/button", DOCS + "foundations/colors"],
        "code": """<script setup>
import { Button } from 'frappe-ui'
</script>

<template>
  <div class="flex gap-2">
    <Button variant="outline" label="Open in Portal" icon-right="lucide-arrow-left-right" />
    <Button variant="solid" label="Add calculation" icon-left="lucide-plus" />
  </div>
</template>""",
    },
    {
        "id": "6", "name": "Tool cards (grid view)", "short": "tool cards", "file": "cards.png",
        "used_in": "Tools Registry — grid view",
        "frappe": "— (no Card); built from Badge + Button",
        "available": "No", "fit": "Custom", "effort": "Medium",
        "gap": "frappe-ui has no general-purpose Card component (ChartCard is for charts only). The card layout "
               "(badges, title, subtitle, divider, 2×2 label/value grid, round arrow button) is a small custom "
               "component using frappe-ui Badge and Button inside it.",
        "recommendation": "Create a reusable ToolCard.vue (≈40 lines) from frappe-ui primitives + Tailwind.",
        "docs": [DOCS + "components/badge", DOCS + "components/button"],
        "code": """<!-- ToolCard.vue -->
<script setup>
import { Badge, Button } from 'frappe-ui'

defineProps({ tool: { type: Object, required: true } })
defineEmits(['open'])
</script>

<template>
  <div class="rounded-lg border border-outline-gray-1 bg-surface-base p-4 shadow-sm">
    <div class="flex gap-1.5">
      <Badge theme="blue" :label="tool.type" />
      <Badge v-if="tool.autonomous" theme="amber" label="Autonomous" />
    </div>
    <h3 class="mt-3 text-lg font-semibold text-ink-gray-9">{{ tool.name }}</h3>
    <p class="text-sm text-ink-gray-5">{{ tool.source }}</p>
    <hr class="my-3 border-outline-gray-1" />
    <dl class="grid grid-cols-2 gap-3 text-sm">
      <div><dt class="text-xs uppercase text-ink-gray-5">Category</dt><dd>{{ tool.category }}</dd></div>
      <div><dt class="text-xs uppercase text-ink-gray-5">Version</dt><dd class="font-mono">{{ tool.version }}</dd></div>
      <div><dt class="text-xs uppercase text-ink-gray-5">Status</dt>
           <dd><Badge theme="green" :label="tool.status" /></dd></div>
      <div><dt class="text-xs uppercase text-ink-gray-5">Approved by</dt>
           <dd>{{ tool.approvedBy }}<br /><span class="text-xs text-ink-gray-5">{{ tool.approvedOn }}</span></dd></div>
    </dl>
    <div class="mt-2 flex justify-end">
      <Button variant="subtle" icon="lucide-arrow-right" @click="$emit('open', tool)" />
    </div>
  </div>
</template>""",
    },
    {
        "id": "7", "name": "Notes / comment list with input", "short": "notes list", "file": "comment-box.png",
        "used_in": "Calculation details modal (Notes)",
        "frappe": "— (no comment component); TextInput + Button",
        "available": "No", "fit": "Custom", "effort": "Low",
        "gap": "There's no comments/notes component in frappe-ui. The note bubbles (author · date, text) are simple "
               "custom markup; the input and the Add note button are frappe-ui TextInput and Button.",
        "recommendation": "Small custom NotesList.vue using TextInput + Button.",
        "docs": [DOCS + "components/textinput", DOCS + "components/button"],
        "code": """<script setup>
import { ref } from 'vue'
import { TextInput, Button } from 'frappe-ui'

const props = defineProps({ notes: { type: Array, default: () => [] } })
const emit = defineEmits(['add'])
const text = ref('')

function add() {
  if (text.value.trim()) emit('add', text.value.trim())
  text.value = ''
}
</script>

<template>
  <section>
    <h4 class="text-xs font-semibold uppercase text-ink-gray-5">Notes ({{ notes.length }})</h4>
    <div v-for="(note, i) in notes" :key="i" class="mt-2 rounded-lg bg-surface-gray-2 px-3 py-2">
      <div class="text-xs text-ink-gray-5">
        <strong class="text-ink-gray-8">{{ note.author }}</strong> · {{ note.date }}
      </div>
      <p class="text-sm text-ink-gray-8">{{ note.text }}</p>
    </div>
    <div class="mt-3 flex gap-2">
      <TextInput v-model="text" class="flex-1"
                 placeholder="Add a note (usage guidance, limits, caveats)…" @keydown.enter="add" />
      <Button label="Add note" :disabled="!text.trim()" @click="add" />
    </div>
  </section>
</template>""",
    },
    {
        "id": "8", "name": "Collapsible menu group (Engineering Labs)", "file": "dropdown.png",
        "used_in": "Sidebar navigation",
        "frappe": "SidebarSection (collapsible) + SidebarItem",
        "available": "Yes", "fit": "Theme", "effort": "Low",
        "gap": "SidebarSection collapsible and SidebarItem active cover the behaviour. The dark background and the "
               "solid blue active pill differ from frappe-ui's light, subtle active style. Dark mode can be scoped "
               "to the sidebar with data-theme=\"dark\"; the solid active colour needs a theme override.",
        "recommendation": "Use SidebarSection + SidebarItem; decide whether to keep the solid blue active style.",
        "docs": [DOCS + "components/sidebar"],
        "code": """<script setup>
import { SidebarSection, SidebarItem } from 'frappe-ui'
import { useRoute } from 'vue-router'
const route = useRoute()
</script>

<template>
  <SidebarSection label="Engineering Labs" collapsible>
    <SidebarItem label="Home" route="/engineering-labs/home"
                 :active="route.path === '/engineering-labs/home'" />
    <SidebarItem label="Calculation Catalogue" route="/engineering-labs/calculation-catalogue"
                 :active="route.path.startsWith('/engineering-labs/calculation-catalogue')" />
    <SidebarItem label="Tools Registry" route="/engineering-labs/tools-registry"
                 :active="route.path.startsWith('/engineering-labs/tools-registry')" />
  </SidebarSection>
</template>""",
    },
    {
        "id": "9", "name": "Grid / table view toggle (icon buttons)", "file": "dual-button.png",
        "used_in": "Tools Registry header",
        "frappe": "TabButtons (icon-only options)",
        "available": "Yes", "fit": "Out of the box", "effort": "Low",
        "gap": "TabButtons supports icon-only options (icon + label used as accessible text). Active colour follows "
               "frappe-ui's style rather than the solid blue in the screenshot.",
        "recommendation": "Use TabButtons with v-model.",
        "docs": [DOCS + "components/tabbuttons"],
        "code": """<script setup>
import { ref } from 'vue'
import { TabButtons } from 'frappe-ui'

const view = ref('grid')
const options = [
  { value: 'grid', label: 'Grid view', icon: 'lucide-layout-grid' },
  { value: 'table', label: 'Table view', icon: 'lucide-table' },
]
</script>

<template>
  <TabButtons v-model="view" :options="options" />
</template>""",
    },
    {
        "id": "10", "name": "Request form (inputs, select, run button)", "file": "form.png",
        "used_in": "Tool runner / calculation preview",
        "frappe": "TextInput, Select (or FormControl), Button",
        "available": "Yes", "fit": "Out of the box", "effort": "Low",
        "gap": "Labels, text/number inputs, select and a full-width primary button are all built in. frappe-ui's "
               "Select renders its own popover list rather than the browser's native dropdown.",
        "recommendation": "Use TextInput/Select with their label props (or FormControl).",
        "docs": [DOCS + "components/textinput", DOCS + "components/select", DOCS + "components/formcontrol"],
        "code": """<script setup>
import { reactive } from 'vue'
import { TextInput, Select, Button } from 'frappe-ui'

const form = reactive({ address: '', height: '', edition: null })
const editions = [
  { label: 'AS/NZS 1170.2:2021', value: '2021' },
  { label: 'AS/NZS 1170.2:2011', value: '2011' },
]

function run() {
  // call the permission-checked whitelisted method that runs the tool
}
</script>

<template>
  <form class="space-y-4 rounded-lg border border-outline-gray-1 p-4" @submit.prevent="run">
    <p class="text-xs font-semibold uppercase text-ink-gray-5">Request</p>
    <TextInput v-model="form.address" label="Site address" />
    <TextInput v-model="form.height" type="number" label="Structure height (m)" />
    <Select v-model="form.edition" :options="editions" label="Standard edition" />
    <Button type="submit" variant="solid" class="w-full" icon-left="lucide-play"
            label="Run via Revolutio Hazard API" />
    <p class="text-xs text-ink-gray-5">Routed through the Labs adapter layer…</p>
  </form>
</template>""",
    },
    {
        "id": "11", "name": "App identity block (logo + title + subtitle)", "file": "icon-badge.png",
        "used_in": "Sidebar header",
        "frappe": "SidebarHeader",
        "available": "Yes", "fit": "Out of the box", "effort": "Low",
        "gap": "SidebarHeader has title, subtitle and logo props, and an optional workspace menu.",
        "recommendation": "Use SidebarHeader.",
        "docs": [DOCS + "components/sidebar"],
        "code": """<script setup>
import { SidebarHeader } from 'frappe-ui'
import logo from '@/assets/cresco-logo.svg'
</script>

<template>
  <SidebarHeader title="Engineering Labs" subtitle="Cresco Australia" :logo="logo" />
</template>""",
    },
    {
        "id": "12", "name": "Audit log list", "file": "logs.png",
        "used_in": "Calculation audit log",
        "frappe": "List (frappe-ui/list) + Badge",
        "available": "Yes", "fit": "Compose", "effort": "Low",
        "gap": "Rows with a mono timestamp, title text, bolt pill and a green \"Complete\" badge map to a "
               "three-column List. The card wrapper and the description line are plain markup.",
        "recommendation": "Use List with columns ['9rem', 'minmax(0,1fr)', 'auto'].",
        "docs": [DOCS + "molecules/list", DOCS + "components/badge"],
        "code": """<script setup>
import { Badge } from 'frappe-ui'
import { List, ListRows, ListRow, ListCell } from 'frappe-ui/list'

defineProps({ logs: { type: Array, required: true } })
</script>

<template>
  <List :columns="['9rem', 'minmax(0,1fr)', 'auto']">
    <ListRows :items="logs" row-key="name" v-slot="{ item, value }">
      <ListRow :value="value">
        <ListCell class="font-mono text-ink-gray-5">{{ item.ran_at }}</ListCell>
        <ListCell><strong>{{ item.tool }}</strong> — {{ item.description }}</ListCell>
        <ListCell><Badge theme="green" variant="outline" label="Complete" /></ListCell>
      </ListRow>
    </ListRows>
  </List>
</template>""",
    },
    {
        "id": "13", "name": "Details modal", "file": "modal.png",
        "used_in": "Tool / calculation details",
        "frappe": "Dialog (+ Badge, Button, TextInput)",
        "available": "Yes", "fit": "Compose", "effort": "Medium",
        "gap": "Dialog provides the title, close button, sizes and an #actions slot. The body (badges, 2-column "
               "details, notes) is composed. Button has no amber/orange theme, so the orange \"Deprecate\" button "
               "needs a class override or theme=\"red\".",
        "recommendation": "Use Dialog; reuse NotesList (component 7) inside it.",
        "docs": [DOCS + "components/dialog"],
        "code": """<script setup>
import { Dialog, Badge, Button } from 'frappe-ui'

const open = defineModel('open', { type: Boolean })
defineProps({ tool: { type: Object, required: true } })
</script>

<template>
  <Dialog v-model:open="open" :title="tool.name" size="xl">
    <div class="space-y-4">
      <div class="flex gap-1.5">
        <Badge theme="blue" :label="tool.type" />
        <Badge theme="green" :label="tool.status" />
        <Badge :label="tool.version" />
      </div>
      <p class="text-sm">{{ tool.description }}</p>
      <Button variant="solid" icon-left="lucide-eye" label="View calculation" />
      <!-- 2-column details grid + <NotesList /> -->
    </div>
    <template #actions>
      <Button variant="solid" theme="red" label="Deprecate" />
      <span class="ml-3 text-sm text-ink-gray-5">Acting as Growth &amp; Innovation Manager</span>
    </template>
  </Dialog>
</template>""",
    },
    {
        "id": "14", "name": "Info banner", "file": "notification-box.png",
        "used_in": "Calculation preview",
        "frappe": "Alert (theme blue)",
        "available": "Yes", "fit": "Out of the box", "effort": "Low",
        "gap": "None. Alert theme=\"blue\" with a title or description.",
        "recommendation": "Use Alert.",
        "docs": [DOCS + "components/alert"],
        "code": """<script setup>
import { Alert } from 'frappe-ui'
</script>

<template>
  <Alert theme="blue"
         title="Catalogue preview — not attached to a project. Runs here are for inspection only and are not recorded against a job." />
</template>""",
    },
    {
        "id": "15", "name": "Result panel (key–value tables + disclaimer)", "file": "one-column-table.png",
        "used_in": "Tool runner result",
        "frappe": "List (2 columns) + Badge + Alert (amber)",
        "available": "Yes", "fit": "Compose", "effort": "Medium",
        "gap": "Section headings, label/value rows (values in monospace) and the status pill map to List and Badge. "
               "The amber disclaimer maps to Alert theme=\"amber\" with the pill in its #prefix slot. The layout "
               "matches only approximately.",
        "recommendation": "Compose; make a small ResultSection.vue for the repeated label/value groups.",
        "docs": [DOCS + "molecules/list", DOCS + "components/alert", DOCS + "components/badge"],
        "code": """<script setup>
import { Alert, Badge } from 'frappe-ui'
import { List, ListRows, ListRow, ListCell } from 'frappe-ui/list'

defineProps({ result: { type: Object, required: true } })
</script>

<template>
  <div class="space-y-4">
    <div class="flex items-center justify-between">
      <p class="text-xs font-semibold uppercase text-ink-gray-5">Result · Revolutio Hazard API</p>
      <Badge theme="green" variant="outline" :label="`status: ${result.status}`" />
    </div>
    <section v-for="section in result.sections" :key="section.title">
      <h4 class="mb-1 text-sm font-semibold text-ink-blue-6">{{ section.title }}</h4>
      <List :columns="['minmax(0,1fr)', 'auto']">
        <ListRows :items="section.rows" :row-key="(row) => row[0]" v-slot="{ item, value }">
          <ListRow :value="value">
            <ListCell>{{ item[0] }}</ListCell>
            <ListCell class="font-mono font-semibold">{{ item[1] }}</ListCell>
          </ListRow>
        </ListRows>
      </List>
    </section>
    <Alert theme="amber"
           description="This report was generated by an automated calculation tool. Results must be reviewed and verified by a qualified engineer before use in design.">
      <template #prefix><Badge theme="amber" variant="outline" label="Preliminary — Subject to Engineer Review" /></template>
    </Alert>
  </div>
</template>""",
    },
    {
        "id": "16", "name": "User profile (role pill, avatar, name, title)", "file": "profile.png",
        "used_in": "Top header",
        "frappe": "Avatar + Badge + Dropdown",
        "available": "Yes", "fit": "Compose", "effort": "Low",
        "gap": "Avatar shows initials from label. The role pill is a Badge. The name block plus caret becomes the "
               "Dropdown's #trigger (see component 18).",
        "recommendation": "Compose with Avatar, Badge and Dropdown.",
        "docs": [DOCS + "components/avatar", DOCS + "components/badge", DOCS + "components/dropdown"],
        "code": """<script setup>
import { Avatar, Badge } from 'frappe-ui'
defineProps({ user: { type: Object, required: true } })
</script>

<template>
  <div class="flex items-center gap-3">
    <Badge theme="violet" :label="user.role" />
    <Avatar :label="user.full_name" :image="user.image" size="lg" />
    <div class="text-right leading-tight">
      <div class="text-sm font-semibold text-ink-gray-9">{{ user.full_name }}</div>
      <div class="text-xs text-ink-gray-5">{{ user.job_title }}</div>
    </div>
  </div>
</template>""",
    },
    {
        "id": "17", "name": "Search bar", "file": "search-bar.png",
        "used_in": "Projects / Tools Registry lists",
        "frappe": "TextInput (type search)",
        "available": "Yes", "fit": "Out of the box", "effort": "Low",
        "gap": "None. The debounce prop is built in (useful for server-side search); an optional icon goes in the "
               "#prefix slot.",
        "recommendation": "Use TextInput with debounce.",
        "docs": [DOCS + "components/textinput"],
        "code": """<script setup>
import { ref } from 'vue'
import { TextInput } from 'frappe-ui'
import LucideSearch from '~icons/lucide/search'

const search = ref('')
</script>

<template>
  <TextInput v-model="search" type="search" :debounce="300" placeholder="Search name, client, ref…">
    <template #prefix><LucideSearch class="size-4 text-ink-gray-5" /></template>
  </TextInput>
</template>""",
    },
    {
        "id": "18", "name": "User switcher menu (avatars, groups, sign out)", "file": "select-modal.png",
        "used_in": "Header profile menu",
        "frappe": "Dropdown (grouped options, #item-prefix slot)",
        "available": "Yes", "fit": "Compose", "effort": "Low",
        "gap": "Grouped options ({ group, options }), a red-themed item for Sign out, and the #item-prefix slot for "
               "avatars. Two-line items (name + role) use the description field or the #item-label slot.",
        "recommendation": "Use Dropdown with the profile block (16) as its #trigger.",
        "docs": [DOCS + "components/dropdown"],
        "code": """<script setup>
import { Dropdown, Avatar } from 'frappe-ui'

const users = [
  { label: 'Isaac Mannion', description: 'Management' },
  { label: 'Sarah Chen', description: 'Structural' },
]
const switchTo = (user) => { /* demo only */ }
const logout = () => (window.location.href = '/?cmd=web_logout')
const options = [
  { group: 'Switch user (demo)', options: users.map((u) => ({ ...u, onClick: () => switchTo(u) })) },
  { label: 'Sign out', theme: 'red', onClick: logout },
]
</script>

<template>
  <Dropdown :options="options" align="end">
    <template #trigger><!-- profile block from component 16 --></template>
    <template #item-prefix="{ item }">
      <Avatar v-if="item.description" :label="item.label" size="sm" />
    </template>
  </Dropdown>
</template>""",
    },
    {
        "id": "19", "name": "Filter select (All disciplines)", "file": "select.png",
        "used_in": "Projects list filter",
        "frappe": "Select",
        "available": "Yes", "fit": "Out of the box", "effort": "Low",
        "gap": "Works as a filter. The visual differs: the screenshot is the browser's native select, while frappe-ui "
               "renders its own styled popover.",
        "recommendation": "Use Select (accept frappe-ui's look, or confirm with the client).",
        "docs": [DOCS + "components/select"],
        "code": """<script setup>
import { ref } from 'vue'
import { Select } from 'frappe-ui'

const discipline = ref('')
const options = [
  { label: 'All disciplines', value: '' },
  { label: 'Structural — Residential', value: 'STR-RESI' },
  { label: 'Structural — Commercial', value: 'STR-COMM' },
  { label: 'Civil Engineering', value: 'CIVIL' },
]
</script>

<template>
  <Select v-model="discipline" :options="options" placeholder="All disciplines" />
</template>""",
    },
    {
        "id": "20", "name": "Application sidebar (dark)", "file": "sidebar.png",
        "used_in": "Main navigation",
        "frappe": "Sidebar, SidebarHeader, SidebarItem, SidebarCollapseToggle",
        "available": "Yes", "fit": "Theme", "effort": "Medium",
        "gap": "Header, items with icons, active state and collapsing (icons-only) are built in. This also covers "
               "the collapsible-sidebar requirement. The sidebar can be dark while the page stays light by setting "
               "data-theme=\"dark\" on it. The exact navy background and purple active pill need theme overrides. "
               "The footer status line goes in the bottom of the default slot.",
        "recommendation": "Use Sidebar. Decide with the client whether frappe-ui's dark palette is acceptable or the "
                          "exact navy/purple is required.",
        "docs": [DOCS + "components/sidebar", DOCS + "components/sidebarrail"],
        "code": """<script setup>
import { ref } from 'vue'
import { Sidebar, SidebarHeader, SidebarItem, SidebarCollapseToggle } from 'frappe-ui'
import logo from '@/assets/cresco-logo.svg'

const collapsed = ref(false)
</script>

<template>
  <Sidebar v-model:collapsed="collapsed" data-theme="dark">
    <SidebarHeader title="Engineering Labs" subtitle="Cresco Australia" :logo="logo" />
    <div class="flex-1 overflow-y-auto">
      <SidebarItem label="Projects" icon="lucide-folder" route="/projects" />
      <SidebarItem label="Calculation Catalogue" icon="lucide-calculator" route="/catalogue" />
      <SidebarItem label="Automations" icon="lucide-zap" route="/automations" />
      <SidebarItem label="Portal Integration" icon="lucide-arrow-left-right" route="/integration" />
      <SidebarItem label="Metrics" icon="lucide-line-chart" route="/metrics" />
    </div>
    <div class="px-3 py-2 text-xs text-ink-gray-5">● Labs API · live</div>
    <SidebarCollapseToggle />
  </Sidebar>
</template>""",
    },
    {
        "id": "21", "name": "Loading placeholder", "file": "skeleton.png",
        "used_in": "Tool runner (while the API responds)",
        "frappe": "LoadingText / Skeleton / Spinner",
        "available": "Yes", "fit": "Out of the box", "effort": "Low",
        "gap": "LoadingText shows a message with a spinner; Skeleton gives a pulsing placeholder block.",
        "recommendation": "Use LoadingText inside the result panel.",
        "docs": [DOCS + "components/loadingtext", DOCS + "components/skeleton"],
        "code": """<script setup>
import { LoadingText } from 'frappe-ui'
</script>

<template>
  <div class="flex h-28 items-center justify-center rounded-lg border border-outline-gray-1">
    <LoadingText text="Contacting Revolutio Hazard API…" />
  </div>
</template>""",
    },
    {
        "id": "22", "name": "API status indicator (dot + text)", "file": "small-badge.png",
        "used_in": "Sidebar footer",
        "frappe": "Badge (variant ghost, dot in #prefix)",
        "available": "Yes", "fit": "Compose", "effort": "Low",
        "gap": "There's no dedicated status-dot component. A ghost Badge with a coloured dot in its #prefix slot "
               "gives the same result; the version line is plain text.",
        "recommendation": "Badge ghost + dot, or a 3-line custom span.",
        "docs": [DOCS + "components/badge"],
        "code": """<script setup>
import { Badge } from 'frappe-ui'
</script>

<template>
  <div class="text-xs text-ink-gray-5">
    <Badge variant="ghost" theme="green" label="Labs API · live">
      <template #prefix><span class="size-2 rounded-full bg-surface-green-3" /></template>
    </Badge>
    <div>POC v0.7 · Management view</div>
  </div>
</template>""",
    },
    {
        "id": "23", "name": "Data table (projects)", "file": "table.png",
        "used_in": "Projects list, Tools Registry table view",
        "frappe": "List (frappe-ui/list) + Badge",
        "available": "Yes", "fit": "Compose", "effort": "Medium",
        "gap": "List provides grid columns, a header with sortable cells, row selection and virtual scrolling. Two-line "
               "cells and status pills are composed with Badge. List has no built-in pagination bar; the "
               "first/prev/next/last + rows-per-page control required in the 2026-10-20 meeting must be built from "
               "Button + Select.",
        "recommendation": "Use List; add a small Pagination.vue (Buttons + Select) under it.",
        "docs": [DOCS + "molecules/list", DOCS + "experimental/listview"],
        "code": """<script setup>
import { Badge } from 'frappe-ui'
import { List, ListHeader, ListHeaderCell, ListRows, ListRow, ListCell } from 'frappe-ui/list'

defineProps({ projects: { type: Array, required: true } })
const stageTheme = { 'WIP': 'blue', 'L1 Check': 'amber', 'Deliverable Approved': 'green' }
</script>

<template>
  <List :columns="['minmax(0,2fr)', '7rem', 'minmax(0,1fr)', '9rem', '8rem', '8rem']">
    <ListHeader>
      <ListHeaderCell>Project</ListHeaderCell>
      <ListHeaderCell>Discipline</ListHeaderCell>
      <ListHeaderCell>Owner / Team</ListHeaderCell>
      <ListHeaderCell>Status</ListHeaderCell>
      <ListHeaderCell>Calculations</ListHeaderCell>
      <ListHeaderCell>Portal / Synergy</ListHeaderCell>
    </ListHeader>
    <ListRows :items="projects" row-key="name" v-slot="{ item, value }">
      <ListRow :value="value" :route="`/projects/${item.name}`">
        <ListCell><strong>{{ item.project_name }}</strong><br /><small>{{ item.client }}</small></ListCell>
        <ListCell><Badge variant="outline" :label="item.discipline" /></ListCell>
        <ListCell>{{ item.owner }}<br /><small>{{ item.team }}</small></ListCell>
        <ListCell><Badge :theme="stageTheme[item.stage] || 'gray'" :label="item.stage" /></ListCell>
        <ListCell>{{ item.calcs_done }}/{{ item.calcs_total }} done</ListCell>
        <ListCell class="font-mono text-sm">{{ item.portal_ref }}<br />{{ item.name }}</ListCell>
      </ListRow>
    </ListRows>
  </List>
</template>""",
    },
    {
        "id": "24", "name": "On/off toggle", "file": "toggle.png",
        "used_in": "Automations / settings",
        "frappe": "Switch",
        "available": "Yes", "fit": "Out of the box", "effort": "Low",
        "gap": "Switch with v-model. The \"ON\" caption below the switch is a custom label position (Switch puts its "
               "label beside it).",
        "recommendation": "Use Switch.",
        "docs": [DOCS + "components/switch"],
        "code": """<script setup>
import { ref } from 'vue'
import { Switch } from 'frappe-ui'

const enabled = ref(true)
</script>

<template>
  <div class="flex flex-col items-center gap-1">
    <Switch v-model="enabled" />
    <span class="text-xs font-semibold" :class="enabled ? 'text-ink-green-3' : 'text-ink-gray-5'">
      {{ enabled ? 'ON' : 'OFF' }}
    </span>
  </div>
</template>""",
    },
    # ------------------------------------------------------------------ added 2026-10-27 (batch 2)
    {
        "id": "25", "name": "Collapsed sidebar (icons only)", "file": "collapsed-sidebar.png",
        "used_in": "Main navigation (collapsed state)",
        "frappe": "Sidebar (collapsed) + SidebarCollapseToggle",
        "available": "Yes", "fit": "Theme", "effort": "Low",
        "gap": "Sidebar collapses to icons natively (collapsedWidth, default 3rem) and is controlled with "
               "v-model:collapsed; SidebarCollapseToggle adds the toggle. The dark colours follow component 20. "
               "Still to check once frappe-ui is installed: how a collapsed SidebarSection exposes its sub-items "
               "(the portal currently shows them in a pop-out).",
        "recommendation": "Use Sidebar's built-in collapse; verify sub-item behaviour when collapsed.",
        "docs": [DOCS + "components/sidebar", DOCS + "components/sidebarrail"],
        "code": """<script setup>
import { ref } from 'vue'
import { Sidebar, SidebarHeader, SidebarItem, SidebarCollapseToggle } from 'frappe-ui'

const collapsed = ref(true)   // icons only
</script>

<template>
  <Sidebar v-model:collapsed="collapsed" collapsed-width="4rem" data-theme="dark">
    <SidebarHeader title="Cresco Australia" />
    <SidebarItem label="Dashboard" icon="lucide-layout-grid" route="/portal" />
    <SidebarItem label="Engineering Labs" icon="lucide-flask-conical" route="/engineering-labs/home" />
    <!-- labels are hidden automatically while collapsed -->
    <SidebarCollapseToggle />
  </Sidebar>
</template>""",
    },
    {
        "id": "26", "name": "Report & data panel — PDF preview", "short": "PDF preview", "file": "pdf-preview.png",
        "used_in": "Project calculation page (Report & Data)",
        "frappe": "TabButtons + Select + Button; PDF viewer: none",
        "available": "No", "fit": "Custom", "effort": "Medium",
        "gap": "The panel's controls (PDF/JSON switch, calculation selector, download button) are frappe-ui "
               "TabButtons, Select and Button. frappe-ui has no PDF viewer. The usual approach: generate the PDF on "
               "the server with a Frappe Print Format (permission-checked) and show it in the browser's built-in "
               "viewer through an <iframe>; pdf.js is an option if a custom-styled viewer is required.",
        "recommendation": "Frappe Print Format for the branded PDF + <iframe> preview; controls from frappe-ui.",
        "docs": [DOCS + "components/tabbuttons", DOCS + "components/select", DOCS + "components/button"],
        "code": """<script setup>
import { ref, computed } from 'vue'
import { TabButtons, Select, Button } from 'frappe-ui'

const view = ref('pdf')
const calc = ref('ENG-104206')
const runs = [{ label: 'Climate Zone Lookup · Rev C', value: 'ENG-104206' }]

// Frappe renders the Print Format to PDF on the server (permission-checked).
// "Labs Calculation Run" and "Cresco Calculation Report" are example names — neither exists yet.
const pdfUrl = computed(() =>
  `/api/method/frappe.utils.print_format.download_pdf?doctype=Labs Calculation Run` +
  `&name=${calc.value}&format=Cresco Calculation Report&no_letterhead=0`)
</script>

<template>
  <section class="rounded-lg border border-outline-gray-1 p-4">
    <div class="mb-3 flex items-center justify-between">
      <p class="text-xs font-semibold uppercase text-ink-gray-5">Report &amp; Data</p>
      <div class="flex gap-2">
        <TabButtons v-model="view" :options="[{ value: 'pdf', label: 'PDF report' }, { value: 'json', label: 'JSON data' }]" />
        <Select v-model="calc" :options="runs" />
        <Button variant="solid" icon-left="lucide-download" label="PDF" :href="pdfUrl" />
      </div>
    </div>
    <iframe v-if="view === 'pdf'" :src="pdfUrl" class="h-[480px] w-full rounded" />
  </section>
</template>""",
    },
    {
        "id": "27", "name": "Toast notification", "file": "toast.png",
        "used_in": "Feedback after actions (e.g. revision created)",
        "frappe": "toast() + ToastProvider",
        "available": "Yes", "fit": "Out of the box", "effort": "Low",
        "gap": "frappe-ui ships toast (built on vue-sonner) with success / error / warning / info variants. Add "
               "<ToastProvider /> once at the app root. The dark style with a green accent may differ slightly from "
               "frappe-ui's default toast look. The red \"Returned\" pill in the screenshot is a Badge (theme red).",
        "recommendation": "Use toast.success(...) after actions; ToastProvider in App.vue.",
        "docs": [DOCS + "components/toast"],
        "code": """<!-- App.vue (once) -->
<script setup>
import { ToastProvider } from 'frappe-ui'
</script>
<template>
  <RouterView />
  <ToastProvider />
</template>

<!-- Anywhere after an action -->
<script setup>
import { toast } from 'frappe-ui'

function onRevisionCreated() {
  toast.success('Revision created — inputs carried forward; the superseded revision is retained in the audit log')
}
</script>""",
    },
    {
        "id": "28", "name": "Report & data panel — JSON preview", "file": "json-preview.png",
        "used_in": "Project calculation page (Report & Data)",
        "frappe": "CodeEditor (read-only, JSON) + TabButtons + Badge + Button",
        "available": "Yes", "fit": "Compose", "effort": "Medium",
        "gap": "frappe-ui's code-editor molecule (CodeMirror) shows JSON read-only with syntax highlighting "
               "(editable=false). The header strip (GET badge, endpoint, X-API-Key pill) is Badge + text; Copy and "
               "Download are Buttons. The dark code background can come from data-theme=\"dark\" on the panel.",
        "recommendation": "Use CodeEditor read-only with loadLanguage('json').",
        "docs": [DOCS + "molecules/code-editor", DOCS + "components/tabbuttons"],
        "code": """<script setup>
import { ref, shallowRef, onMounted } from 'vue'
import { Badge, Button } from 'frappe-ui'
import { CodeEditor, CodeEditorContent, CodeKit, loadLanguage } from 'frappe-ui/code-editor'

const props = defineProps({ payload: { type: Object, required: true } })
const json = ref(JSON.stringify(props.payload, null, 2))
const extensions = shallowRef([CodeKit.configure({ lineNumbers: false })])

onMounted(async () => {
  extensions.value = [CodeKit.configure({ lineNumbers: false }), await loadLanguage('json')]
})
const copy = () => navigator.clipboard.writeText(json.value)
</script>

<template>
  <div data-theme="dark" class="rounded-lg bg-surface-gray-1">
    <div class="flex items-center gap-2 px-3 py-2 text-xs">
      <Badge theme="green" label="GET" />
      <code class="text-ink-blue-6">/api/v1/calculations/ENG-104206</code>
      <Badge theme="violet" label="X-API-Key" />
      <Button class="ml-auto" label="Copy" @click="copy" />
    </div>
    <CodeEditor v-model="json" :extensions="extensions" :editable="false">
      <CodeEditorContent />
    </CodeEditor>
  </div>
</template>""",
    },
    {
        "id": "29", "name": "Back link + page title with badges", "file": "back-option.png",
        "used_in": "Calculation page header",
        "frappe": "Button (ghost, route) + Badge  (or PageHeader / Breadcrumbs)",
        "available": "Yes", "fit": "Compose", "effort": "Low",
        "gap": "The back link is a ghost Button with a left-arrow icon and a route; the badges are Badge. "
               "PageHeader (with its back button) or Breadcrumbs (component 4) are frappe-ui alternatives for the "
               "same \"go up one level\" pattern.",
        "recommendation": "Ghost Button with route + title + Badges.",
        "docs": [DOCS + "components/button", DOCS + "components/pageheader", DOCS + "components/badge"],
        "code": """<script setup>
import { Button, Badge } from 'frappe-ui'
</script>

<template>
  <div>
    <Button variant="ghost" icon-left="lucide-arrow-left" label="Thornbury Townhouses — Lot 42"
            route="/projects/SYN-8835" />
    <div class="mt-1 flex items-center gap-2">
      <h1 class="text-xl font-semibold text-ink-gray-9">Climate Zone Lookup</h1>
      <Badge theme="blue" label="Python" />
      <Badge theme="green" label="Approved v1.4" />
      <Badge theme="violet" label="Rev C" />
    </div>
  </div>
</template>""",
    },
    {
        "id": "30", "name": "Read-only source code viewer", "file": "code-preview.png",
        "used_in": "Calculation preview (Python tools)",
        "frappe": "CodeEditor (read-only, Python) + Badge",
        "available": "Yes", "fit": "Compose", "effort": "Low",
        "gap": "Same code-editor molecule as component 28 with loadLanguage('python'). The header (file name + "
               "\"Read-only · server-side logic\" badge) is plain markup + Badge. Note: the code shown must come "
               "from the server and only to users allowed to see it — the viewer itself doesn't restrict anything.",
        "recommendation": "Use CodeEditor read-only with loadLanguage('python').",
        "docs": [DOCS + "molecules/code-editor"],
        "code": """<script setup>
import { shallowRef, onMounted } from 'vue'
import { Badge } from 'frappe-ui'
import { CodeEditor, CodeEditorContent, CodeKit, loadLanguage } from 'frappe-ui/code-editor'

defineProps({ fileName: String, source: String })
const extensions = shallowRef([CodeKit])
onMounted(async () => { extensions.value = [CodeKit, await loadLanguage('python')] })
</script>

<template>
  <div data-theme="dark" class="overflow-hidden rounded-lg bg-surface-gray-1">
    <div class="flex items-center justify-between px-3 py-2 text-xs">
      <span class="font-mono font-semibold">{{ fileName }}</span>
      <Badge theme="green" label="Read-only · server-side logic" />
    </div>
    <CodeEditor :model-value="source" :extensions="extensions" :editable="false">
      <CodeEditorContent />
    </CodeEditor>
  </div>
</template>""",
    },
    {
        "id": "31", "name": "Protected Excel workbook preview (spreadsheet)", "short": "Excel spreadsheet preview", "file": "excel-preview.png",
        "used_in": "Calculation preview (Excel tools)",
        "frappe": "— (no spreadsheet); Alert, Button, Tabs, Badge around it",
        "available": "No", "fit": "Custom", "effort": "High",
        "gap": "frappe-ui has no spreadsheet grid (cell references, formula bar, row/column headers, sheet tabs, "
               "live recalculation). The surrounding parts are covered: protected-workbook banner (Alert amber), "
               "toolbar (Button), sheet tabs (Tabs), disclaimer (Alert). Two routes: (a) an external spreadsheet "
               "library — e.g. Jspreadsheet CE (MIT), Univer (Apache-2.0), Handsontable (paid licence for commercial "
               "use) — plus server-side formula evaluation; or (b) since only the input cells are editable, show "
               "the workbook as an inputs form + results table (TextInput + List), which frappe-ui covers fully.",
        "recommendation": "Decide with the client whether a true spreadsheet look is required. If not, use route (b); "
                          "if yes, evaluate the libraries' licences and bundle size first.",
        "docs": [DOCS + "components/alert", DOCS + "components/tabs", DOCS + "molecules/list"],
        "code": """<!-- Route (b): inputs form + results table, all frappe-ui -->
<script setup>
import { reactive } from 'vue'
import { Alert, Button, TextInput, Badge } from 'frappe-ui'
import { List, ListRows, ListRow, ListCell } from 'frappe-ui/list'

const inputs = reactive({ s_u: 60, d_h: 350, n_c: 9 })        // editable input cells
defineProps({ results: { type: Array, default: () => [] } })    // computed on the server
</script>

<template>
  <Alert theme="amber" title="Protected workbook — Cresco_AU_Calc_Screw_Pile_Design_V1_0.xlsx"
         description="Formulas, macros and layout are locked. You can edit the input cells only." />
  <div class="my-3 flex justify-end gap-2">
    <Button label="Recalculate" icon-left="lucide-refresh-cw" />
    <Button label="Export JSON" />
    <Button variant="solid" label="Generate PDF" />
  </div>
  <div class="grid grid-cols-3 gap-3">
    <TextInput v-model="inputs.s_u" type="number" label="Undrained shear strength, S_u (kPa)" />
    <TextInput v-model="inputs.d_h" type="number" label="Helix diameter, D_h (mm)" />
    <TextInput v-model="inputs.n_c" type="number" label="Bearing factor, N_c" />
  </div>
  <List :columns="['minmax(0,1fr)', '8rem', '5rem']" class="mt-4">
    <ListRows :items="results" row-key="label" v-slot="{ item, value }">
      <ListRow :value="value">
        <ListCell>{{ item.label }}</ListCell>
        <ListCell class="font-mono text-right">{{ item.value }}</ListCell>
        <ListCell>{{ item.unit }}</ListCell>
      </ListRow>
    </ListRows>
  </List>
</template>""",
    },
    {
        "id": "32", "name": "Calculation Catalogue page (complete screen)", "file": "ready-made-panek.png",
        "used_in": "Calculation Catalogue",
        "frappe": "Breadcrumbs, Select, NumberCard, List, Button, Badge, Avatar",
        "available": "Yes", "fit": "Compose", "effort": "Medium",
        "gap": "A full page assembled from rows already covered: header breadcrumb (4) and profile (16), filters "
               "(19), stat boxes (3), the calculation table (23) and badges (1). The amber \"Awaiting your "
               "approval\" panel is a styled container with List rows and Approve / Return to draft Buttons "
               "(Alert only has one primary + one secondary action, so it doesn't fit a multi-row list).",
        "recommendation": "Compose from the components above; the approval panel is a small custom wrapper.",
        "docs": [DOCS + "charts/numbercard", DOCS + "molecules/list", DOCS + "components/breadcrumbs"],
        "code": """<script setup>
import { Breadcrumbs, Select, Button } from 'frappe-ui'
import { NumberCard } from 'frappe-ui/charts'
import { List, ListRows, ListRow, ListCell } from 'frappe-ui/list'

defineProps({ stats: Object, awaiting: Array })
</script>

<template>
  <Breadcrumbs :items="[{ label: 'Engineering Labs', route: '/engineering-labs' }, { label: 'Calculation Catalogue' }]" />
  <div class="mt-4 flex items-end justify-between">
    <h1 class="text-2xl font-semibold">Calculation Catalogue</h1>
    <div class="flex gap-2">
      <Select :options="['All types', 'API', 'Python', 'Excel']" placeholder="All types" />
      <Select :options="['All statuses', 'Approved', 'Draft']" placeholder="All statuses" />
    </div>
  </div>
  <div class="mt-4 grid grid-cols-4 gap-3">
    <NumberCard title="Approved & live" :value="stats.approved" color="#059669" />
    <NumberCard title="Awaiting approval" :value="stats.awaiting" color="#d97706" />
    <NumberCard title="Draft" :value="stats.draft" />
    <NumberCard title="Deprecated" :value="stats.deprecated" color="#dc2626" />
  </div>
  <section class="mt-4 rounded-lg border-l-4 border-amber-500 bg-surface-amber-1 p-4">
    <p class="mb-2 font-semibold text-ink-amber-3">Awaiting your approval</p>
    <List :columns="['minmax(0,1fr)', 'auto']">
      <ListRows :items="awaiting" row-key="name" v-slot="{ item, value }">
        <ListRow :value="value">
          <ListCell><strong>{{ item.title }}</strong> · {{ item.version }} · submitted by {{ item.submitted_by }}</ListCell>
          <ListCell class="flex gap-2">
            <Button variant="solid" theme="green" label="Approve" />
            <Button variant="outline" label="Return to draft" />
          </ListCell>
        </ListRow>
      </ListRows>
    </List>
  </section>
  <!-- calculation table: see component 23 -->
</template>""",
    },
    {
        "id": "33", "name": "Automation rule cards (horizontal list)", "file": "horizontal-cards.png",
        "used_in": "Automations page",
        "frappe": "List (frappe-ui/list) + Badge + Switch",
        "available": "Yes", "fit": "Compose", "effort": "Medium",
        "gap": "Each rule is one full-width row: title, a WHEN pill → DO pill (Badge, blue / violet, with an arrow "
               "icon between), a meta line (scope · owner · runs · last run), an italic description and an ON/OFF "
               "Switch. List gives one row per rule with a content cell and a switch cell. List draws rows with "
               "dividers, so the separate rounded, spaced cards in the screenshot need a small wrapper class "
               "(or render the rows with v-for in plain bordered divs). The ON caption under the switch is the same "
               "custom label as component 24.",
        "recommendation": "Use List (or v-for over bordered divs) with Badge + Switch; reuse the toggle from component 24.",
        "docs": [DOCS + "molecules/list", DOCS + "components/badge", DOCS + "components/switch"],
        "code": """<script setup>
import { Badge, Switch } from 'frappe-ui'
import LucideArrowRight from '~icons/lucide/arrow-right'

const props = defineProps({ rules: { type: Array, required: true } })
const emit = defineEmits(['toggle'])
</script>

<template>
  <div class="space-y-3">
    <div v-for="rule in rules" :key="rule.name"
         class="flex items-start justify-between gap-4 rounded-lg border border-outline-gray-1 bg-surface-base p-4">
      <div class="min-w-0 space-y-1.5">
        <h3 class="font-semibold text-ink-gray-9">{{ rule.title }}</h3>
        <div class="flex flex-wrap items-center gap-2">
          <Badge theme="blue" variant="outline" :label="`WHEN ${rule.trigger}`" />
          <LucideArrowRight class="size-3 text-ink-gray-5" />
          <Badge theme="violet" variant="outline" :label="`DO ${rule.action}`" />
        </div>
        <p class="text-xs text-ink-gray-5">
          Scope: {{ rule.scope }} · Owner: {{ rule.owner }} · {{ rule.runs }} runs · last {{ rule.last_run }}
        </p>
        <p class="text-xs italic text-ink-gray-5">{{ rule.description }}</p>
      </div>
      <div class="flex flex-col items-center gap-1">
        <Switch :model-value="rule.enabled" @update:model-value="(on) => emit('toggle', rule, on)" />
        <span class="text-xs font-semibold" :class="rule.enabled ? 'text-ink-green-3' : 'text-ink-gray-5'">
          {{ rule.enabled ? 'ON' : 'OFF' }}
        </span>
      </div>
    </div>
  </div>
</template>""",
    },
]
