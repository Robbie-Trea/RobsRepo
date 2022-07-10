class Engineer:
    def __init__(self,name,tpe,experience):
        self.name=name
        self.tpe = tpe
        self.experience = experience
        
E1 = Engineer("Robert","Mechanical",4)
E2 = Engineer("SomeGuy","Mining",1.5)

Fav_No = 42
MyName = "Robert Treasure"
print(MyName)

Str1 = E1.name+" "+E1.tpe+" "
print(Str1, E1.experience, "yrs experience")
Str2 = E2.name+" "+E2.tpe+" "
print(Str2, E2.experience, "yrs experience")

strLen = len(MyName)
MyNameRev = ""
while strLen > 0:
    strLen = strLen - 1
    MyNameRev += MyName[strLen]
    
print (MyNameRev)

input("Press Enter to Show my Favourite Number Squared")

Sq_F_No=Fav_No*Fav_No
for i in range(Sq_F_No+1):
    print(i)
