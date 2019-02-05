x=0
def collatz(n):
    global x
    if x ==1:
        print("Done")
    while x !=1:
        if n%2==0:
            x = n//2
        elif n%2==1:
            x = 3*n +1
        print(x)
        collatz(x)
        
try:
    r=int(input("Enter your number : "))
    collatz(r)
except ValueError:
    print("Please enter an integer.")

