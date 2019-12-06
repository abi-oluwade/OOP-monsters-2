class Monsters:
    def __init__(self, name, skill_list = []):
        self.name = name
        self.skills_list = skill_list

    def name(self):
        print(self.name() + " This is my name")
        return self.name

    def skill_list(self):
        return 'These are my skills!'

monster1 = Monsters('Dexter',['fast, hungry, tall'])

print(monster1.name)
print(monster1.skills_list)