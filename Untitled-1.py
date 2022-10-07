import random
spysok=[]
lowest=10
high=-10
for i in range(20):
  k=random.randint(-10,10)
  if k>high:
    high=k
  if k<lowest:
    lowest=k
print(high-lowest)