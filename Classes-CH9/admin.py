from users import User

class Admin(User):
    def __init__(self,first_name,last_name,age,email_address):

        super(Admin,self).__init__(first_name,last_name,age,email_address)
        self.privileges = Privileges()
    


class Privileges(object):
    def __init__(self):
        self.privilegess = ['can add post','can delete post','can lke post']
    def funcname(self):
        print self.privilegess