n = int(input("print Even numbers: "))
even = 0
even_num = []
while even<n:
    even = even+2
    if even == 10:
        continue
    even_num.append(even)