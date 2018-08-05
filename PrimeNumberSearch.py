#prime number search with a prompt
#find Nth prime number and asks if you want to find next
def prime(number):
    if number == 1:
        return 2
    elif number == 2:
        return 3
    else:
        primes=[1,3]
        x=3
        while len(primes) < number:
            for y in range (2, x):
                if x%y != 0:
                    if x not in primes:
                        primes.append(x)
                else:
                    if x in primes:
                        primes.remove(x)
                    break
            x+=1
        return primes[-1]

def question(entry):
    print("Prime number", entry, "is", prime(entry))
    print ("Do you want to find next in order?")
    while True:
        secondQuestion = input("Yes/No").lower()
        if secondQuestion == "yes":
            entry+=1
            print("Prime number", entry, "is", prime(entry))
        else:
            print("ok thank you!")
            break
if __name__ == "__main__":
    question(int(input("What order of prime number do you want to find")))
