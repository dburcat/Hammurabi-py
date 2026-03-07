"""
Hammurabi - A classic resource management game.
Rule the kingdom of Hammurabi for 10 years and maximize the welfare of your citizens.
"""

import random


class Hammurabi:
    def __init__(self):
        # Initial state
        self.year = 1
        self.bushels = 1000
        self.acres = 1000
        self.population = 100
        self.harvested_bushels_per_acre = 0
        self.rats_ate_bushels = 0
        self.plague_deaths = 0
        
    def display_status(self):
        """Display current game status."""
        print(f"\n--- Year {self.year} ---")
        print(f"Acres owned: {self.acres}")
        print(f"Bushels in storage: {self.bushels}")
        print(f"Population: {self.population}")
        if self.plague_deaths > 0:
            print(f"Plague deaths this year: {self.plague_deaths}")
        if self.rats_ate_bushels > 0:
            print(f"Rats ate {self.rats_ate_bushels} bushels")
        
    def get_land_to_buy(self):
        """Get amount of land to buy."""
        price = self.get_land_price()
        while True:
            try:
                acres = int(input(f"How many acres will you buy (price: {price} bushels/acre)? "))
                cost = acres * price
                if acres < 0:
                    print("You cannot buy negative acres!")
                    continue
                if cost > self.bushels:
                    print(f"You only have {self.bushels} bushels!")
                    continue
                return acres
            except ValueError:
                print("Please enter a valid number.")
    
    def get_land_to_sell(self):
        """Get amount of land to sell."""
        price = self.get_land_price()
        while True:
            try:
                acres = int(input(f"How many acres will you sell (price: {price} bushels/acre)? "))
                if acres < 0:
                    print("You cannot sell negative acres!")
                    continue
                if acres > self.acres:
                    print(f"You only have {self.acres} acres!")
                    continue
                return acres
            except ValueError:
                print("Please enter a valid number.")
    
    def get_bushels_to_feed(self):
        """Get amount of bushels to feed the population."""
        while True:
            try:
                bushels = int(input("How many bushels will you feed your people? "))
                if bushels < 0:
                    print("You cannot feed negative bushels!")
                    continue
                if bushels > self.bushels:
                    print(f"You only have {self.bushels} bushels!")
                    continue
                return bushels
            except ValueError:
                print("Please enter a valid number.")
    
    def get_acres_to_plant(self):
        """Get amount of acres to plant."""
        max_plantable = min(self.acres, self.bushels)
        while True:
            try:
                acres = int(input(f"How many acres will you plant (max: {max_plantable})? "))
                if acres < 0:
                    print("You cannot plant negative acres!")
                    continue
                if acres > self.acres:
                    print(f"You only have {self.acres} acres!")
                    continue
                if acres > self.bushels:
                    print(f"You only have {self.bushels} bushels for seeds!")
                    continue
                if acres * self.population < 1:
                    print("You need people to plant!")
                    continue
                return acres
            except ValueError:
                print("Please enter a valid number.")
    
    @staticmethod
    def get_land_price():
        """Get random land price (17-23 bushels per acre)."""
        return random.randint(17, 23)
    
    def execute_buy_land(self, acres):
        """Execute land purchase."""
        price = self.get_land_price()
        cost = acres * price
        self.bushels -= cost
        self.acres += acres
        print(f"You bought {acres} acres for {cost} bushels")
    
    def execute_sell_land(self, acres):
        """Execute land sale."""
        price = self.get_land_price()
        revenue = acres * price
        self.bushels += revenue
        self.acres -= acres
        print(f"You sold {acres} acres for {revenue} bushels")
    
    def execute_feed_people(self, bushels):
        """Execute feeding the people."""
        self.bushels -= bushels
        # 1 bushel feeds 1 person
        
    def execute_plant(self, acres):
        """Execute planting crops."""
        self.bushels -= acres
        self.harvested_bushels_per_acre = random.randint(1, 5)
        harvested = acres * self.harvested_bushels_per_acre
        self.bushels += harvested
        print(f"You planted {acres} acres. Harvest: {self.harvested_bushels_per_acre} bushels/acre = {harvested} total")
    
    def random_events(self, bushels_fed):
        """Handle random events like plague and rats."""
        # Plague (10% chance)
        if random.random() < 0.15:
            self.plague_deaths = self.population // 2
            self.population -= self.plague_deaths
            print("A plague struck! Half your population died!")
        
        # Rats (10% chance)
        if random.random() < 0.10:
            self.rats_ate_bushels = self.bushels // (random.randint(1, 4))
            self.bushels -= self.rats_ate_bushels
            print("Rats invaded the storage!")
    
    def calculate_population_change(self, bushels_fed):
        """Calculate population change based on food and acres."""
        # People need food
        fed_people = bushels_fed
        
        # Deaths from starvation
        starvation_deaths = max(0, self.population - fed_people)
        self.population -= starvation_deaths
        
        if starvation_deaths > 0:
            print(f"{starvation_deaths} people starved!")
        
        # Births (max 10% of population per year, based on acres and food)
        birth_rate = min(10, (self.acres // 100) + (bushels_fed // 100))
        births = (self.population * birth_rate) // 100
        self.population += births
        
        if births > 0:
            print(f"{births} people were born!")
    
    def play_turn(self):
        """Execute one turn of the game."""
        self.display_status()
        
        print("\n========== LAND MARKET ==========")
        print("(Buy or sell land)")
        
        # Land transactions
        choice = input("Buy (b) or Sell (s) or Skip (n)? ").lower()
        if choice == 'b':
            acres_to_buy = self.get_land_to_buy()
            if acres_to_buy > 0:
                self.execute_buy_land(acres_to_buy)
        elif choice == 's':
            acres_to_sell = self.get_land_to_sell()
            if acres_to_sell > 0:
                self.execute_sell_land(acres_to_sell)
        
        print("\n========== FEEDING ==========")
        bushels_to_feed = self.get_bushels_to_feed()
        self.execute_feed_people(bushels_to_feed)
        
        print("\n========== PLANTING ==========")
        acres_to_plant = self.get_acres_to_plant()
        self.execute_plant(acres_to_plant)
        
        print("\n========== EVENTS ==========")
        self.random_events(bushels_to_feed)
        
        print("\n========== POPULATION ==========")
        self.calculate_population_change(bushels_to_feed)
        
        self.year += 1
    
    def final_score(self):
        """Calculate final score."""
        score = (self.acres // 2) + (self.bushels // 5 * 3) + (self.population * 4)
        return score
    
    def display_final_results(self):
        """Display final game results."""
        print("\n" + "="*40)
        print("GAME OVER - Year 10 Complete!")
        print("="*40)
        print(f"Final Acres: {self.acres}")
        print(f"Final Bushels: {self.bushels}")
        print(f"Final Population: {self.population}")
        print(f"Final Score: {self.final_score()}")
        print("="*40)
    
    def run(self):
        """Main game loop."""
        print("Welcome to Hammurabi!")
        print("You will rule for 10 years.\n")
        
        while self.year <= 10:
            self.play_turn()
            if self.population <= 0:
                print("Your civilization has ended!")
                break
        
        if self.year > 10:
            self.display_final_results()


def main():
    game = Hammurabi()
    game.run()


if __name__ == "__main__":
    main()
