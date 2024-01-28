#ques 2 OOP
#(a)
class Balloon:
    def __init__(self, defitem, col):
        self.health = 100 #INTEGER
        self.colour = col #STRING
        self.defenceitem = defitem #STRING
#(b)
    def GetDefenceItem(self):
        return self.defenceitem
#(c)
    def ChangeHealth(self, num):
        self.health = self.health + num
#(d)
    def CheckHeath(self):
        if self.health <= 0:
            return True
        else:
            return False
#(e)
#main
defenceitem = input('enter defence item: ')
colour = input('enter a colour: ')
Balloon1 = Balloon(defenceitem,colour)

#(f)
def Defend(MyBalloon):
    strength = int(input('enter strength: '))
    MyBalloon.ChangeHealth(-strength)
    print('you defended with ', str(MyBalloon.GetDefenceItem()))
    if MyBalloon.CheckHealth() == True:
        print('defence failed')
    else:
        print('defence succeeded')
    return MyBalloon

#(g)
Balloon1 = Defend(Balloon1)
