def chia_het_cho_5(so_nhi_phan):
    so_thap_phan = int(so_nhi_phan,2)
    if so_thap_phan % 5==0:
        return True
    else:
        return False

user_input = input("Nhap cac so nhi phan co 4 chu so cach nhau boi dau phay: ")

input_list = user_input.split(",")
so_chia_het_cho_5 = [so for so in input_list if chia_het_cho_5(so)]
if len(so_chia_het_cho_5) > 0:
    ket_qua = ",".join(so_chia_het_cho_5)
    print("Cac so nhi phan chia het cho 5 la:", ket_qua)
else:
    print("Khong co so nhi phan nao chia het cho 5")

    