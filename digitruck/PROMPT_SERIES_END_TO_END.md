# Claude Code Prompt Series — Build the DigiTruck Curriculum Static Site (End-to-End)

Use this sequence in order. Each prompt assumes the repo exists per Prompt 1.

---

## Prompt 1 — Initialize Project + Navigation
Create the full folder structure, shared CSS, and base navigation across:
- index.html
- modules/index.html
- personas/index.html
- schedules/index.html
Also create starter JSON data files in /data:
- modules.json
- personas.json
- schedules.json

---

## Prompt 2 — Define Data Schemas (modules/personas/schedules)
Create `/data/README.md` describing:
- Module metadata schema (fields + allowed values)
- Persona schema (persona id, name, description, default maturity entry)
- Schedule schema (schedule id, persona id, sessions list; each session links to module ids)
Include `schema_version`.

---

## Prompt 3 — Create the Module HTML Blueprint Template
Create:
- /templates/module-template.html (includes front-matter example)
- /templates/module-blueprint.md (human-readable blueprint)

---

## Prompt 4 — Create 11 Core Module Stubs
Create 11 module pages in `/modules/core/`:
- CORE-01 fundamentals
- CORE-02 communication
- CORE-03 safety-trust-privacy
- CORE-04 gov-eservices-appointments
- CORE-05 govpay-payments-receipts
- CORE-06 digital-banking-safe-use
- CORE-07 ai-awareness
- CORE-08 ai-aptitude-prompting-verification
- CORE-09 productivity-problem-solving
- CORE-10 pathways-opportunity
- CORE-11 gn-continuity-support

Populate each with:
- 3–5 outcomes
- 5–7 key concepts
- 2 activities
- 1 quick assessment
Add Sinhala/Tamil placeholders.
Update /data/modules.json.

---

## Prompt 5 — Create ToT Module Pack (4 modules)
Create ToT modules in `/modules/tot/`:
- TOT-01 facilitation-pacing
- TOT-02 assessment-certification
- TOT-03 safeguarding-escalation
- TOT-04 running-gn-microsessions
Update /data/modules.json.

---

## Prompt 6 — Create Persona Overview Pages (7)
For each persona folder under /personas, create:
- index.html (overview)
- day-1.html (DigiTruck schedule view)
- continuity.html (GN clinic plan view)
Update /data/personas.json.

---

## Prompt 7 — Create DigiTruck Day Schedules for Each Persona
Create schedule pages under `/schedules/digiTruck-day/` for each persona.
Each schedule lists Sessions 1–7 and links to 1–2 modules per session.
Update /data/schedules.json.

---

## Prompt 8 — Create GN Clinic Continuity Schedules
Create continuity schedule pages under `/schedules/gn-clinics/` per persona.
Include 4 weekly micro-sessions per month.
Update /data/schedules.json.

---

## Prompt 9 — Build the Module Library Index with Filters
Enhance /modules/index.html to read /data/modules.json and filter by:
persona, maturity, theme, session_fit, time.  
Use minimal vanilla JS.

---

## Prompt 10 — Add Cross-linking & Breadcrumbs
Add breadcrumbs to all pages and “Related modules” to each module page.

---

## Prompt 11 — Add Printable Job Aids & Trainer Scripts
For each core module, create:
- /assets/job-aids/{module_id}.html
- /assets/trainer-scripts/{module_id}.html

---

## Prompt 12 — Quality Pass
Ensure consistent typography, mobile readability, and no broken links.

---

## Prompt 13 — Optional Offline Pack (PWA-lite)
Add a manifest + service worker if feasible.

---

## Prompt 14 — Package for Release
Create `/RELEASE.md` with hosting instructions and version notes.
