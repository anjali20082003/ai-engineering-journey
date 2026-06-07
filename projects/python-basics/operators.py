

# --- USER INPUT ---
name = input("Apna naam batao: ")
age = int(input("Apni age batao: "))
city = input("Apna sheher batao: ")

# --- F-STRING OUTPUT ---
print(f"\nHello {name}!")
print(f"Tum {city} mein rehte ho.")
print(f"Tumhari age {age} hai.")
print(f"10 saal baad age hogi: {age + 10}")

# --- ARITHMETIC OPERATORS ---
print("\n--- Arithmetic Operators ---")

a = 10
b = 3
print(f"{a} + {b} = {a+b}")
print(f"{a} -{b} ={a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} % {b} = {a%b}")
print(f"{a} ** {b} = {a**b}")



# --- COMPARISON OPERATORS ---
print("\n----comparison operators----")
x = 50 
y = 30 
print(f"{x} == {y} : {x == y}")
print(f"{x} != {y} : {x != y}")
print(f"{x} > {y} : {x > y}")
print(f"{x} < {y} : {x < y}")
print(f"{x} >= {y} : {x >= y}")
print(f"{x} <= {y} : {x <= y}")     


# --- LOGICAL OPERATORS ---
print("\n----logical operators----")
is_raining = True
is_cold = False
print(f"Is it raining and cold? {is_raining and is_cold}")
print(f"Is it raining or cold? {is_raining or is_cold}")    
print(f"Is it not raining? {not is_raining}")

# --- ASSIGNMENT OPERATORS ---

print("\n--- ASSIGNMENT OPERATORS ---\n")
score = 500
print(f"Score: {score}")
score += 100
print(f" After Score: {score}")
score -= 50
print(f" now score: {score}")
score *= 3
print(f" now score: {score}")
score /= 2
print(f" now score: {score}")
score **= 2
print(f" now score: {score}")
score //= 10
print(f" now score: {score}")
score %= 3
print(f" now score: {score}")

