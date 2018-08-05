#uses Ramanjunan's approximation to find decimals of pi

def factorial(number):
    if number == 0:
        return 1
    else:
        for x in range(1,number): #no recursion because there is a limit of a few 1000
            number*=x
    return number

def main(decimals):
    initNum = (2*2**(1/2))/9801
    pi=0
    for x in range(decimals):
        pi+=((factorial(4*x))*(1103+26390*x))/((factorial(x)**4)*(396**(4*x)))

    pi*=initNum
    print(pi)
    pi=1/pi
    print(pi)
if __name__ == "__main__":
    main(int(input("How many decimals of Pi do you want?")))
