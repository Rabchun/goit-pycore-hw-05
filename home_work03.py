
def load_logs(file_path: str) -> list:

    with open(file_path, 'r') as log_file:
        return log_file.readlines()



def filter_logs_by_level(logs: list, level: str) -> list:

    filtered_logs = []
    for log_line in logs:
        parsed_log = parse_log_line(log_line)
        if parsed_log['level'] == level.upper():
            filtered_logs.append(log_line)
    return filtered_logs


def count_logs_by_level(logs: list) -> dict:

    log_counts = {'INFO': 0, 'ERROR': 0, 'DEBUG': 0, 'WARNING': 0}
    for log_line in logs:
        parsed_log = parse_log_line(log_line)
        log_counts[parsed_log['level']] += 1
    return log_counts


def display_log_counts(counts: dict):
   
    print("=== Статистика логів ===")
    for level, count in counts.items():
        print(f"{level}: {count}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Аналіз файлів логів")
    parser.add_argument("log_file", type=str, help="Шлях до файлу логів")
    parser.add_argument("-l", "--level", type=str, help="Фільтрувати за рівнем логування (INFO, ERROR, DEBUG, WARNING)", choices=["INFO", "ERROR", "DEBUG", "WARNING"])

    args = parser.parse_args()
