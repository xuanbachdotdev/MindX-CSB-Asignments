import random

char = {"Name": "Light",
        "Age": 17,
        "Strength": 8,
        "Defense": 10,
        "HP": 100,
        "Backpack": ["Shield", "Bread Loaf"],
        "Gold": 100,
        "Level": 2
        }

skills = [{'Name': "Tackle", 'Minimum level': 1, 'Damage': 5, 'Hit rate': 0.3}, {'Name': "Quick attack", 'Minimum level': 2,
                                                                                 'Damage': 3, 'Hit rate': 0.5}, {'Name': "Strong kick", 'Minimum level': 4, 'Damage': 9, 'Hit rate': 0.2}]

for index, el in enumerate(skills):
    print("Skill %d:" % (index + 1), skills[index]['Name'])

selected_skill = int(input("Choose skill by number: "))


if 1 <= selected_skill <= len(skills):
    skill = skills[selected_skill - 1]
    min_level = skill['Minimum level']

    if char["Level"] >= min_level:
        print("You chose %s." % skill['Name'])
        if random.random() > skill['Hit rate']:
            print("Missed.")
        if random.random() < skill['Hit rate']:
            print("Damage: %d" % skill['Damage'])

    else:
        print("Cannot deploy. Required level", min_level)
else:
    print("Invalid skill selection.")
