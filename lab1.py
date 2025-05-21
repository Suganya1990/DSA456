#Function 1
def wins_rock_scissors_paper(plGuess, opGuess):
    #converts string into number
    p = convertOption(plGuess)
    o = convertOption(opGuess)

    #compares numbers to determine winner 1 = rock | 2 = paper | 3 = scissors | -1 any other value
    if ( p == o   or p ==-1 or o ==-1 ):
        return False
    if(p ==1 and o ==3 ) or (p==2 and o ==1 ) or (p==3 and o ==2 ):
        return True
    elif(p==1 and o == 2) or (p==2 and o==3) or (p==3 and o ==1 ):
        return False


def convertOption(option):
    match(option.lower()):
        case 'rock':
            return 1
        case 'paper':
            return 2
        case 'scissors':
            return 3
        case _:
            return -1

# print ('Test 1 P1:"Rock" P2:"Rock" : ', wins_rock_scissors_paper('Rock', 'rock'),  "|", 'passed' if wins_rock_scissors_paper('Rock', 'rock')==False else 'Failed')#False
# print ('Test 2 P1:"Rock" P2:"Paper" : ', wins_rock_scissors_paper('Rock', 'Paper'),  "|", 'passed' if wins_rock_scissors_paper('Rock', 'Paper')==False else 'Failed')   #False
# print ('Test 3 P1:"Rock" P2:"Scissors" : ', wins_rock_scissors_paper('Rock', 'scissors'),"|",  'passed' if wins_rock_scissors_paper('Rock', 'scissors')==True else 'Failed ') #True
# print ('Test 4 P1:"Paper" P2:"PAPer" : ',wins_rock_scissors_paper('Paper', 'PAPer'), "|", 'passed' if wins_rock_scissors_paper('Paper', 'PAPer')==False else 'Failed')#False
# print ('Test 5 P1:"Paper" P2:"Rock" : ',wins_rock_scissors_paper('Paper', 'Rock'), "|", 'passed' if wins_rock_scissors_paper('Paper', 'Rock')==True else 'Failed') #True
# print ('Test 6 P1:"Paper" P2:"Scissors" : ',  wins_rock_scissors_paper('Paper', 'Scissors'), "|",  'passed' if  wins_rock_scissors_paper('Paper', 'Scissors')==False else 'Failed' ) #False
# print ('Test 7 P1:"Scissors" P2:"Scissors" : ',  wins_rock_scissors_paper('Scissors', 'Scissors'),  "|", 'passed' if wins_rock_scissors_paper('Scissors', 'Scissors')==False else 'Failed')#False
# print ('Test 8 P1:"Scissors" P2:"Paper" : ',  wins_rock_scissors_paper('Scissors', 'Paper'),  "|", 'passed' if  wins_rock_scissors_paper('Scissors', 'Paper')==True else 'Failed') #True
# print ('Test 9 P1:"Scissors" P2:"Rock" : ', wins_rock_scissors_paper('Scissors', 'Rock'), "|",  'passed' if wins_rock_scissors_paper('Scissors', 'Rock')==False else 'Failed') #False
# print ('Test 10 P1:"Scissors" P2:"Rock" : ',wins_rock_scissors_paper('sdfsd', 'Rocdsdsk'), "|",   'passed' if wins_rock_scissors_paper('sdfsd', 'Rocdsdsk')==False else 'Failed') #False



#************************************************#

# #Function 2 
# This function passes a non-negative integer, which we will call n in this description. the function returns n! (pronounced n factorial). n! = n * (n-1) * (n-2)... * 1 Thus, 3! = 3 * 2 * 1. Note that 0! is 1 by definition.

def factorial(num):
    i = num-1
    factorialValue= num  
    if(num < 0):
        return 
    if(num == 0 ):
        return 1
    else:
        while (i > 0 and i < num   ):
            factorialValue = factorialValue*i 
            i = i-1
    print(factorialValue)
    return factorialValue



# factorial(5)
# factorial(6)
# factorial(7)
# factorial(8)
# factorial(9)
# factorial(20)






#************************************************#

#Function 3 

# def Fibonacci(num):
#     n = 0
#     numArray = []; 
#     fibonaciiVal= 0  
#     if(num < 0):
#         return 
#     if(num == 0 ):
#         return 0
#     else:
#         while (n >= 0 and n < num   ):
#             numArray.push()
#             n=n+1


def Fibonacci(num):
    for n in range(num):
        total = fibRecursion(n)
        if n == num-1:
            print(total)
            
     


def fibRecursion(n):
    if n <= 1:
        return n
    else:
        return(fibRecursion(n-1)+ fibRecursion(n-2))




Fibonacci(5)
Fibonacci(10)
Fibonacci(35)
#Fibonacci(100)






#************************************************#

#Function 4cd 