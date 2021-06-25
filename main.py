def checkIfPrime(n):
    prime = True
    for i in range(2, n - 1):
        if n % i == 0:
            prime = False
            break
        else:
            pass
        
    if prime == True:
        return "Prime"
    elif prime == False:
        return "Composite"
    
def myProg():
    StartNum = int(input("Number 1: "))
    EndNum = int(input("Number 2: "))

    composites = []
    primes = []

    for j in range(StartNum, EndNum + 1):
        status_J = checkIfPrime(j)
        if status_J == "Prime":
            primes.append(j)
        elif status_J == "Composite":
            composites.append(j)

    print("The primes are: ")
    print(primes)

    print("The composites are: ")
    print(composites)
    
myProg()