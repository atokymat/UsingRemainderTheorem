import copy
def factors(x):
    "Returns factors of the absolute value of x"
    factors = []
    for i in range(1, abs(x)+1):
        if x%i == 0:
            factors.append(i)
    return factors

def gcd(x, y):
    a = abs(x)
    b = abs(y)
    while b != 0:
        a, b = b, a%b
    return a
    

print("""Copyright \u00a9 2016 Michael Wood


Enter a list of the coefficients separated by commas.
The last number entered will be treated as the constant term.
Use a minus sign for subtraction of the coefficient.
Ex.\tFor:\tf(x) = x\u2074 - 5x\u00b3 + 5x\u00b2 + 17x - 42
\tType:\t1, -5, 5, 17, -42

Use the zeroes function with your arguments to find the factors
of the polynomial.
Ex.\t zeroes(1, -5, 5, 17, -42)

""")

def zeroes(*args):
    a = list(args) #List of coefficients
    for i in range(len(a)):
        a[i] = str(a[i]) #Turn each item into type str
    b = copy.deepcopy(a) #Deepcopy of the coefficients

    #Use a for loop to create the function as a string with variable 'x'
    for i in range(len(a)):
        if len(a)-i-1 > 1:
            a[i] += "*x**" + str(len(a)-i-1)
        elif len(a)-i-1 == 1:
            a[i] += "*x"

    #Join the parts of the equation together to form a single string
    eqn = a[0]
    for i in range(1, len(a)):
        if a[i][0] != "-":
            eqn += "+" + a[i]
        else:
            eqn += a[i]

    #The equation as a function
    def f(x):
        return eval(eqn)

    #Formatting and printing
    print("f(x) = " + a[0], end="")
    for i in range(1, len(a)):
        if a[i][0] != "-":
            print(" + " + a[i], end="")
        else:
            print(" - " + a[i][1:], end="")
    print("\n"*2)

    fractions = []
    possibles = []
    garbage = []
    leadfactors = factors(int(b[0]))
    constantfactors = factors(int(b[-1]))

    #Use the remainder theorem to find linear factors of f(x)
    for m in constantfactors:
        for n in leadfactors:
            if f(m/n) == 0:
                fractions.append([m, n])

            #A value was detected, but the binary fraction caused the value to not
                #precisely equal zero
            elif (-1/2**40) <= f(m/n) <= (1/2**40):
                possibles.append([m, n])

            if f(-m/n) == 0:
                fractions.append([-m, n])
            elif (-1/2**40) <= f(-m/n) <= (1/2**40):
                possibles.append([-m, n])

    #Removing the factors which are not in lowest terms (in fractions and garbage)
    for i in fractions:
        if gcd(i[0], i[1]) != 1:
            garbage.append(i)
    for i in garbage:
        fractions.remove(i)
    garbage = [] #Hardcode the clearing of garbage array
    for i in possibles:
        if gcd(i[0], i[1]) != 1:
            garbage.append(i)
    for i in garbage:
        possibles.remove(i)

    #Printing the results to the screen, with formatting
    if len(fractions) == 0 and len(possibles) == 0:
        print("I was confused when I saw your function. \
Try again when I am updated")
    else:
        for i in fractions:
            if i[1] == 1:
                if i[0] > 0:
                    print("x - " + str(i[0]) + " is a factor of f(x)")
                    print("f(" + str(i[0]) + ") = 0")
                elif i[0] < 0:
                    print("x + " + str(abs(i[0])) + " is a factor of f(x)")
                    print("f(" + str(i[0]) + ") = 0")               
                else:
                    print("x")
                    print("f(0) = 0")
            else:
                if i[0] > 0:
                    print(str(i[1]) + "x - " + str(i[0]) + " is a factor of f(x)")
                    print("f(" + str(i[0]) + "/" + str(i[1]) + ") = 0")               
                elif i[0] < 0:
                    print(str(i[1]) + "x + " + str(abs(i[0])) + " is a factor of f(x)")
                    print("f(" + str(i[0]) + "/" + str(i[1]) + ") = 0")
            print()

        if len(possibles) > 0:   
            print("The following are possible factors of f(x),\n\
They must be confirmed. This is due to using IEEE-754:")
            print("~"*54 + "\n")
            for i in possibles:
                if i[1] == 1:
                    if i[0] > 0:
                        print("x - " + str(i[0]) + " could be a factor of f(x)")
                        print("f(" + str(i[0]) + ") = 0")
                    elif i[0] < 0:
                        print("x + " + str(abs(i[0])) + " could be a factor of f(x)")
                        print("f(" + str(i[0]) + ") = 0")               
                    else:
                        print("x")
                        print("f(0) = 0")
                else:
                    if i[0] > 0:
                        print(str(i[1]) + "x - " + str(i[0]) + " could be a factor of f(x)")
                        print("f(" + str(i[0]) + "/" + str(i[1]) + ") = 0")               
                    elif i[0] < 0:
                        print(str(i[1]) + "x + " + str(abs(i[0])) + " could be a factor of f(x)")
                        print("f(" + str(i[0]) + "/" + str(i[1]) + ") = 0")
        print("\n" + "-"*54 + "\n")

