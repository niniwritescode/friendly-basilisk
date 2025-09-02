# def average(a=9, b=1):
#     print("The average is", (a + b) / 2)
def average(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
       sum = sum + i
    # print("Average is:", sum/len(numbers))
    # return 7
    return sum/len(numbers)

# average(4, 6)
# average(b=9)
# average(a=21)
c = average(5,7,6,1)
print(c)
# def name(fname, mname ="John", lname = "Whatson"):
#     print("Hello,", fname, mname, lname)

# name("Amy", "Louise")

def name(**name):
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname="Buchanan", lname = "Barnes", fname = "James")












