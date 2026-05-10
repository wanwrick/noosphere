"""AI Consumption Contract generator.

Turns a parsed `data-contract.yml` into the AI Consumption Contract markdown
section that the AI-Ready Platinum Layer (Principle 5) mandates in every
data product PRD.

Consumers:
    - scripts/generate_ai_contract.py CLI wrapper
    - the dabs-template-init skill
"""

from __future__ import annotations

from typing import Any


def generate_ai_consumption_contract(contract: dict[str, Any]) -> str:
    """Render contract -> Markdown AI Consumption Contract section."""
    md = contract.get("metadata", {})
    ai = contract.get("ai_consumption", {})
    if not ai.get("enabled", False):
        return _disabled_template(md)

    parts: list[str] = []
    parts.append(f"## AI Consumption Contract — {md.get('name', '<unnamed>')}\n")
    parts.append(
        f"**Owner team:** `{md.get('owner_team', 'unknown')}` · "
        f"**Steward:** `{md.get('steward', 'unknown')}` · "
        f"**Classification:** `{md.get('classification', 'unknown')}` · "
        f"**Version:** `{md.get('version', {}).get('current', '?')}`\n"
    )

    parts.append("### Answerable questions\n")
    qs = ai.get("answerable_questions") or []
    if qs:
        parts.extend(f"- {q}" for q in qs)
        parts.append("")
    else:
        parts.append("_No questions declared. AI consumption is not contractual until populated._\n")

    parts.append("### Scoped views\n")
    views = ai.get("scoped_views") or []
    if views:
        parts.append("| Name | Grain | Columns | Purpose |")
        parts.append("|---|---|---|---|")
        for v in views:
            cols = ", ".join(v.get("columns", []))
            parts.append(
                f"| `{v.get('name', '')}` | {v.get('grain', '')} | "
                f"{cols} | {v.get('description', '')} |"
            )
        parts.append("")
    else:
        parts.append("_No scoped views declared. Agents will read raw tables, which is not recommended._\n")

    parts.append("### UC Functions\n")
    fns = ai.get("uc_functions") or []
    if fns:
        parts.append("| Name | Logic | Governance |")
        parts.append("|---|---|---|")
        for fn in fns:
            parts.append(
                f"| `{fn.get('name', '')}` | {fn.get('logic_summary', '')} | "
                f"{fn.get('governance', '')} |"
            )
        parts.append("")
    else:
        parts.append("_No UC Functions declared. Business logic must live in agent prompts, which is fragile._\n")

    parts.append("### Freshness commitment\n")
    fr = contract.get("freshness", {})
    parts.append(
        f"- SLA: **{fr.get('sla_minutes', '?')} min** ({fr.get('measurement', 'unspecified')})\n"
    )

    parts.append("### Metadata coverage\n")
    parts.append(
        "- **Grain:** " + contract.get("grain", {}).get("description", "unspecified") + "\n"
        "- **Time coverage:** see source metadata; populate from registry.\n"
        "- **Currency / units:** see column descriptions.\n"
        "- **Out of scope:** populate before agent consumption begins.\n"
    )

    parts.append("### Consumed by\n")
    consumed = contract.get("consumed_by", {})
    if consumed.get("ai_agents"):
        parts.append(f"- AI agents: {', '.join(consumed['ai_agents'])}\n")
    if consumed.get("bi"):
        parts.append(f"- BI tools: {', '.join(consumed['bi'])}\n")
    parts.append(
        "\n---\n_Auto-generated from `data-contract.yml`. Do not hand-edit; "
        "update the contract and regenerate via `scripts/generate_ai_contract.py`._\n"
    )
    return "\n".join(parts)


def _disabled_template(md: dict[str, Any]) -> str:
    return (
        f"## AI Consumption Contract — {md.get('name', '<unnamed>')}\n\n"
        "**AI consumption is currently disabled** for this data product "
        "(`ai_consumption.enabled: false`). Set to `true` and regenerate this "
        "section before any agent is allowed to read this product's tables.\n"
    )
