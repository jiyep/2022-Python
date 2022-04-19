#packing
numbers= (1,2,3,4,5,6,7,8)

#inpacking
v1,v2,v3,v4,v5 = numbers
print(v1)

x, y = 10, 20
print(x, y)
x, y = y, x
print(x, y)

aa = [[1,2,3,4],
      [5,6],
      [7,8,9]]

totalSum = 0
for i in range(len(aa)):
    sum = 0
    for j in range(len(aa[i])):
        sum += aa[i][j]
        totalSum += aa[i][j]
        print(sum)
        print("total:", totalSum)


tt1 = (10, 20 ,30);  tt1
tt2 = 10, 20, 30; tt2



tt3 = (10); tt3
tt4 = 10; tt4   #튜플 없음
tt5=(10,); tt5
tt6 = 10,; tt6   #튜플 있음
#----------------------------------


myTurtle = (10,20,30)
myList = list(myTuple)
myList.append(40)
myList = tuple(myList)
myTurtle


