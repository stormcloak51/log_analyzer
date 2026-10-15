from typing import Any


def print_report(stats: dict[str, Any]):
    print("=" * 40)
    print("         ОТЧЕТ ПО АНАЛИЗУ ЛОГА        ")
    print("=" * 40)
    print(f"Всего обработано записей: {stats['total_lines']}")
    print("\nРазделение по уровням:")
    # .items() -> [(key, value), (key, value)]
    for level, count in stats["levels"].items():
        print(f"- {level}: {count}")

    if stats["errors"]:
        print("\nСписок обнаруженных ошибок:")

        # enumerate() -> [(idx, value), (idx, value)]
        for idx, err in enumerate(stats["errors"], 1):
            print(f"  {idx}. {err}")

    print("=" * 40)
