import re

LOG_PATTERN = re.compile(
    r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+"
    r"\[(?P<level>[A-Z]+)\]\s+"
    r"(?P<message>.*)$"
)


def parse_log_file(file_path: str):
    parsed_entries = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if not line:
                continue
            match = re.match(LOG_PATTERN, line)
            if match:
                parsed_entries.append(match.groupdict())
    return parsed_entries
