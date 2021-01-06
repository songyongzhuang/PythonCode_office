# -*-coding=utf-8-*-

# 2.分别使用for和while打印九九乘法表，格式：每项数据之间空一个Tab键，可以使用"\t"

# for方法
for i in range(1, 10):
    for j in range(1, i+1):
        print("{} * {} = {}".format(j, i, j*i), end="\t")
    print()

print("*" * 120)


# while方法
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("{} * {} = {}".format(j, i, j * i), end="\t")
        j += 1
    i += 1
    print()


