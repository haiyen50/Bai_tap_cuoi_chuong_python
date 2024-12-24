import math


class Diem:
    def __init__(self, x=0, y=0):
        self.x = x  # Tọa độ x
        self.y = y  # Tọa độ y


class Elip(Diem):
    def __init__(self, x, y, Ban_truc_lon, Ban_truc_nho):
        super().__init__(x, y)
        self.Ban_truc_lon = Ban_truc_lon
        self.Ban_truc_nho = Ban_truc_nho

    def Dien_tich(self):
        return math.pi * self.Ban_truc_lon * self.Ban_truc_nho


class Duong_tron(Elip):
    def __init__(self, x, y, Ban_kinh):
        super().__init__(x, y, Ban_kinh, Ban_kinh)
        self.Ban_kinh = Ban_kinh

    def Dien_tich(self):
        return math.pi * self.Ban_kinh ** 2


if __name__ == "__main__":
    x = float(input("Nhập tọa độ x của tâm elip: "))
    y = float(input("Nhập tọa độ y của tâm elip: "))
    Ban_truc_lon = float(input("Nhập bán trục lớn của elip: "))
    Ban_truc_nho = float(input("Nhập bán trục nhỏ của elip: "))

    Elip = Elip(x, y, Ban_truc_lon, Ban_truc_nho)

    print(f"Diện tích của elip là: {Elip.Dien_tich():.2f}")

    x_Duong_tron = float(input("\nNhập tọa độ x của tâm đường tròn: "))
    y_Duong_tron = float(input("Nhập tọa độ y của tâm đường tròn: "))
    Ban_kinh = float(input("Nhập bán kính của đường tròn: "))

    Duong_tron = Duong_tron(x_Duong_tron, y_Duong_tron, Ban_kinh)

    print(f"Diện tích của đường tròn là: {Duong_tron.Dien_tich():.2f}")
