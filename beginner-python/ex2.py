#Excersice 2: Good Morning Sir
# Write a program that greets the user with greetings based on time

# timestamp = int(input("Enter the current time please "))
# print("The current time is", timestamp)

# if timestamp < 12:
#     print("Good Morning Sir")
# elif 12 <= timestamp <18:
#     print("Good Afternoon Sir")
# elif 18<= timestamp < 24:
#     print("Good Evening Sir")
# else:
#     print("Invalid time entered, please enter a valid time between 0 and 23")

# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = int(time.strftime('%H'))
# print(timestamp)
# timestamp = int(time.strftime('%M'))
# print(timestamp)
# timestamp = int(time.strftime('%S'))
# print(timestamp)

# if timestamp < 12:
#     print("Good Morning Sir")
# elif 12 <= timestamp < 18:
#     print("Good Afternoon Sir")
# elif 18 <= timestamp < 24:
#     print("Good Evening Sir")
# else:
#     print("Invalid time entered, please enter a valid time between 0 and 23")

import time

current_time = time.strftime('%H:%M:%S')
print("Current time:", current_time)

hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
second = int(time.strftime('%S'))

print("Hour:", hour)
print("Minute:", minute)
print("Second:", second)

if hour < 12:
    print("Good Morning Sir")
elif 12 <= hour < 18:
    print("Good Afternoon Sir")
elif 18 <= hour < 24:
    print("Good Evening Sir")
else:
    print("Invalid time entered, please enter a valid time between 0 and 23")


