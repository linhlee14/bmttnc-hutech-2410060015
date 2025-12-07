def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]

user_input =input("Nhap chuoi can dao nguoc: ")
print("Chuoi sau khi dao nguoc la:", dao_nguoc_chuoi(user_input))

