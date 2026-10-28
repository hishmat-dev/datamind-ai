"""Text report generation for experiments."""
from __future__ import annotations
from pathlib import Path


def write_metrics_report(
    path: Path,
    title: str,
    metrics: dict[str, float],
    extra_lines: list[str] | None = None,
) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"# {title}", "", "## Metrics", ""]
    for k, v in metrics.items():
        if isinstance(v, float):
            lines.append(f"- **{k}**: {v:.6f}")
        else:
            lines.append(f"- **{k}**: {v}")
    if extra_lines:
        lines.extend(["", "## Notes", ""])
        lines.extend(f"- {line}" for line in extra_lines)
    lines.append("")
    path.write_text("\n".join(lines))
    return path