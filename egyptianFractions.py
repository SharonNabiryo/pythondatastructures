#SHARON N NABIRYO


from math import ceil

def egyptian(n,d):

    print("The Egyptian Fraction of {}/{} is: ".format(n, d))
    ans  = []
    # while numerator is not 0
    while (n > 0):
        x = ceil(d / n)
        ans.append(x)
        n, d = x * n - d, d * x
    for a in ans:
        print("1/{}".format(a), end =" ")
    print()
        
        

def main():
    egyptian(5, 6)      #  1/2, 1/3 
    egyptian(7, 15)     #  1/3, 1/8, 1/120 
    egyptian(23, 34)    #  1/2 1/6 1/102 
    egyptian(121, 321)  # 1/3, 1/23, 1/7383
    egyptian(5, 123)    # 1/25, 1/1538, 1/4729350

main()
