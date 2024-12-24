# Định nghĩa lớp TS (Thí Sinh)
class TS:
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

    @staticmethod
    def nhap_thong_tin():
        ho_ten = input("Nhập họ tên thí sinh: ")
        diem_toan = float(input("Nhập điểm Toán: "))
        diem_ly = float(input("Nhập điểm Lý: "))
        diem_hoa = float(input("Nhập điểm Hoá: "))
        return TS(ho_ten, diem_toan, diem_ly, diem_hoa)

    def in_thong_tin(self):
        print(f"Họ tên: {self.ho_ten} - Toán: {self.diem_toan} - Lý: {self.diem_ly} - Hoá: {self.diem_hoa} - Tổng điểm: {self.tinh_tong_diem()}")


def nhap_danh_sach_ts():
    ds_ts = []
    so_luong_ts = int(input("Nhập số lượng thí sinh: "))
    for _ in range(so_luong_ts):
        ts = TS.nhap_thong_tin()
        ds_ts.append(ts)
    return ds_ts


def in_ds_trung_tuyen(ds_ts, diem_chuan=20):
    ds_trung_tuyen = [ts for ts in ds_ts if ts.tinh_tong_diem() >= diem_chuan]
    ds_trung_tuyen.sort(key=lambda x: x.tinh_tong_diem(), reverse=True)
    print("\nDanh sách thí sinh trúng tuyển:")
    for ts in ds_trung_tuyen:
        ts.in_thong_tin()


if __name__ == "__main__":
    ds_ts = nhap_danh_sach_ts()
    in_ds_trung_tuyen(ds_ts)
