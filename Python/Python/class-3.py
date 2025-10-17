def loopOne():
    i = 1
    while i <= 10:
        print(i)
        i = i + 1

def loopTwo():
    i = 1
    while i <= 10:
        print("2 x ", i, "=",2 * i)
        i = i + 1


def loopThree():
    a = 0
    row = ""
    while(a < 10):
        row += "* "
        a += 1
    print(row)  



def loopFour():
    i = 5
    sum = 0
    while(i > 0):
        sum += i
        print(i)
        i -= 1
    print(sum)    
# loopFour()

def loopFive():
    i = 1
    while i <= 3:
        j = 1
        while j <= 3:
            print(i, j)
            j += 1
        i += 1
# loopFive()


def loopSix():
    i = 1
    while(i <= 5):
        row = ""
        j = 1
        while(j <= i):
            row += "i "
            j += 1
        print(row)
        i += 1
# loopSix()


def loopSeven():
    i = 1
    while i <= 5:
        row = ""
        j = 1
        while j <= i:
            row += str(i) + " "
            j += 1
        print(row)
        i += 1

loopSeven()

 
