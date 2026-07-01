print("For loop:")
for i in range(1,6):
    print(f"Number: {i} ")


print('\n--Loop on list--')
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
for fruit in fruits:
    print(fruit)


print("\n---Range ")
print("range(5):", list(range(5)))
print("range(2,5):", list(range(2,5)))
print("range(2,10,3):", list(range(2,10,3)))
print("range(10,2,-2):", list(range(10,2,-2)))


print("\n---while loop")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

print("\n---break")
for i in range(1,8):
    if i == 3:
        print(f" Loop break at Number: {i}")
        break
    print(f"Number: {i}")


print("\n---continue")
for i in range (1,11):
    if i % 2 == 0:
        continue
    print(f"Number: {i}")


print("\n--nested loop---")
for i in range (1,4):
    for j in range(1,4):
        print(f"{i}*{j} = {i*j}")

    

print("\n---sum 1 to 10 ---")
total = 0
for i in range (1,11):
    print(f"\n Iteration: {i}")
    print(f"Current total: {total}") 
    print(f"Adding {i} to total")
    total += i
    print(f"New Total = {total}")


print("\n---AI Training Simulation----")
epochs = 5
accuracy = 60.0
for epoch in range (1, epochs + 1):
    accuracy += 8
    print(f"Epoch: {epoch}/{epochs}, Accuracy: {accuracy}%")
print("Training Complete!")
