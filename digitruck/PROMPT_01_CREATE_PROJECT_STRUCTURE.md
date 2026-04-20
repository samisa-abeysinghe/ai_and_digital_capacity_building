# Claude Code Prompt — Create Project Structure (Static Curriculum Site)

You are building a static-site content repository for the DigiTruck Rural Digital Empowerment Curriculum.

## Objectives
1) Create a clean project folder structure for:
- central module library (core/local/tot)
- persona pages
- schedules
- assets (job aids, trainer scripts, assessment cards)
- data files (modules/personas/schedules)

2) Create starter index pages and navigation.

## Requirements
- Use wide compatibility HTML (no framework required).
- Use minimal JS; site should be fast and readable on mobile.
- Prepare for Sinhala/Tamil/English (placeholders and language fields).
- Use machine-readable metadata for modules (YAML/JSON front-matter or sidecar JSON).

## Output
Generate:
- directory tree
- starter HTML pages with navigation:
  - /index.html
  - /modules/index.html (module library index)
  - /personas/index.html (personas index)
  - /schedules/index.html
- /data/modules.json, /data/personas.json, /data/schedules.json
- shared CSS file: /assets/site.css (government proposal style: minimal, grayscale + one accent)

## Folder Structure
Use exactly:
- /modules/core
- /modules/local-plugins
- /modules/tot
- /personas/{schoolchildren,youth,women,entrepreneurs,elderly,gn-officials,tot-trainers}
- /schedules/digiTruck-day
- /schedules/gn-clinics
- /assets/{job-aids,assessment-cards,trainer-scripts}
- /data

## Conventions
- Filenames: kebab-case
- Stable IDs (do not change once referenced)
- Semantic version strings in metadata

Now produce the scaffold and starter files.
