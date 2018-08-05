#Fibonacci sequence to the Nth number
#https://en.wikipedia.org/wiki/Fibonacci_number

def fibonacci(number):
    if number < 2:
        return number
    else:
        return (fibonacci(number-1) + fibonacci(number-2))

if __name__ == "__main__":
    print(fibonacci(int(input("How many numbers do you want to see?"))))
