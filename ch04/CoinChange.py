coin = 0

coin = int(input("교환할 돈은 얼마? : "))

c500 = coin // 500
coin %= 500

c100 = coin // 100
coin %= 100

c50 = coin // 50
coin %= 50

c10 = coin // 10
coin %= 10

print('\n500원 짜리==>%d 개' %c500)
print('100원 짜리==>%d 개' %c100)
print('50원 짜리==>%d 개' %c50)
print('500원 짜리==>%d 개' %c10)
print('잔돈==>%d 원' %coin)