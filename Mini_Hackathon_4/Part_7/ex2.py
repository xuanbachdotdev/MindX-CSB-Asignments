skills = [{'Name': "Tackle", 'Minimum level': 1, 'Damage': 5, 'Hit rate': 0.3}, {'Name': "Quick attack", 'Minimum level': 2,
                                                                        'Damage': 3, 'Hit rate': 0.5}, {'Name': "Strong kick", 'Minimum level': 4, 'Damage': 9, 'Hit rate': 0.2}]


for index, el in enumerate(skills):
    print("Skill %d:" % (index + 1), skills[index]['Name'])