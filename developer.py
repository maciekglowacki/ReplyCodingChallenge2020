class Developer:
    
    def __init__(self,company,bonus_potential,skills_count,skills):
        self.company = company
        self.bonus_potential = bonus_potential
        self.skills_count = skills_count
        self.skills = skills 
        self.x = 0
        self.y = 0
        
    def __str__(self):
        return f"Developer's company: {self.company}, Bonus: {self.bonus_potential}, skills count: {self.skills_count}, skills: {self.skills}"