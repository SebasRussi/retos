def facto(num, lim):
    if num == lim:
        return lim
    else:
        print(num)
        return facto(num + 1, lim)


print(facto(10, 15))



