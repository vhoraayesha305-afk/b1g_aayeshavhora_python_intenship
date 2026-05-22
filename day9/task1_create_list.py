numbers=[]

print("please enter 5 numbers:")

for i in range(1,6):
   num =int(input(f"enter number {i}:"))
   numbers.append(num)
   print("_"* 30)

print(f"Your list of numbers: {numbers}")
