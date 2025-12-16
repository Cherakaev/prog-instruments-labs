import csv
import re
from typing import List
from checksum import calculate_checksum, serialize_result


CSV_PATH = "27.csv"


REGEX = {
    "email": r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    "height": r"^\d\.\d{2}$",
    "snils": r"^\d{11}$",
    "passport": r"^\d{2} \d{2} \d{6}$",
    "occupation": r"^[A-Za-zА-Яа-яЁё\s\-\.\(\)/]+$",
    "longitude": r"^-?\d{1,3}\.\d+$",
    "hex_color": r"^#[0-9a-fA-F]{6}$",
    "issn": r"^\d{4}-\d{4}$",
    "locale_code": r"^[a-z]{2}(-[a-z0-9]{2,4})?$",
    "time": r"^\d{2}:\d{2}:\d{2}(\.\d+)?$"
}


def find_invalid_rows(
        file_path: str,
        encoding: str = "utf-16",
        delimiter: str = ";"
) -> List[int]:
    invalid_rows = []

    try:
        with open(file_path, "r", encoding=encoding, newline='') as f:
            reader = csv.DictReader(f, delimiter=delimiter)

            if reader.fieldnames:
                headers = set(reader.fieldnames)
                keys = set(REGEX.keys())
                if not keys.issubset(headers):
                    print(f"ВНИМАНИЕ: В CSV не найдены колонки: "
                          f"{keys - headers}")

            for row_index, row in enumerate(reader):
                for column, pattern in REGEX.items():
                    value = row.get(column, "") or ""
                    value = value.strip()

                    if not re.fullmatch(pattern, value):
                        invalid_rows.append(row_index)
                        break

        return sorted(set(invalid_rows))

    except FileNotFoundError:
        print(f"Файл {file_path} не найден!")
        return []


def main() -> None:
    invalid_rows = find_invalid_rows(CSV_PATH, encoding="utf-16", delimiter=";")

    print(f"Найдено невалидных строк: {len(invalid_rows)}")

    checksum = calculate_checksum(invalid_rows)
    print(f"Контрольная сумма: {checksum}")

    serialize_result(27, checksum)


if __name__ == "__main__":
    main()