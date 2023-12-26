# num_char = len(input("What is your name: "))
# new_num = str(num_char)
# print(new_num)

a= str(123)
print(type(a))
print(6/3)
# exponent
print(2**2)
print(2**4) 

# PEMDASLR
# ()
# **
# */
# +-

print(3*3 + 3/3 -3)
print((3*3) + (3/3) -3)


print(round(8/3,2))
print(round(8/3))
print(8/3)
# shortcut of converting into integer round
print(8//3)

score = 0
score +=1
print(score)

score=0
height = 1.8
isWinning = True
# f-String

print(f"your score is {score} , your height is {height} ,your winning is {isWinning}")


print(6+4 /2 - (1*2))


# Excersie 1

two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
print(int(two_digit_number[0]) + int(two_digit_number[1]))

# Exercise  2

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

#print(type(height))
#print(type(height))
height_float = float(height)
weight_int = int(weight)
bmi = round(weight_int /height_float **2)
print(bmi)


# Exercise 2

age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

#print(type(age))
years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left." )
