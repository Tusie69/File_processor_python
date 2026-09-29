class Student:
    def __init__(self, rollnumber, fullname, dob):
        self.rollnumber = rollnumber
        self.fullname = fullname
        self.dob = dob

    def __str__(self):
        return f"MSSV: {self.rollnumber} | Họ tên: {self.fullname} | Ngày sinh: {self.dob}"
