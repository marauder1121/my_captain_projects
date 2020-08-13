def recurse(n):
  if n<=1:
    return n
  else:
    return recurse(n-1)+recurse(n-2)
num=20
for i in range(1,num):
  print(recurse(i),sep=' ,')
