print("How many slices of pizza you have to share?")
pizzaSlices = int(input())
print("How many people are sharing the pizza?")
people  = int(input())

Slices = pizzaSlices // people

RemainingSlices = pizzaSlices % people

print(f"Each person will receive {Slices} Enjoy!")
print(f"There will be {RemainingSlices} remaining slices")