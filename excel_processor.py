from openpyxl import load_workbook

from file_processor import FileProcessor
from student import Student


class ExcelProcessor(FileProcessor):
    def read_file_to_get_student_list(self, file_path):
        self.student_list = []
        workbook = load_workbook(file_path, read_only=True, data_only=True)
        try:
            sheet = workbook.active
            for row in sheet.iter_rows(min_row=2, values_only=True):
                if row[0] is None:
                    continue
                student = Student(
                    rollnumber=str(row[0]).strip(),
                    fullname=str(row[1]).strip(),
                    dob=row[2],
                )
                self.student_list.append(student)
        finally:
            workbook.close()
