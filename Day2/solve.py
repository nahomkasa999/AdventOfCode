file = open("/home/nahomkasa/Documents/puzzel/Day2/input.txt", "r")
content = file.read()

lines = content.splitlines()
safe = 0
unsafe = 0

for data in lines:
    Data = data.split()
    NumData = [int(numbers) for numbers in Data]

    difference = [NumData[i + 1] - NumData[i] for i in range(len(NumData) - 1)]
    
    if all(diff >= 0 for diff in difference) or all(diff <= 0 for diff in difference):
        if all(1 <= abs(diff) <= 3 for diff in difference):
            safe += 1
    else:
        unsafe += 1

print(safe, unsafe)
    