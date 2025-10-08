# A.T.L.A.S. on AWS — Agents for Bedrock

**Why use it**
- Good for teams standardized on AWS.

## Prerequisites
- AWS account with access to **Agents for Bedrock** and a model (e.g., **Anthropic Claude**).
- S3 bucket for the **PM Pack** and knowledge files (optional RAG via Knowledge Bases).
- IAM role for the Agent and Lambda action.

## High‑Level Steps
1. **Create an Agent**
   - Bedrock Console → *Agents* → *Create agent* (name: `atlas-pm-twin`).
   - Paste a trimmed version of `docs/copilot_instructions.md` into the **instruction** field (remove Microsoft‑specific lines).
   - (Optional) Attach a **Knowledge Base** that indexes the industry/profile docs stored in S3.

2. **Action Group (Lambda)**
   - Create a Lambda function from `lambda/pm_pack.py` (Python 3.11).
   - Purpose: accept a JSON payload matching our schema, render tables into a Word or Markdown template, save PDF/ZIP to S3, return `file_url`.
   - Add an **Action group** in the Agent; import the **OpenAPI schema** in `lambda/openapi.json` to declare the tool.

3. **Test**
   - Use the built‑in chat in the Bedrock console. Provide the Sheboygan sample brief and verify S3 outputs.

## Cost & Limits
- You pay per token + Lambda/S3 costs. Keep sessions short and cache static content.
