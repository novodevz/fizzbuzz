from icecream import ic # type: ignore


for n in range(1, 101):
    if n % 15 == 0: print(ic('fizzbuzz'))
    elif n % 3 == 0: print('fizz')
    elif n % 5 == 0: print('buzz')
    else: print(n)