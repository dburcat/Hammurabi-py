import random

class Hammurabi:
    def __init__(self):
        self.rand = random.Random()
        self.pop = 100
        self.acres = 1000
        self.bushels = 2800
        self.land_cost = 19
        self.year = 1
        self.starved = 0
        self.died = 0
        self.immigrants = 0
        self.harvest = 0
        self.harvest_rate = 0
        self.rats = 0

    def main(self):
        self.playGame()

    def playGame(self):
        print("\033c\033[92mWelcome to Hammurabi!\033[0m")
        print("Congratulations, you are the newest ruler of ancient Sumer, elected for a ten year term of office. \nYour duties are to dispense food, direct farming, and buy and sell land as needed to support your people. \nWatch out for rat infestiations and the plague! \nGrain is the general currency, measured in bushels. The following will help you in your decisions:")
        print("Each person needs at least 20 bushels of grain per year to survive. \nEach person can farm at most 10 acres of land. \nIt takes 2 bushels of grain to farm an acre of land. \nThe market price for land fluctuates yearly.")
        print("Rule wisely and you will be showered with appreciation at the end of your term. Rule poorly and you will be kicked out of office!")
        begin = input("\nAre you ready to begin? (y/n) ")
        if begin.lower() != "y":
            print("\033c\033[91mThou are not ready. Begone foul beast!\033[0m")
            exit()
        self.printSummary()
        # declare local variables here: grain, population, etc.
        # statements go after the declarations
        return 0

    # other methods go here

    def askHowManyAcresToBuy(self):
        # ask the user how many acres to buy
        return 0
    
    def askHowManyAcresToSell(self):
        # ask the user how many acres to sell
        return 0
    
    def askHowManyBushelsToFeedPeople(self):
        # ask the user how many bushels to feed the people
        return 0
    
    def askHowManyAcresToPlant(self):
        # ask the user how many acres to plant with seed
        return 0
    
    def plagueDeaths(self):
        # return the number of people who die in a plague
        return 0
    
    def starvationDeaths(self):
        # return the number of people who starve to death
        return 0
    
    def uprising(self):
        # return True if there is an uprising, False otherwise
        return False
    
    def immigrants(self):
        # return the number of people who immigrate to the city
        return 0
    
    def harvest(self):
        # return the number of bushels harvested per acre
        return 0
    
    def grainEatenByRats(self):
        # return the number of bushels eaten by rats
        return 0
    
    def newCostOfLand(self):
        # return the new cost of land
        return 0

    def printSummary(self):
        # print a summary of the current year
        print("\033cO great Hammurabi!")
        print(f"You are in year {self.year} of your ten year rule.")
        print(f"In the previous year {self.starved} people starved to death.")
        print(f"In the previous year {self.immigrants} people entered the kingdom.")
        print(f"The population is now {self.pop}.")
        print(f"We harvested {self.harvest} bushels at a rate of {self.harvest_rate} bushels per acre.")
        print(f"Rats destroyed {self.rats} bushels, leaving {self.bushels} bushels in storage.")
        print(f"The city owns {self.acres} acres of land.")
        print(f"Land is currently worth {self.land_cost} bushels per acre.")
        return
    
    def finalSummary(self):
        # print a final summary of the game
        return 0

if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()
