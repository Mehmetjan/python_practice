class FirstClass: #  classess uppper case, module name with lower case
    # classesa re blueprint of specific objects,  we don't have specific value, we have attributes
    # attributes liek email, phone...value will be set when we create object,  but funtion will actually take these value as assign to object
    def __init__(self,email,phone,password,website):    #init is special funtion, with underscore __init__ also called Custructure, to use construct object, (self)-- means craete parameter, object of the class
        self.email=email
        self.phone=phone
        self.password = password
        self.website=website
    def change_password(self,newPass):
        self.password = newPass
    def changeEmail(self,newEmal):
        self.email=newEmal

    def get_info(self):
        print(f"email is: {self.email} \nphone: {self.phone}\nnewPass: {self.password}\nweb address: {self.website}")
#FirstClass("mett@gmail.com","2435354","sfjk45","www.slepy.com")   #  <-- calling class
user1 = FirstClass("mett@gmail.com","2435354","sfjk45","www.slepy.com")
user2 = FirstClass("jack@gmail.com","45657575","fghdg67652f","www.slepyjack.com")
print("-----------------------")
user1.get_info()
print("-----------------------")
user2.get_info()
