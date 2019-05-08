a_f=0
b_f=0
c_f=0

for i in range(500):
    for j in range(500):
        for k in range(500):
            if i**2+j**2==k**2 and i+j+k==1000:
                print(i*j*k)
                break
