from math import gcd


class PS:
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so

    def kiem_tra_hop_le(self):
        return self.mau_so != 0

    def rut_gon(self):
        ucln = gcd(self.tu_so, self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln

    @staticmethod
    def nhap_phan_so():
        tu_so = int(input("Nhập tử số: "))
        mau_so = int(input("Nhập mẫu số: "))
        return PS(tu_so, mau_so)

    def in_phan_so(self):
        if not self.kiem_tra_hop_le():
            print("Phân số không hợp lệ! (mẫu số phải khác 0)")
        else:
            self.rut_gon()
            if self.mau_so == 1:
                print(f"Phân số: {self.tu_so}")
            else:
                print(f"Phân số: {self.tu_so}/{self.mau_so}")


if __name__ == "__main__":
    phan_so = PS.nhap_phan_so()
    phan_so.in_phan_so()
