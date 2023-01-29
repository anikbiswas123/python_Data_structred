
a=[5,2,10,6,7,3]
serch=10

found=0
for i in range(len(a)):
    if a[i] == serch:
        print(f"Data is found! locations is {i}")
        found =found+1
        break

if found == 0:
    print("data is not found!")
