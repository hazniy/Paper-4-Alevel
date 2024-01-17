#set only 
class Member() :
    def __init__(self):
        self.MemberName = ''
        self.MemberID = ''
        self.SubscriptionPaid = False
    def SetMemberName(self, n):
        self.MemberName = n
    def SetMemberID(self, i):
        self.MemberID = i
    def SetSubscriptionPaid(self, p):
        self.SubscriptioPaid = p

class JuniorMember(Member):
    def __init__(self):
        Member.__init__(self)
        self.DateOfBirth = ''
    def SetDateOfBirth(self, d):
        self.DateOfBirth = d

import datetime
NewMember = JuniorMember()
NewMember.SetMemberID('0999')
NewMember.SetMemberName('ali')
NewMember.SetSubscriptionPaid(False)
datetime.date(2001,11,12)
print(NewMember.MemberID)
print(NewMember.MemberName)
print(NewMember.SubscriptionPaid)
print(NewMember.DateOfBirth)
