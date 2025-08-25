a = int(input("Enter your age:"))
print("Your age is:", a)
# # Conditional operators
# # >,<,>=,<=,==,!=
# # print(a>18)
# # print(a<=18)
# # print(a==18)
# # print(a!=18)
if(a>18):
    print("You can drive")
    print("yes")
else:
    print("You cannot drive")
    print("no")
    print("yay!!")

applePrice = 170
budget = 200
if(budget - applePrice > 40 ):
    print("Alexa, add 1 kg Apples to the cart")
elif (budget - applePrice > 20 ):
    print("It,s ok you  can buy Apples")
else:
    print("Alexa, do not add Apples to the cart")

#another exercise I'm trying hehe

num = int(input("Enter the value of num: "))
if (num < 0):
    print("The number is negative")
elif (num == 0):
    print("The number is zero")
elif(num == 999):
    print("The number is special")
else:
    print("The number is positive")
    if (num % 2 == 0):
        print("The number is even")
    else:
        print("The number is odd")

print("I'm happy now")
























































