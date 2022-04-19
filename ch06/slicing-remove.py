a = [10, 20, 30]
aa = [10, 20, 30, 40, 50]
re = [3, 5, 6, 8, 9, 80, 60, 70]

a[1:2] = [200, 201]
print(a)

a[1] = [200, 201]
print(a)

del(a[1])
print(a)

aa[1:4] = []
print(aa)

b = [10, 20, 30]; b = []; print(b)
bb = [10, 20, 30]; bb = None; print(bb)
# bbb = [10, 20, 30]; del(bbb); print(bbb)  오류발생

print(list(reversed(re)))
re.reverse()
print(re)
