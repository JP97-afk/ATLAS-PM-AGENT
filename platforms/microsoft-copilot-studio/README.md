# A.T.L.A.S. on Microsoft Copilot Studio (Recommended)

**Why this platform**
- No‑code build; native export via **Power Automate + Word + SharePoint**.

## Prerequisites
- Microsoft 365 tenant with **Copilot Studio** and **Power Automate (Premium)** licenses.
- SharePoint/OneDrive location for the **PM Pack** PDFs.
- Word template with content controls (see repo `templates/word_template_mapping.md`).

## Build Steps
1. **Create the Copilot**
   - Copilot Studio → *Create a copilot*.
   - Name: **A.T.L.A.S. — PM Twin**.
   - Paste **full instructions** from `docs/copilot_instructions.md` into *Instructions*.

2. **Variables**
   - Create **Industry** (Choices: SaaS, Healthcare, FinTech, Energy, Engineering).
   - Create **RiskTolerance** (Choices: Low, Medium, High).

3. **Knowledge**
   - Upload: `knowledge/ATLAS_Industry_Profiles_v1.md` and `knowledge/ATLAS_Templates_and_Definitions_v1.md`.

4. **Topic: Set Industry (optional)**
   - Simple prompt with buttons for the five industries; set the **Industry** variable.

5. **Action: Generate PM Pack (PDF)**
   - Create a **Power Automate** flow with trigger **“When an HTTP request is received.”**
   - Paste JSON schema from `schemas/generate_pm_pack_payload.schema.json`.
   - Actions:
     1. *Populate a Microsoft Word template* (map fields per `templates/word_template_mapping.md`).
     2. *Convert Word to PDF*.
     3. *Create file in SharePoint/OneDrive*.
     4. *Respond to Copilot* with the file link.

6. **Test**
   - Use `samples/sample_brief_saas.md` as the brief.
   - Verify artifacts (RAID, RACI, Stakeholders, Comms, Roadmap, KPIs) and PDF export.


