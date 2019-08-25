#Consider an equation of form, Ax + B = Cx + D
def elemR(input_array, x):
    i=0 #loop counter
    length = len(input_array)
    while(i<length):
            y=input_array[i]
            p = y.split(x)
            input_array.extend(p)
            input_array.remove(input_array[i])
            length= length - 1
            i= i + 1
    
def xR(input_array1, input_array2):
    for elem in input_array1:
        if elem.endswith("x"):
            input_array2.append(elem)
            input_array1.remove(elem)

def ArraySum(input_array):
    i = 0
    S = 0
    length = len(input_array)
    while(i < length):
        S = S + input_array[i]
        i = i + 1
    return S

def Solve():
    Cdiff = SumRightC - SumLeftC
    Xdiff = SumLeftX - SumRightX
    Ans = Cdiff/Xdiff
    print(str(Xdiff) + "x = " + str(Cdiff))
    print(Ans)

Variables = []
RHS = []
LHS = []
RHS_x = []
LHS_x = []


z = input('Enter your function:')
Variables.extend(z.split("="))

LHS.append(Variables[0])
RHS.append(Variables[1])

elemR(RHS,"+")
elemR(LHS, "+")

RHS = [x.strip(' ') for x in RHS]
LHS = [x.strip(' ') for x in LHS]

xR(RHS, RHS_x)
xR(LHS, LHS_x)

RHS_x = [x.strip('x') for x in RHS_x]
LHS_x = [x.strip('x') for x in LHS_x]

RHS = [int(n) for n in RHS]
RHS_x = [int(n) for n in RHS_x]
LHS = [int(n) for n in LHS]
LHS_x = [int(n) for n in LHS_x]

SumRightC = ArraySum(RHS)
SumLeftC = ArraySum(LHS)
SumRightX = ArraySum(RHS_x)
SumLeftX = ArraySum(LHS_x)


Solve()
