# student_manager.py
# Danh sách để lưu thông tin các sinh viên.
# Mỗi sinh viên là một dictionary.
student_list = []

def add_student(hoten, namsinh, diachi):
    student = {
    'ho_ten': hoten,
    'nam_sinh': namsinh,
    'dia_chi': diachi
    }
    student_list.append(student)
    print(f"Đã thêm sinh viên {hoten} thành công.")
    
def print_student_list():
    if not student_list:
        print("Danh sách sinh viên trống.")
        return
    for student in student_list:
        print(f"Họ tên: {student['ho_ten']}, Năm sinh: {student['nam_sinh']}, Địa chỉ: {student['dia_chi']}")
    
if __name__ == "__main__":
    print("--- CHUONG TRINH QUAN LY SINH VIEN ---")
    # Yêu cầu 1: Thêm sinh viên
    print("\n1. Them sinh vien:")
    add_student("Nguyen Van An", 2003, "Da Nang")
    add_student("Tran Thi Binh", 2002, "Quang Nam")
    add_student("Le Van Hung", 2003, "Hue")
    
    # Yêu cầu 2: In danh sách
    print("\n2. In danh sach sinh vien:")
    print_student_list()