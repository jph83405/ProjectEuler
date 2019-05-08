sum_1=0
sum_2=0

for i in range(101):
    sum_1+=i

for i in range(101):
    sum_2+=i**2

print(sum_1**2-sum_2)
