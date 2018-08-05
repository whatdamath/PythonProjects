#uses Spigot algorithm to find decimals of pi
#much faster than previous algorithms, also allows to calculate individual
#decimal points of pi

def main(decimals):
    pi=0
    for x in range(decimals):
        pi+=(1/16**x)*((4/(8*x+1))-(2/(8*x+4))-(1/(8*x+5))-(1/(8*x+6)))
    print(pi)
if __name__ == "__main__":
    main(int(input("How many itterations of sum do you want?")))
