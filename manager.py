class Manager:
    def __init__(self, id, company,bonus_potential):
        self.id = id
        self.company = company
        self.bonus_potential = bonus_potential
        self.x = -1
        self.y = -1

    def __str__(self):
        return f"Project Manager's id: {self.id} company is: {self.company} and bonus potential is: {self.bonus_potential}"