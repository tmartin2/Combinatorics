import math
import sys

while True:
    to_calc = input("Enter: ")
    if to_calc is "q":
        sys.exit()
    left_num = int(to_calc.split(",")[0][2:])
    right_num = int(to_calc.split(",")[1][:-1])
    diff = left_num - right_num
    if to_calc[0] is "C":
        r = math.factorial(left_num) / (math.factorial(right_num)*math.factorial(diff))
        print(r)
    elif to_calc[0] is "M":
        r = math.factorial(right_num) / math.factorial(abs(diff))
        print(r)
    else:
        r = math.factorial(left_num) / math.factorial(diff)
        print(r)
