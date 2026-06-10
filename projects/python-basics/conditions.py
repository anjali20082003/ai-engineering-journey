# --- BASIC IF ---
print("=== BASIC IF ===")
temparature = float(input("Enter your body temparature in Celsius: "))
if temparature > 37:
    print("You have a fever! You should see a doctor.")

# --- IF-ELSE ---
print("\n=== IF-ELSE ===")
age = int(input("How old are you? "))
if age >=18:
    print("You are an adult. You should be able to vote.")
else:
    print(f"Tum {18-age} saal baad vote kar sakte ho.")

# --- IF-ELIF-ELSE ---
print("\n=== IF-ELIF-ELSE ===")
marks = float(input("Enter your marks (0-100): "))
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter between 0 and 100.")
else:
    if marks >= 90:
        grade = "A"
        message = "Excellent!"
    elif marks >= 80:
        grade = "B"
        message = "Good job!"
    elif marks >= 70:
        grade = "C"
        message = "You passed."
    elif marks >= 60:
        grade = "D"
        message = "You are average."
    else:
        grade = "F"
        message = "You failed. Better luck next time."
    print(f"Your marks are {marks}, and your grade is {grade}. {message}")




# --- NESTED IF ---
print("\n=== NESTED IF ===")
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin":
    if password == "password123":
        print("Login successful! Welcome, admin.")
    else:
        print("Incorrect password. Access denied.")
else:
    print("Username not found. Access denied.")


#---Short Hand If---
print("\n=== SHORT HAND IF ===")
number = int(input("Enter a number: "))
if number % 2 == 0: print(f"{number} is an even number.")
else: print(f"{number} is an odd number.")


#--AI Eaample--
print("\n=== AI Spam detector===")
message = input("Enter a message: ")

if "free" in message.lower() or "win" in message.lower():
    print("spam detected.")
elif len(message) < 5:
    print("Message is too short.")
else:
    print("Message looks good.")


#--Percentage Calculator--
print("---Percentage Calculator---")
marks = int(input("Enter your marks: "))
total_marks = int(input("Enter total marks: "))
percentage = (marks/total_marks)*100
if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
else:
    print("Grade: F")

print(f"\nYour percentage is: {percentage}%")
print(f"Your grade is: {('A' if percentage >= 90 else 'B' if percentage >= 80 else 'C' if percentage >= 70 else 'D' if percentage >= 60 else 'F')}")
print("Thank you for using the Percentage Calculator!" \
"")


#--Simple Calculator--
print("\n-----Calculator-----\n")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print("Sum:", num1 + num2)
elif operation == "-":
    print("Difference:", num1 - num2)
elif operation == "*":
    print("Product:", num1 * num2)
elif operation == "/":
    print("Quotient:", num1 / num2)
else:
    print("Invalid operation")


#--Simple ATM--
print("/n---Simple ATM---/n")
balance = 5000
amount = int(input("Enter the amount "))
if amount <= balance:
   print ("dispensing cash")
else:   print ("insufficient balance")



#--Age Category Checker--
print("\n---Age category checker---\n")
age = int(input("Enter your age: "))
if age >= 0 and age <= 12:
    print("You are a child.")
elif age >= 13 and age <= 17:
    print("You are a teenager.")
elif age >= 18 and age <= 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")



#--Password Strength Checker--
print("/n-----Password strength checker----/n")
password = input("Enter your password: ")
if len(password) >= 8:
    print("Your password is strong.")
elif len(password) >= 5 and len(password) <= 7:
    print("Your password is medium.")
else:
    print("Your password is weak.")


#--FizzBuzz--
print("/n-----FizzBuzz----/n")
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)