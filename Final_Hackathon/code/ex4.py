import sys

print('== Welcome to MindX Restaurant ==')

many_dishes = []

while True:
    dish = input("\nPlease choose a dish: ")
    if dish in many_dishes:
        print("You chose this already.", end = "  ")
    else:
        print("Great choice!", end=" ")
        many_dishes.append(dish)
    break_condition = input("Anything else? (y/n): ")
    if break_condition == "y":
        continue
    if break_condition == "n":
        break
    if break_condition != "y" or break_condition != "n":
        sys.exit()


print("\nWell done! Your order:")
for dish in many_dishes:
    print("- %s" % dish)



