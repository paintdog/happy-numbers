# Happy numbers
# https://oeis.org/A007770


def check_happy_number(n):
    while True:
        result = sum([int(a) ** 2 for a in str(n)])
        if result == 1:
            return True
        elif result == 4:
            return False
        else:
            n = result


for i in range(1,1000 + 1):
    if check_happy_number(i):
        print(i, end=", ")
    else:
        pass
