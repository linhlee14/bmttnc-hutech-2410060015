row = int(input("Nhap so hang: "))
col = int(input("Nhap so cot: "))
matran = [[i*j for j in range(col)] for i in range(row)]
print(matran)