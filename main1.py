class Member:
    not_allowed_names = ['Hell','Sheit','Baloot']
    users_num = 0

    @classmethod
    def show_users_count(cls):
        print( f"We Have {cls.users_num} Users In Our System." )

    @staticmethod
    def Say_hello():
        print("Hello From Static Method")

    def __init__(self, first_name, middle_name, last_name , gender):
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender
        Member.users_num +=1

    def full_name(self):
        if self.fname in Member.not_allowed_names:
            raise ValueError('Name is Not Allowed')
        
        else:
            return f"{self.fname} {self.mname} {self.lname}"
    
    
    def name_with_title(self):
        if self.gender == 'Male':
            return f"Hello Mr {self.fname} "
        elif self.gender == 'Female':
            return f"Hello Miss {self.fname}"
        else:
            return f"Hello {self.fname}"
        
    def get_all_info(self):
        return f"{self.name_with_title()} , Your Full Name Is: {self.full_name()}"


    def delete_user(self):
        Member.users_num -= 1
        return f"user {self.fname} Deleted."





print(Member.users_num)

member_one = Member('ahmed','samir','awed','Male')
member_Two = Member('mona','Ali','Mahmoud', 'Female' )
member_Three = Member('Hell','abas','yy','dd')


print(Member.users_num)

print(member_one.full_name())
print(member_one.name_with_title())

print('\n','='*50,'\n')

print(member_Two.full_name())
print(member_Two.name_with_title())

print('\n','='*50,'\n')

print(member_one.get_all_info())

print('\n','='*50,'\n')

print(member_Two.get_all_info())

# print('\n','='*50,'\n')

# print(member_Three.get_all_info())


print('\n','='*50,'\n')

print(member_Three.delete_user())

print(Member.users_num)

print('\n','='*50,'\n')

Member.show_users_count()
Member.Say_hello()