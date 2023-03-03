# Greetings
print(f'Hello, there! I have an adventurous story about a girl and her family trying to survive in the distant future. It\'s an exciting tale.')
print(f'Before this tale begins, I need you to answer a few questions.')
print(f'Please press the enter key after typing your answer.')
input(f"\nPress the enter key to continue...")

# 5 questions
characterName = input("\nWhat is your character's name:  ")
townName = input("What town do you want to live near:  ")
vegetableName = input("What is your favorite vegetable:  ")
roadName = input("What road do you live on:  ")
travelerName = input("What name would a traveler have:  ")

#Story begins
print(f"\nLets begin...")
print(f"\nOur story begins with {characterName} on {roadName}, walking back to their home where they live with their family in the foothills of the mountain.")
print(f"\n{characterName} spent the day in {townName} nearby bartering for food. Unfortunately they only managed to get a few seeds of {vegetableName} for their family garden.")
print(f"\nThe worst of winter has passed and the weather is starting to warm but frost is still prevalent. Your family is running low on food and are getting desperate.")

#Decision 1
plantSeeds = input(f"\nShould {characterName} plant the {vegetableName} seeds even though there is a risk of frost killing the seedlings?  Type yes or no:  ")
if plantSeeds == "yes":
    print(f"\n{characterName} plants the {vegetableName} seeds on the next sunny day hoping for the best.")
    print(f"\nA few days of warm weather have {characterName} feeling good about their decision...")
    print(f"\nThat night it gets colder then it has been in weeks causing the ground to frost and killing any {vegetableName} sprouts.")
    print(f"\n{characterName} hopes that by some miracle the sprouts survived the frost but weeks go by and nothing grows.")
    print(f"\nThe family tries to make their food last as long as possible but eventually starve to death.")
else:
    print(f"\n{characterName} waits till there is no chance of frost to plant the {vegetableName} seeds.")
    print(f"\nThey ration all the food they have left waiting for the sprouts to grow.")
    print(f"\nIn a few weeks time they are able to harvest {vegetableName}. Sustaining them with food and getting rid of any fear of starving. ")