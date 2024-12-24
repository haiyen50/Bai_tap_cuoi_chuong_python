class hinh_chu_nhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def chu_vi(self):
        return (self.chieu_rong + self.chieu_dai) * 2

    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong

    def thong_tin(self):
        print("Chiều dài của hình chữ nhật là: ", self.chieu_dai)
        print("Chiều rộng của hình chữ nhật là: ", self.chieu_rong)


chieu_dai = int(input("nhập chiều dài của hình chữ nhật: "))
chieu_rong = int(input("nhập chiều rộng của hình chữ nhật: "))
hinh_chu_nhat = hinh_chu_nhat(chieu_dai, chieu_rong)
hinh_chu_nhat.thong_tin()
print("Chu vi của hình chữ nhật là: ", hinh_chu_nhat.chu_vi())
print("Diện tích của hình chữ nhật là: ", hinh_chu_nhat.dien_tich())
