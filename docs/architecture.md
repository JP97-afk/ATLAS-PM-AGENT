# A.T.L.A.S. Architecture (high level)

**Core:** Microsoft Copilot Studio agent with Instructions enforcing: Industry‑first intake → artifact generation → executive summary → export.

**Grounding:** Industry profiles + artifact definitions uploaded as Knowledge for retrieval‑augmented responses.

**Industry Switch:** Global variable `Industry` (SaaS/Healthcare/FinTech/Energy) selects terminology, risks, KPIs, and compliance cues.

**Export:** Power Automate flow receives JSON payload → populates a Word template (content controls) → converts to PDF → saves to SharePoint → returns link.

```mermaid
flowchart LR
  A[Intake Form\n(Industry, Brief, Stakeholders, Risk Tolerance)] --> B[Copilot Studio Agent\n(A.T.L.A.S.)]
  B --> C[Artifacts\nRAID/RACI/Stakeholders/Comms/Roadmap/KPIs]
  C --> D[Executive Summary + Next-7-Days]
  D --> E[Power Automate Action\nGenerate PM Pack (PDF)]
  E --> F[Word Template → PDF]
  F --> G[SharePoint Link to PM Pack]
```
