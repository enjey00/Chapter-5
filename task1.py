def funnyString(s):
    ascii_l = [ord(x) for x in s ]
    subtracted_l = []

    for i in range(len(ascii_l)-1):
        subtracted_nums = ascii_l[i]-ascii_l[i+1]
        subtracted_l.append(abs(subtracted_nums))

    if subtracted_l == subtracted_l[::-1]:
        print('Funny')

    elif subtracted_l != subtracted_l[::-1]:
        print('Not Funny')

funnyString('acxz')
funnyString('bcxz')