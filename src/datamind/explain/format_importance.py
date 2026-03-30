from __future__ import annotations

def format_importance_table(importances: dict[str, float]) -> str:
    lines = ['feature,score']
    for k, v in sorted(importances.items(), key=lambda kv: -abs(kv[1])):
        lines.append(f'{k},{v:.6f}')
    return '\n'.join(lines)
