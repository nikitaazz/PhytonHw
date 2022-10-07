n=int(input())
while n>-0:
  if n//2==0:
    n=n/10+1
  else:
    n=n%10+1
print(n)