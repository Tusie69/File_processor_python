import argparse
from pathlib import Path
import sys

from CSV_Processor import CSVProcessor
from excel_processor import ExcelProcessor


def main():
    parser = argparse.ArgumentParser(description="Đọc danh sách sinh viên từ CSV/Excel")
    parser.add_argument(
        "file", nargs="?", type=Path,
        default=Path(__file__).resolve().with_name("students.csv"),
        help="File .csv hoặc .xlsx (mặc định: students.csv cạnh main.py)",
    )
    args = parser.parse_args()
    try:
        suffix = args.file.suffix.lower()
        if suffix == ".csv":
            processor = CSVProcessor()
        elif suffix == ".xlsx":
            processor = ExcelProcessor()
        else:
            raise ValueError("Chỉ hỗ trợ .csv và .xlsx")
        processor.read_file_to_get_student_list(args.file)
        processor.print_student_list()
    except Exception as exc:
        print(f"Lỗi đọc file: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    raise SystemExit(main())
