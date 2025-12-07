
def kiem_tra_so_nguyen_to(so):
    if so <=1:
        return False
    for i in range(2, int(so**0.5)+1):
        if so % i ==0:
            return False
    return True
number = int(input("Nhap vao so can kiem tra: "))

if kiem_tra_so_nguyen_to(number):
    print(number, "la so nguyen to")
else:
    print(number, "khong phai la so nguyen to")
    
        