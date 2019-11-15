def digitsum(m):
    if m <= 9 :
        return m
    else:
        return digitsum(sum([int(c) for c in str(m)]))

print(digitsum(987598759875))