# A.T.L.A.S. — Adaptive Task & Lifecycle Automation System (Copilot Agent)

**A.T.L.A.S.** is a no‑code **Microsoft Copilot Studio** agent that converts a short project brief into executive‑ready PM artifacts:
**RAID, RACI, Stakeholder Map, Communications Plan, Phase 0–3 Roadmap, and KPIs/OKRs**.
It includes an **Industry Switch** (SaaS / Healthcare / FinTech / Energy) and a one‑click **PM Pack (PDF)** export via **Power Automate + Word + SharePoint**.

> Draft outputs only — review for policy, legal, and compliance before use.

## Why it matters
- ≤ **30 seconds** to a first‑draft plan (≈ **90% faster** in demo scenarios)
- Adapts risks, KPIs, compliance cues, and vocabulary to your **industry**
- Exports a board‑ready **PM Pack (PDF)** for SteerCo/executive review

## How it works (high level)
1. **Intake:** Industry → name → objective → constraints → stakeholders → risk tolerance  
2. **Generate:** RAID → RACI → Stakeholders → Comms Plan → Phase 0–3 Roadmap → KPIs/OKRs  
3. **Summarize:** One‑paragraph executive summary + Next‑7‑Days action list  
4. **Export:** Call **Generate PM Pack (PDF)** (Power Automate) and return a SharePoint link

## Demo
- 🎥 **60–90s video:** _Add your Loom/YouTube link here_
- 📄 **Sample PM Packs (PDF):** _Add Drive/OneDrive links here_
- 🔗 **Overview page:** _Add Google Sites/Notion link here_

## Architecture
See [`/docs/architecture.md`](docs/architecture.md).

## Action payload schema
See [`/schemas/generate_pm_pack_payload.schema.json`](schemas/generate_pm_pack_payload.schema.json).

## Knowledge (grounding)
- [`/knowledge/ATLAS_Industry_Profiles_v1.md`](knowledge/ATLAS_Industry_Profiles_v1.md)
- [`/knowledge/ATLAS_Templates_and_Definitions_v1.md`](knowledge/ATLAS_Templates_and_Definitions_v1.md)

## License
MIT © Jordan Polk
