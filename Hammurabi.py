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
        self.newpop = 0
        self.harv = 0
        self.harvest_rate = 0
        self.rats = 0
        self.bushels_to_feed = 0
        self.revolt = False
        self.begin = True

    def main(self):
        self.intro()
        self.playGame()

    def playGame(self):
        self.printSummary()
        self.run_game_logic()
        if not self.revolt:
            self.begin = False
            while self.year <= 9 and not self.revolt:
                self.year += 1
                self.printSummary()
                self.run_game_logic()
            self.finalSummary()
        else:
            print("\033c\033[91mYou are not fit to rule\033[0m")
        # declare local variables here: grain, population, etc.
        # statements go after the declarations
        self.ending = input("\nDo you want to play again? (y/n) ")
        if self.ending.lower() == "y":
            self.__init__()
            self.playGame()
        else:
            print("\033cThou rest in peace, great Hammurabi. May your legacy live on forever in the annals of history.\033[0m")
        return

    # other methods go here

    def intro(self):
        print("\033c\033[92mWelcome to Hammurabi!\033[0m")
        print("Congratulations, you are the newest ruler, elected for a ten year term of office. \nYour duties are to dispense food, direct farming, and buy and sell land as needed to support your people. \nWatch out for rat infestiations and the plague! \nGrain is the general currency, measured in bushels. The following will help you in your decisions:")
        print("Each person needs at least 20 bushels of grain per year to survive. \nEach person can farm at most 10 acres of land. \nIt takes 2 bushels of grain to farm an acre of land. \nThe market price for land fluctuates yearly.")
        print("Rule wisely and you will be showered with appreciation at the end of your term. Rule poorly and you will be kicked out of office!")
        begin = input("\nAre you ready to begin? (y/n) ")
        if begin.lower() != "y":
            print("\033c\033[91mThou are not ready. Begone foul beast!\033[0m")
            exit()
        return

    def run_game_logic(self):
        # run the game logic for one year
        self.askHowManyAcresToBuy()
        self.askHowManyAcresToSell()
        self.askHowManyBushelsToFeedPeople()
        self.starvationDeaths()
        if self.revolt:
            return
        self.askHowManyAcresToPlant()
        self.plagueDeaths()
        self.harvest()
        self.grainEatenByRats()
        self.popgrowth()
        self.newCostOfLand()
        return

    def askHowManyAcresToBuy(self):
        # ask the user how many acres to buy
        print(f"\nYou have {self.acres} acres of land. Land is currently worth {self.land_cost} bushels per acre.")
        try:
            acres_to_buy = int(input("How many acres of land do you wish to buy? "))
            if acres_to_buy < 0:
                print("A ruler does not buy negative acres! Try again.")
                self.askHowManyAcresToBuy()
            elif acres_to_buy * self.land_cost > self.bushels:
                print("You do not have enough bushels to buy that much land! Try again.")
                self.askHowManyAcresToBuy()
            else:
                self.acres += acres_to_buy
                self.bushels -= acres_to_buy * self.land_cost
        except ValueError:
            print("A ruler does not speak in gibberish! Try again.")
            self.askHowManyAcresToBuy()
        return
    
    def askHowManyAcresToSell(self):
        # ask the user how many acres to sell
        print(f"\nYou have now have {self.acres} acres of land.")
        try:
            acres_to_sell = int(input("How many acres of land do you wish to sell? "))
            if acres_to_sell < 0:
                print("A ruler does not sell negative acres! Try again.")
                self.askHowManyAcresToSell()
            elif acres_to_sell > self.acres:
                print("You do not have that many acres to sell! Try again.")
                self.askHowManyAcresToSell()
            else:
                self.acres -= acres_to_sell
                self.bushels += acres_to_sell * self.land_cost
        except ValueError:
            print("A ruler does not speak in gibberish! Try again.")
            self.askHowManyAcresToSell()
        return
    
    def askHowManyBushelsToFeedPeople(self):
        # ask the user how many bushels to feed the people
        print(f"\nYou currently have {self.bushels} bushels in storage. You need at least {self.pop * 20} bushels to feed your people.")
        try:
            self.bushels_to_feed = int(input("How many bushels of grain do you wish to feed your people? "))
            if self.bushels_to_feed < 0:
                print("A ruler does not feed negative bushels! Try again.")
                self.askHowManyBushelsToFeedPeople()
            elif self.bushels_to_feed > self.bushels:
                print("You do not have that many bushels to feed your people! Try again.")
                self.askHowManyBushelsToFeedPeople()
            else:
                self.bushels -= self.bushels_to_feed
        except ValueError:
            print("A ruler does not speak in gibberish! Try again.")
            self.askHowManyBushelsToFeedPeople()
        return
    
    def askHowManyAcresToPlant(self):
        # ask the user how many acres to plant with seed
        print(f"\nYou have {self.acres} acres of land available and {self.bushels} bushels left in storage.")
        print(f"You can plant at most {min(self.acres, self.bushels // 2)} acres of land with seed.")
        try:
            self.acres_to_plant = int(input("How many acres of land do you wish to plant with seed? "))
            if self.acres_to_plant < 0:
                print("A ruler does not plant negative acres! Try again.")
                self.askHowManyAcresToPlant()
            elif self.acres_to_plant > self.acres:
                print("You do not have that many acres to plant! Try again.")
                self.askHowManyAcresToPlant()
            elif self.acres_to_plant > self.bushels:
                print("You do not have enough bushels to plant that many acres! Try again.")
                self.askHowManyAcresToPlant()
            else:
                self.bushels -= self.acres_to_plant * 2
        except ValueError:
            print("A ruler does not speak in gibberish! Try again.")
            self.askHowManyAcresToPlant()
        return
    
    def plagueDeaths(self):
        # return the number of people who die in a plague
        if self.rand.random() < 0.15:
            self.died = self.pop // 3
            self.pop -= self.died
        return
    
    def starvationDeaths(self):
        # return the number of people who starve to death
        if self.bushels_to_feed < self.pop * 20:
            self.starved = self.pop - self.bushels_to_feed // 20
            self.uprising()
            if self.revolt:
                return
            self.pop -= self.starved
        else:
            self.starved = 0
        return
    
    def uprising(self):
        # return True if there is an uprising, False otherwise
        if self.starved > self.pop // 4:
            self.revolt = True
        return
    
    def popgrowth(self):
        # return the number of people who immigrate to the city
        if not self.revolt and self.starved == 0:
            self.newpop = (self.rand.randint(10, 20) * (self.acres + self.bushels_to_feed)) // (100 * self.pop) + 1
            self.pop += self.newpop
        return
    
    def harvest(self):
        # return the number of bushels harvested per acre
        self.harvest_rate = self.rand.randint(1, 6)
        self.harv = self.harvest_rate * self.acres_to_plant
        self.bushels += self.harv
        return
    
    def grainEatenByRats(self):
        # return the number of bushels eaten by rats
        if self.rand.random() < 0.4:
            self.rats = self.rand.randint(10, 30) * self.bushels // 100
            self.bushels -= self.rats
        return
    
    def newCostOfLand(self):
        # return the new cost of land
        self.land_cost = self.rand.randint(17, 23)
        return

    def printSummary(self):
        # print a summary of the current year
        if self.begin:
            print("\033cO great Hammurabi!")
            print(f"Your reign has just begun. You are in year {self.year} of your 10 year rule.")
            print(f"You have recruited {self.pop} people to your banner.")
            print(f"You now watch over {self.acres} acres of land")
            print(f"You have {self.bushels} bushels to your name.")
            print(f"Land is currently worth {self.land_cost} bushels per acre.")
            print(f"May you rule wisely or suffer the consequences!")
        else:
            print("\033cO great Hammurabi!")
            print(f"You are in year {self.year} of your 10 year rule.")
            if self.starved != 0:
                print(f"In the previous year {self.starved} people starved to death.")
            else:
                print(f"In the previous year your kingdom's population grew by {self.newpop}.")
            print(f"The population is now {self.pop}.")
            if self.died > 0:
                print(f"Unfortunately, {self.died} people died in the plague.")
            print(f"We harvested {self.harv} bushels at a rate of {self.harvest_rate} bushels per acre.")
            if self.rats > 0:
                print(f"Rats destroyed {self.rats} bushels, leaving {self.bushels} bushels in storage.")
            print(f"The city owns {self.acres} acres of land.")
            print(f"Land is currently worth {self.land_cost} bushels per acre.")
        return
    
    def finalSummary(self):
        # print a final summary of the game
        if self.revolt:
            print("\033c\033[91mGame Over\nThe people have had enough of your rule and have overthrown you! You are kicked out of office.\033[0m")
        else:
            print("\033c\033[92mGame Over\033[0m")
        print(f"Your reign has ended after {self.year} years.")
        print(f"Your final population is {self.pop}.")
        print(f"Your final land holdings are {self.acres} acres.")
        return

if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()
