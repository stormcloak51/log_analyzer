from collections import Counter
from typing import Any


def calculate_stats(log_entries: list[dict[str, str]]) -> dict[str, Any]:
    total = len(log_entries)
    levels = Counter()
    errors: list[str] = []

    for entry in log_entries:
        lvl = entry.get("level")
        if lvl:
            levels[lvl] += 1

        if lvl == "ERROR":
            msg = entry.get("message")
            if msg:
                errors.append(msg)

    return {"total_lines": total, "levels": dict(levels), "errors": errors}
