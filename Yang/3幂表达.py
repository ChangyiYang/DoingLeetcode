
def f(n):
    # first, generate a sequence that a1* 1 + a2 * 3+ ... where a1 and a2 can be 0,1,2

    coef_list = []
    while n > 0:
        coef_list.append(n%3)
        n = n//3

    coef_list.append(0)


    s = ''
    base = 1

    for i in range(len(coef_list)):
        coef = coef_list[i]
        if coef == 2:
            coef_list[i] = -1
            coef_list[i+1]+= 1

        coef = coef_list[i]

        if coef == 0:
            base *= 3
            continue


        if coef == 1:
            symbol = '+'
        else:
            symbol = '-'
        s = symbol + str(base) + s
        base *= 3

        

    print(s[1:])


f(20)