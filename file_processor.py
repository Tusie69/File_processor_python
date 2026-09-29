from abc import abstractmethod

class FileProcessor:

    student_list = []

    def __init__(self):
        pass

    def print_student_list(self):
        for student in self.student_list:
            print(student)

    @abstractmethod
    def read_file_to_get_student_list():
        # lấy danh sách sinh viên từ các kiểu file khác nhau
        # Nhiệm vụ là fill vào mảng danh sách sinh viên
        pass