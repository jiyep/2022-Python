a = ['one', 'two', 'three']
b = ['a', 'b', 'c']
print(list(zip(a, b)))

foods = ['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨']
sides = ['오뎅', '딘무지', '김치']
for food, side in zip(foods, sides):
    print(food, '--->', side)