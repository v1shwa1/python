in1= int(input("Enter the 1st num: "))
in2= int(input("Enter the 2nd num: "))+1
for n in range(in1, in2 ):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n)
