import re

file = open("/home/nahomkasa/Documents/puzzel/Day3/input.txt", "r")
content = file.read()

trc = "mul(1,2)mul(0,7)"
allMulwithNumbers = re.findall(r"mul\(\d+\,\d+\)",content)
NumbersOnly = [re.findall(r"\d+", x) for x in allMulwithNumbers]

sumOfMultiple = 0

for PairOfMultiple in NumbersOnly:
    multiple = int(PairOfMultiple[0]) * int(PairOfMultiple[1])
    sumOfMultiple += multiple

print(sumOfMultiple)
