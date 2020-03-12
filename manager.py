class Manager:
    def __init__(self,company,bonus_potential):
        self.company = company
        self.bonus_potential = bonus_potential


    def __str__(self):
        return f"Project Manager's company is: {self.company} and bonus potential is: {self.bonus_potential}"