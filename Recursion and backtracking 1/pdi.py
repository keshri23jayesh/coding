def pdi(num):
    if num == 0:
        return
    print(num)
    pdi(num - 1)
    print(num)


pdi(5)
