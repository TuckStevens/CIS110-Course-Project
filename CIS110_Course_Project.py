# Greetings
print(f'Hello, there! I have an adventurous story about a girl and her family trying to survive in the distant future. It\'s an exciting tale.')
print(f'Before this tale begins, I need you to answer a few questions.')
print(f'Please press the enter key after typing your answer.')
input(f"\nPress the enter key to continue...")

playAgain = "yes"
while playAgain.lower() == "yes":

    # 5 questions
    characterName = input("\nWhat is your character's name:  ")
    while len(characterName) == 0:
        characterName = input(f"Your character needs a name! Please enter a name:  ")
    townName = input("What town do you want to live near:  ")
    while len(townName) == 0:
        townName = input(f"Please enter a town:  ")
    vegetableName = input("What is your favorite vegetable:  ")
    while len(vegetableName) == 0:
        vegetableName = input(f"Please enter a vegetable:  ")
    roadName = input("What road do you live on:  ")
    while len(roadName) == 0:
        roadName = input(f"Please enter a road name:  ")
    travelerName = input("What name would a traveler have:  ")
    while len(travelerName) == 0:
        travelerName = input(f"Please enter a name:  ")

    #Story begins
    print(f"\nLets begin...")
    print(f"\nOur story begins with {characterName} on {roadName}, walking back to their home where they live with their family  in the foothills of the mountain.")
    print(f"\n{characterName} spent the day in {townName} nearby bartering for food. Unfortunately they only managed to get a few seeds of {vegetableName} for their family garden.")
    print(f"\nThe worst of winter has passed and the weather is starting to warm but frost is still prevalent. Your family is running low on food and are getting desperate.")

    #Decision 1
    plantSeeds = input(f"\nShould {characterName} plant the {vegetableName} seeds even though there is a risk of frost killing the seedlings?  Type yes or no:  ")
    while plantSeeds.lower() not in ["yes", "no"]:
        plantSeeds = input("Please enter yes or no:  ")
    if plantSeeds == "yes":
        print(f"\n{characterName} plants the {vegetableName} seeds on the next sunny day hoping for the best.")
        print(f"\nA few days of warm weather have {characterName} feeling good about their decision...")
        print(f"\nThat night it gets colder then it has been in weeks causing the ground to frost and killing any {vegetableName} sprouts.")
        print(f"\n{characterName} hopes that by some miracle the sprouts survived the frost but weeks go by and nothing grows.")
        print(f"\nThe family tries to make their food last as long as possible and are barely surviving.")
    else:
        print(f"\n{characterName} waits till there is no chance of frost to plant the {vegetableName} seeds.")
        print(f"\nThey ration all the food they have left waiting for the sprouts to grow.")
        print(f"\nIn a few weeks time they are able to harvest {vegetableName}. Sustaining them with food and getting rid of any fear of starving. ")

    #Story
    print(f"\nAs the weather warms more travelers are passing through heading towards {townName}.")

    #Decision 2
    helpTraveler = input(f"\nOne day a traveler knocks at the families door, they introduce themselves as {travelerName}. They kindly ask for shelter before a storm passes through. Do you let {travelerName} stay or do you tell them no? Type yes or no:  ")
    while helpTraveler.lower() not in ["yes", "no"]:
        helpTraveler = input("Please enter yes or no:  ")
    if helpTraveler == "yes":
        print(f"\nYou invite {travelerName} inside and offer them some food. {travelerName} shares stories and shares that they are an avid hunter. They plan on settling near {townName}.")
        print(f"\nIn the morning the storm has passed and {travelerName} gets ready to set off. They thank you and your family for all the hospitality.")
        print(f"\nBefore leaving they promise to come back and visit with meat from their hunts.")
        print(f"\n{travelerName} sets off towards {townName} as you wave goodbye.")
    else:
        print(f"\n{travelerName} sets off towards town as it begins to storm.")
        print(f"\n{characterName} heads into town next week and discover {travelerName} has become a hunter there.")
        print(f"\n{travelerName} shares with others about how you turned them away and now you are unable to trade with most people in town.")

    #Alternate Endings
    if plantSeeds == "yes" and helpTraveler == "yes":
        print(f"\nAfter some hard times and little to no food, things start looking up for {characterName} and their family. {travelerName} returns with enough food for a feast.")
        print(f"\nThey eat until their bellies are full and thank {travelerName} for the food.")
        print(f"\n{characterName} and their family are able to start a bountiful garden so they can trade crops for resources in town. They also give plenty to {travelerName} everytime they visit.")
        print(f"\nLife is good as they set their worries of struggle behind.")
    elif plantSeeds == "no" and helpTraveler == "no":
        print(f"\n{characterName} and their family are able to sustain themselves with food from the garden.")
        print(f"\nHowever the only other food they manage to get is from foraging and the occasional animal they catch from traps around the home.")
        print(f"\nThey no longer go into town unless necessary as they are usually not looked upon kindly.")
        print(f"\nAs the years pass they are forgotten about and travelers only notice the house slowly falling into disrepair.")
    elif plantSeeds == "no" and helpTraveler == "yes":
        print(f"\n{characterName} and their family manage to grow and sustain enough food to pass the coming years.")
        print(f"\nTravelers come and go through the area. The family offers food to some for resources.")
        print(f"\nThe family is well know in {townName} for helpng others.")
    else:
        print(f"\n{characterName} and their family is unable to grow or forage for food.")
        print(f"\nThey begin to run out of food and start to starve.")
        print(f"\nNo one knows what happened to {characterName} and their family. Only that their home seems to have been abandoned.")
    print("\nThe End")

    playAgain = input(f"\nWould you like to play again? Enter yes or no:  ")
    while playAgain.lower() != "yes" and playAgain.lower() != "no":
        playAgain = input(f"Please type yes or no:  ")