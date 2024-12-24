class Da_giac:
    def __init__(self, canh):
        self.canh = canh  # Lưu trữ số cạnh của đa giác


class Hinh_binh_hanh(Da_giac):
    def __init__(self, do_dai_day, chieu_cao, canh_ben):
        super().__init__(4)  # Hình bình hành có 4 cạnh
        self.do_dai_day = do_dai_day  # Độ dài đáy
        self.chieu_cao = chieu_cao  # Chiều cao
        self.canh_ben = canh_ben  # Chiều dài cạnh bên

    # Tính chu vi hình bình hành
    def chu_vi(self):
        return 2 * (self.do_dai_day + self.canh_ben)

    # Tính diện tích hình bình hành
    def dien_tich(self):
        return self.do_dai_day * self.canh_ben


class Hinh_chu_nhat(Hinh_binh_hanh):
    def __init__(self, chieu_rong, chieu_dai):
        super().__init__(chieu_rong, chieu_dai, chieu_rong)  # Với hình chữ nhật, cạnh bên bằng cạnh đáy
        self.chieu_rong = chieu_rong
        self.chieu_dai = chieu_dai

    # Tính chu vi hình chữ nhật
    def chu_vi(self):
        return 2 * (self.chieu_rong + self.chieu_dai)

    # Tính diện tích hình chữ nhật
    def dien_tich(self):
        return self.chieu_rong * self.chieu_dai


# Lớp Hình vuông (Square) kế thừa từ Hình chữ nhật
class Hinh_vuong(Hinh_chu_nhat):
    def __init__(self, chieu_rong_hv):
        super().__init__(chieu_rong_hv, chieu_rong_hv)  # Hình vuông có chiều rộng bằng chiều cao
        self.chieu_rong_hv = chieu_rong_hv

    # Tính chu vi hình vuông
    def chu_vi(self):
        return 4 * self.chieu_rong_hv

    # Tính diện tích hình vuông
    def dien_tich(self):
        return self.chieu_rong_hv ** 2


# Chương trình chính
if __name__ == "__main__":
    # Tạo một hình bình hành
    hinh_binh_hanh = Hinh_binh_hanh(do_dai_day=10, chieu_cao=5, canh_ben=7)
    print("Hình bình hành:")
    print("Chu vi:", hinh_binh_hanh.chu_vi())
    print("Diện tích:", hinh_binh_hanh.dien_tich())

    # Tạo một hình chữ nhật
    hinh_chu_nhat = Hinh_chu_nhat(chieu_rong=8, chieu_dai=6)
    print("\nHình chữ nhật:")
    print("Chu vi:", hinh_chu_nhat.chu_vi())
    print("Diện tích:", hinh_chu_nhat.dien_tich())

    # Tạo một hình vuông
    hinh_vuong = Hinh_vuong(chieu_rong_hv=4)
    print("\nHình vuông:")
    print("Chu vi:", hinh_vuong.chu_vi())
    print("Diện tích:", hinh_vuong.dien_tich())
