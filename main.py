import argparse
from log_analyzer.parser import parse_log_file
from log_analyzer.stats import calculate_stats
from log_analyzer.reporter import print_report


def main():
    parser = argparse.ArgumentParser(description="CLI анализатор лог-файлов")
    parser.add_argument("logfile", help="Путь к файлу логов")
    args = parser.parse_args()

    entries = parse_log_file(args.logfile)

    stats = calculate_stats(entries)

    print_report(stats)


if __name__ == "__main__":
    main()
