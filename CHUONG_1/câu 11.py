import math


class Tam_giac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def kiem_tra(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    def chu_vi(self):
        return self.a + self.b + self.c

    def dien_tich(self):
        if not self.kiem_tra():
            return None
        s = self.chu_vi() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class Tam_giac_can(Tam_giac):
    def __init__(self, canh_bang_nhau, do_dai_day):
        super().__init__(canh_bang_nhau, canh_bang_nhau, do_dai_day)
        self.canh_bang_nhau = canh_bang_nhau
        self.do_dai_day = do_dai_day

    def chieu_cao(self):
        return math.sqrt(self.canh_bang_nhau**2 - (self.do_dai_day / 2)**2)

    def dien_tich(self):
        return (self.do_dai_day * self.chieu_cao()) / 2


class Tam_giac_deu(Tam_giac_can):
    def __init__(self, canh):
        super().__init__(canh, canh)
        self.canh = canh

    def dien_tich(self):
        return (math.sqrt(3) / 4) * (self.canh ** 2)


if __name__ == "__main__":
    a = float(input("Nhập cạnh a của tam giác: "))
    b = float(input("Nhập cạnh b của tam giác: "))
    c = float(input("Nhập cạnh c của tam giác: "))

    tam_giac = Tam_giac(a, b, c)

    if tam_giac.kiem_tra():
        print(f"Chu vi tam giác: {tam_giac.chu_vi():.2f}")
        print(f"Diện tích tam giác: {tam_giac.dien_tich():.2f}")
    else:
        print("Tam giác không hợp lệ!")

    canh_bang_nhau = float(input("\nNhập cạnh bằng của tam giác cân: "))
    do_dai_day = float(input("Nhập cạnh đáy của tam giác cân: "))

    tam_giac_can = Tam_giac_can(canh_bang_nhau, do_dai_day)

    if tam_giac_can.kiem_tra():
        print(f"Chu vi tam giác cân: {tam_giac_can.chu_vi():.2f}")
        print(f"Diện tích tam giác cân: {tam_giac_can.dien_tich():.2f}")
    else:
        print("Tam giác cân không hợp lệ!")

    side = float(input("\nNhập cạnh của tam giác đều: "))

    tam_giac_deu = Tam_giac_deu(side)

    print(f"Chu vi tam giác đều: {tam_giac_deu.chu_vi():.2f}")
    print(f"Diện tích tam giác đều: {tam_giac_deu.dien_tich():.2f}")
