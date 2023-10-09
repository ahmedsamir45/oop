class Skill:
    def __init__(self):

        self.skills = ["Html","Css",'Js']

    def __str__(self):
        return f'This is My Skills =>{self.skills} '

    def __len__(self):
        return len(self.skills)


profile = Skill()

print(profile)
print(len(profile))

profile.skills.append('PHP')
profile.skills.append('MYSQL')

print(len(profile))