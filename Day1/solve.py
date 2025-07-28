file = open("input.txt", "r")
content = file.read().replace('\n', '  ')

arrayofContent = content.split("  ")

numbersOnTheLeft = []
numberOnTheRight = []

for index, number in enumerate(arrayofContent):
    index += 1
    if index%2 == 0:
        numbersOnTheLeft.append(int(number))
    else:
        numberOnTheRight.append(int(number))

numbersOnTheLeft.sort()
numberOnTheRight.sort()

length = len(arrayofContent)

totalDifference = 0

for i in range(0, int(length/2)):
    difference = abs(numberOnTheRight[i] - numbersOnTheLeft[i])
    totalDifference += difference

print(totalDifference)


file.close()
