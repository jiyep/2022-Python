#주석문(코멘트)
#for range step 이용하여 짝수만 더하기

sum = 0

for i in range(2, 11, 2):
    print(i)
    sum += i


print('합계 : ', sum)