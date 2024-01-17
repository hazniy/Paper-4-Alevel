#overloading
class greeting:
    def hello(self, firstname = None, lastname = None):
        if firstname and lastname is not None:
            print ("Hello", firstname, lastname)
        elif lastname is None:
            print ("Hello", firstname)
        else:
            print("Hello")
myGreeting = greeting()
myGreeting.hello()
myGreeting.hello("Christopher")
myGreeting.hello("Najwa", "Farhan")
