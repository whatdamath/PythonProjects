#Collatz Conjecture - Start with a number n > 1. Find the number of steps it
#takes to reach one using the following process: If n is even, divide it by 2.
#If n is odd, multiply it by 3 and add 1.

def collatz(number):
    count = 0
    while number != 1:
        if number%2 == 1:
            number*3+1
        else:
            number/2
        count+=1
    return count

if __name__ == "__main__":
    collatz(int(input("Enter a number")))
    
