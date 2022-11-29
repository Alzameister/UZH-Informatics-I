#You are completely free to change this variables to check your algorithm.
from cmath import sqrt
from math import ceil, floor, isqrt


num1 = 66
num2 = 308

def divisor_of_Number(number1,number2):
    divisors_num1 = [1]
    divisors_num2 = [1]

    for i in range(2, isqrt(number1)+1):
            if number1 % i == 0:
                divisors_num1.append(i)
                divisors_num1.append(int(number1/i))
    divisors_num1.append(number1)
    
    for i in range(2, isqrt(number2)+1):
            if number2 % i == 0:
                divisors_num2.append(i)
                divisors_num2.append(int(number2/i))
    divisors_num2.append(number2)
    
    divisors_num1.sort()
    divisors_num2.sort()
    
    return divisors_num1, divisors_num2
#Function to check whether two numbers are friendly pairs or not.
def isFriendlyPair(num1,num2):
    #You need to complete this function.
    #You need to return a boolean variable . If num1 and num2 are friendly pairs return True. 
    # If they are not return False. 
    # The numbers must be valid according to description before determining friendly parity situations. 
    # Return "Invalid" if they are not valid.
    #if num1 != int or num2 != int or num1 == num2:
    #    return False

    divisors = divisor_of_Number(num1,num2)
    print(divisors)
    divisors1 = divisors[0]
    divisors2 = divisors[1]
    added_divisors1 = 0
    added_divisors2 = 0


    #Calculate abundancy
    for number in divisors1:
        added_divisors1 += number
    for number in divisors2:
        added_divisors2 += number

    abundancy1 = added_divisors1 / num1
    abundancy2 = added_divisors2 / num2
    
    if abundancy1 == abundancy2:
        return True
    else:
        return False

#This line prints your method's return so that you can check your output.
print(isFriendlyPair(num1,num2))
#print(divisor_of_Number(num1,num2))