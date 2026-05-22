name=input("enter your name: ")
city=input("enter your city:")

formatted_name = name.strip().title()
formatted_city =city.strip().title()

massage =f"my name is {formatted_name} and i live in {formatted_city}"

print(massage)