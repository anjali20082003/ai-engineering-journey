# --- Integer-----
age = 25
year = 2024
marks = 85
print("Age:", age)
print("Year:", year)
print("Marks:", marks)

#--- Float-----
height = 5.6
weight = 70.5
learning_rate = 0.01
print("Height:", height)
print("Weight:", weight)
print("Learning Rate:", learning_rate)

#--- String-----
name = "Anjali"
city = "Mumbai"
course = "AI Engineer" 
print("Name:", name)
print("City:", city)
print("Course:", course)

#--- Boolean-----
is_student = True
is_employed = False
has_git_hub_account = True
print("Is Student:", is_student)
print("Is Employed:", is_employed)
print("Has GitHub Account:", has_git_hub_account)   

#----none-----
favorite_color = None
print("Favorite Color:", favorite_color)

# ---type() check ----
print("Type of age:", type(age))
print("Type of height:", type(height)) 
print("Type of name:", type(name))
print("Type of is_student:", type(is_student))  
print("Type of favorite_color:", type(favorite_color))


# ----type conversion-----
age_text = str(age)  # Integer to String
print("Meri age hai :", age_text)

price ="299.99"
price_float = float(price)  # String to Float
print("Price:", price_float)
print("Price + Tax:", price_float + 20)  # Adding tax to price


MY_Name = "Anjali"
My_age = 23
city = "MUMBAI"
is_student = True
print("My Name is:", MY_Name)
print("My Age is:", My_age)     
print("I am a student:", is_student)

a = 5
b = 2.0
print(type(a + b))

print(int(9.9))


name = "Anjali"
age = 20
print("Hello " + str(name))
print(age + 5)


x = 10
y = "10"
print(x == int(y))

price = 599
discount = 0.10
print("Final price: " + str(price - (price * discount)))


name = "Anjali"
age = 20
city = "Mumbai"
print("My name is " + name + ", I am " + str(age) + " years old and I live in " + city + ".")   