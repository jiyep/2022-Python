sum = 0
myList=[ [1, 2],
         [3, 4, 5, 6],
         [7, 8, 9],
         [10] ]

print(myList)
print(len(myList))
print(len(myList[0]))
print(myList[1])
print(myList[1][2])

for i in range(0, len(myList)):
    for j in range(0, len(myList[i])):
        sum += myList[i][j]

print(sum)