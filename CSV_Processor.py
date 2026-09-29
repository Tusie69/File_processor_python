import csv

from file_processor import FileProcessor
from student import Student


class CSVProcessor(FileProcessor):
    def read_file_to_get_student_list(self, file_path):
        self.student_list = []
        with open(file_path, encoding="utf-8-sig", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if not row or not row[0]:
                    continue
                student = Student(
                    rollnumber=str(row[0]).strip(),
                    fullname=str(row[1]).strip(),
                    dob=row[2],
                )
                self.student_list.append(student)
