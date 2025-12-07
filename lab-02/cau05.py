so_gio = float(input("Nhap so gio lam viec tuan nay: "))
muc_luongTC = float(input("Nhap muc luong tieu chuan cua ban: "))
gio_TC = 44
if so_gio <= gio_TC:
    tien_thuc_nhan = so_gio * muc_luongTC
    print(f"{tien_thuc_nhan:.2f}")
else:
    tien_thuc_nhan = (gio_TC * muc_luongTC) + ((so_gio-gio_TC)*muc_luongTC*1.5)
    print(f"{tien_thuc_nhan:.2f}")
