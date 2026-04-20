# DigiTruck Rural Digital Empowerment Curriculum — Claude Code Context Pack (v1.0.0)
**Prepared for:** Claude Code implementation session  
**Prepared by:** Samisa Abeysinghe, Harsha Purasinghe  
**Task Force:** National Digital Capacity Building Task Force  
**Version:** 1.0.0  
**Date:** 19th February 2026  

---

## 0) What this pack is
This markdown consolidates the project requirements, information architecture, and content design rules for building a **static-site curriculum library** for Sri Lanka’s **DigiTruck** rural digital empowerment program.

The site must support:
- A **central repository of modules** (reusable content units)
- A **maturity model** per persona
- **Persona tracks & schedules** that compose modules (DigiTruck 7-session day + GN continuity)
- **ToT (Train-the-Trainer)** content for sustained GN-level delivery

---

## 1) Delivery model & governance assumptions
### 1.1 Administrative delivery ladder
Delivery follows the administrative structure:
**National → Province → District → DS (Divisional Secretariat) → GN (Grama Niladhari Division)**

### 1.2 GN Digital Empowerment Cell (GDEC)
GN-level continuity is enabled by a GN Digital Empowerment Cell:
- Grama Niladhari (Convenor)
- Development Officer
- Women & Children Officer
- Health Officer / PHI
- Youth Officer

### 1.3 Sustainability model
DigiTruck provides **one-day immersion**; the GN Cell + **Local Trainer Pod** provides continuity:
- Local Trainer Pod: youth peer trainers + women peer trainers + elder-support helper + (optional) school-linked champion
- Monthly GN micro-sessions / clinics
- Escalation/support desk patterns through DS/GN

---

## 2) Personas (7 categories)
These are the program’s primary curriculum personas:
1. **Schoolchildren (Grades 6–13)**
2. **Youth**
3. **Women**
4. **Rural Entrepreneurs**
5. **Elderly / Digitally Excluded Adults**
6. **GN Cell Officials**
7. **Local Trainers (ToT)**

---

## 3) Core spine (common curriculum areas across personas)
All personas share a consistent “core spine” (depth varies by persona):
1. Digital Confidence & Fundamentals  
2. Communication & Digital Etiquette  
3. Safety, Trust & Privacy  
4. Government Digital Services & Civic e-Services (official source verification, accounts, forms/uploads, status tracking, appointments)  
5. Digital Payments for Government Services (GovPay-type flows, receipts, failure handling, fake link avoidance)  
6. Digital Banking & Safe Personal Finance Use (balances/transfers/bill pay/history, beneficiaries/limits/alerts, dispute steps, fraud prevention, public Wi-Fi risk; entrepreneurs: reconciliation + separation of personal/business)  
7. AI Awareness (what AI is/isn’t, limitations, bias, privacy, ethics)  
8. AI Aptitude (prompting + “verify before trust”, safe use)  
9. Problem-Solving & Productivity Habits (checklists, templates, time planning, using tools to finish work)  
10. Pathways to Opportunity (life + livelihood)  
11. Community Continuity & Support System (GN anchored)  

**Local plug-ins** (GN-selected): health, agriculture, fisheries, tourism, disaster resilience, local SME needs.

---

## 4) DigiTruck day structure (7 sessions)
DigiTruck daily flow (wide applicability):
- Session 1 (45m): Digital Confidence & Setup  
- Session 2 (45m): Communication & Etiquette  
- Session 3 (45m): Safety, Trust & Privacy  
- Session 4 (60–75m): Gov e-Services + Appointments + GovPay  
- Session 5 (60–75m): Digital Banking + Payments  
- Session 6 (60–75m): AI Awareness + AI Aptitude Lab  
- Session 7 (60–75m): Capstone + Assessment + Certification + GN Handoff

---

## 5) Curriculum maturity model (required)
Use a maturity model to structure progression and allow composition:
- **M0 Awareness:** knows it exists + basic risks
- **M1 Basic Use:** can perform with guidance
- **M2 Independent Use:** can complete tasks safely alone
- **M3 Applied Outcomes:** applies to life/livelihood; may help others

Each module must declare:
- minimum maturity (entry)
- target maturity (exit)
- proof of capability (observable output)

---

## 6) Content architecture (static site)
### 6.1 Three-layer approach
A) **Module Repository (source of truth)**  
B) **Persona Tracks & Schedules (composed views)**  
C) **Delivery Views** (trainer/learner/GN clinic/ToT)

### 6.2 Folder structure (proposed)
```
/modules/
  /core/
  /local-plugins/
  /tot/
/personas/
  /schoolchildren/
  /youth/
  /women/
  /entrepreneurs/
  /elderly/
  /gn-officials/
  /tot-trainers/
/schedules/
  /digiTruck-day/
  /gn-clinics/
/assets/
  /job-aids/
  /assessment-cards/
  /trainer-scripts/
/data/
  modules.json
  personas.json
  schedules.json
```

---

## 7) Module blueprint (must be consistent)
Each module is a standalone HTML page with:
- Title + purpose
- Persona applicability
- Maturity entry/exit
- Time
- Outcomes (3–5)
- Key concepts (5–7)
- Activities (2–3)
- Assessment (1–2)
- Job aid (1-page checklist)
- Safety / safeguarding notes
- Localization slot

### 7.1 Machine-readable metadata (front-matter)
Use YAML or JSON front-matter at top of each module page (or a sidecar JSON).
Example:
```yaml
module_id: CORE-04-GOV-ESERVICES
title: Government e-Services & Appointments
persona_tags: [youth, women, entrepreneurs, elderly, gn-officials, tot-trainers, schoolchildren]
maturity_min: M0
maturity_target: M2
session_fit: [S4]
time_minutes: 75
core_themes: [e-services, govpay, trust]
prerequisites: [CORE-03-SAFETY-TRUST]
outputs: ["Completed appointment workflow (mock)", "Saved receipt screenshot"]
assessment: ["2-question safety check", "Complete a guided workflow"]
safeguarding_level: strict
language: [si, ta, en]
version: 1.0.0
```

---

## 8) Non-negotiables (quality & safety)
- **Trust-by-design:** explicit fraud prevention; never share OTP/PIN/password.
- **Responsible AI rules:** AI is helper; verify; never input sensitive data.
- **Low-bandwidth & phone-first:** pages must render fast, minimal JS.
- **Bilingual readiness:** Sinhala/Tamil/English placeholders supported.

---

## 9) What to build
### 9.1 Minimum viable static site
- Home + navigation
- Module Library index with filters (persona, session, maturity, theme)
- Persona pages (7) with schedules and linked modules
- Schedule pages: DigiTruck day + GN clinics
- ToT section
- Data JSON files for modules/personas/schedules

### 9.2 Suggested initial module set (starter stubs)
Core (11):
- CORE-01 Fundamentals
- CORE-02 Communication
- CORE-03 Safety/Trust/Privacy
- CORE-04 Gov e-Services & Appointments
- CORE-05 GovPay-type Payments & Receipts
- CORE-06 Digital Banking & Safe Use
- CORE-07 AI Awareness
- CORE-08 AI Aptitude (Prompting + Verification)
- CORE-09 Productivity & Problem-Solving
- CORE-10 Opportunity Pathways
- CORE-11 GN Continuity & Support

ToT (4):
- TOT-01 Facilitation & Pacing
- TOT-02 Assessment & Certification Handling
- TOT-03 Safeguarding & Incident Escalation
- TOT-04 Running GN Micro-Sessions

---
