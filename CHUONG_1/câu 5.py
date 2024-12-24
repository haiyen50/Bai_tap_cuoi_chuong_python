# Định nghĩa lớp Stack (Ngăn Xếp)
class Stack:
    def __init__(self, size):
        # Hàm tạo: khởi tạo ngăn xếp với kích thước cố định
        self.stack = []  # Sử dụng danh sách để lưu các phần tử trong ngăn xếp
        self.size = size  # Kích thước tối đa của ngăn xếp

    # Phương thức kiểm tra ngăn xếp có trống không
    def isEmpty(self):
        return len(self.stack) == 0

    # Phương thức kiểm tra ngăn xếp có đầy không
    def isFull(self):
        return len(self.stack) == self.size

    # Phương thức thêm phần tử vào ngăn xếp (push)
    def push(self, value):
        if self.isFull():
            print("Ngăn xếp đã đầy, không thể thêm phần tử!")
        else:
            self.stack.append(value)
            print(f"Đã thêm {value} vào ngăn xếp.")

    # Phương thức lấy phần tử ra khỏi ngăn xếp (pop)
    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp trống, không thể lấy phần tử!")
            return None
        else:
            popped_value = self.stack.pop()
            print(f"Đã lấy {popped_value} ra khỏi ngăn xếp.")
            return popped_value

    # Phương thức in nội dung của ngăn xếp
    def print(self):
        if self.isEmpty():
            print("Ngăn xếp trống.")
        else:
            print("Nội dung ngăn xếp:", self.stack)


# Chương trình chính
if __name__ == "__main__":
    # Khởi tạo một ngăn xếp với kích thước tối đa là 5
    stack = Stack(5)

    # Thêm các phần tử vào ngăn xếp
    stack.push(3.5)
    stack.push(2.1)
    stack.push(4.8)
    stack.push(7.3)
    stack.push(9.6)

    # Thử thêm phần tử khi ngăn xếp đã đầy
    stack.push(10.0)

    # In nội dung ngăn xếp
    stack.print()

    # Lấy phần tử ra khỏi ngăn xếp
    stack.pop()
    stack.pop()

    # In lại nội dung ngăn xếp
    stack.print()

    # Kiểm tra ngăn xếp có trống không
    if stack.isEmpty():
        print("Ngăn xếp hiện đang trống.")
    else:
        print("Ngăn xếp hiện không trống.")
