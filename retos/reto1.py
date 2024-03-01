def atras(num):
    if num == 0:
        return 0
    else:
        print(num)
        return atras(num - 1)


print(atras(10))