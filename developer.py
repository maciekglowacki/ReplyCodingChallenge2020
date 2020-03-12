class Developer:

    def __init__(self, id, company, bonus_potential, skills_count, skills):
        self.id = id
        self.company = company
        self.bonus_potential = bonus_potential
        self.skills_count = skills_count
        self.skills = skills
        self.x = -1
        self.y = -1

    def __str__(self):
        return f"Developer's id: {self.id} company: {self.company}, Bonus: {self.bonus_potential}, skills count: {self.skills_count}, skills: {self.skills}"

    def __repr__(self):
        return self.__str__()