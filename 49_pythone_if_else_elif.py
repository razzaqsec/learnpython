print("Bismillahir Rahmanir Rahim")


a=45
b=73
if a > b:
    print("a b er theke boro")
if a==b:
    print("a b 2 ta e shoman shoman")    
if a!=b:
    print("a b 2 ta shoman na.")    
if a<=b:
    print( "hobe ni")    
else:
    print("a b er theke boro na")

if a < b:
    print("b a er theke boro")




#  elif er akj korbo ekhon

# IF use korle shob run korbe zodi sothik hoy.   Elif use korle sudhu sothik 1st ektai run korbe .

# E X A M P L E -------------

a=100
b=80

if a<b:
    print("ami b er theke boro")

elif a<b:
    print("b a er theke boro")

elif a!=b:
    print("Kono ta e thik na ") 

elif a==b:
    print("2 Ta e shoman ")   


# elif holo ____-----____ If mane jeita prothom e boshbe .. 'ekhon if zodi bhul hoy.
#     tahole elif use korle elif er sothik 1st er tai sudhu run korbe .  '


# else ekbar e use kora jabe . but elif hajar hajar bar use kora zay.


" P Y T H O N       L O O P S "



# WHILE LOOPS 
# FOR LOOPS 

"W H I L E  LOOPS"

usha=0

while usha < 100:
    print("I try my best",usha )
    usha= usha + 1

" F O R   LOOPS "

fruits=["apple","banana","mango","cherry","talha","fatema","ayesha"]
for ox in fruits:
    if ox == "talha":
       break
    print(ox)

    # for loops e 
    "N o t e"
# ekhane "TAlha" likhar por "talha"  soho shob kichu break korbe. Sudhu TALHA er ager word gulo thakbe ,..



# 51 
# PYTHON Fuctions   :::

def usha(a,b):
    talha=a+b
    print(talha)
usha(3657,6723)
usha(28349,98) 
usha(100,900)   

"amra ekhane eksathe onekbar + zog er kaj korte parbo easily"

'eibar amra - biyog niye kaj korbo'

def simi(x,y):
    mimi=x-y
    print(mimi)
simi(5263,2221)
simi(1000,500)




###  B R E A K   &   continue

name = ["arazzaq","fahim","jowel","hanif","badsha","sohel","piyash","jamshed","shorif"]
for x in range(len(name)):
    if x==5:
        break
    print(x)


####       r e c u r s i o n ( rikashon )

def rio():
    print("usha")
    rio()

#rio()
'rio ta run korle 990+ "USHA" run korbe / er por errror dekhabe '


#    5    4     ==  Z I P function bangla.

# ex 1
list1=["rahim","abir","usha","amir"]
list2=["ctg","frankfruit","laksam","comilla"]

print(list(zip(list1,list2 )))

# ex  2 
momo=["usha","ayesha","fatema","talha"]
omom=["apple","samsung","huawei","mi"]

print(list(zip(momo,omom )))



# 55 -- Python Debugging 

i=0
while i < 14:
    print(i)
    i=i+1


# lambda funcations                  lambda funcations                    lambda funcations 
# 


#                                  54 Nomber


'ex uporer 81 number ;line theke neya eita . eita onek boro, amra ei ex shortcut e korbo nicher niyom e '
# def usha(a,b):
#     talha=a+b
#     print(talha)
# usha(3657,6723)
# usha(28349,98) 
# usha(100,900)   


'ex= 1 '
z = lambda a,b: a+b
print(z(455,45))
print(z(541,59))
print(z(4754768345,6345646548))


" amra ekhane shotcut e zog korlam. biyog er ta o same e hobe i hope "

" caile amra ekhane tottal 3/4 vabe o zog biyog gun vag korte parbo "


# ex 3 

x=lambda a,b,c,d: (a+b)/(c+d)
print(x(10,20,1,2))

'ex 2 '

f =lambda a,b,c,d: (a-b)+(c*d)
print(f(100,50,100,2))



#ex 4
def usha (a,b):
    alu= a+b
    print(alu)

k= lambda a,b: a+b
print(k(10,20))
 










# Array                  57 No Work Day

myArray= ["abbu","ammu","vaiya","bon","amoi"]
myArray[4]= "AMi"
print(myArray)

"ekahne name chgange korsi ei r ki array er kaj maybe "
  


# Python class & object         58 Number WORK

class Usha:
    name=   " "
    number= " "

a = Usha()
b=Usha()
c=Usha()
d=Usha()

a.name = "Abdur Razzaq"
b.name="Shuva"
c.name="Fahim"
d.number=+8801540511775

print(d.number)
print(a.name)
print(b.name)
print(c.name)


#ex 2 

class Rahma:
    brand=" "
    price= " "
    model=" "
    roll=""
    bf=""
    study=""

u= Rahma()
v= Rahma()
w= Rahma()
x= Rahma()
y= Rahma()
z= Rahma()

x.brand="Apple"
y.model="iPhone"
z.price="129999"
u.bf="Abdur Razzaq"
w.roll='320'
v.study= "10"


print(x.brand)
print(y.model)
print(z.price)

print(u.bf)
print(v.study)
print(w.roll)


#                    5  9   
# Inheritance --------------------- DALAL System
#  W O R K   D A Y   5 9 

# class baba():
#     car= "BMW"
#     taka= "200 crore"
#     home = "20 floor"

# class kaka(baba):
#     BrokenCar= " "
#     BrokenHome= " "

# dj= kaka()
# m= kaka()

# print(dj.car)
# print(m.home)
" 60 work day te kaj korar subidha te amra ei gula comment kore disi "

' ex 2 '

class fahim():
    Bike= "RTR 160"
    TAka = "20k Taka"
class usha(fahim):
    NoBike = ""
    TAkaNAii = ""

lol= usha()
olo= usha()

print(lol.Bike)
print(olo.TAka)


#                        60
#Multiple Inheritance----------  60 Working DAy

class baba:
    car= "BMW"
    taka= "200 crore"
    home = "20 floor"

class baba2:
    SmartPhone ="Samsung Z Flip 6"
    AC = "Samsung Air Conditionar"
    Headphone = " S O N Y "

class baba3:
    Laptop="MAcboook"
    Camera= " D S L R "
    CAR= "Truck"


class kaka(baba,baba2, baba3):
    BrokenCar= " "
    BrokenHome= " "

dj= kaka()
m= kaka()
mal= kaka()
lois= kaka()
hea=kaka()
dea=kaka()

print(dj.car)
print(m.home)
print(mal.SmartPhone)
print(hea.CAR)
print(dea.AC)


'61 Multilevel Inheritance '

class dad:
    car= "T E S L A - TESLA"
    money= " 50000 Crore"
    home= "70 floor building"

class son1(dad):
    Smartphone1= "iPhone 16 Pro Max"
    AC1 = "Toshiba Air Condinitor"
    Microphone1= "ASUS Rog Microphone"

class son2(son1):
    Camera1= " SONY DSLR "
    Laptop1= "Asus Rog Laptop "
    Webcam1= "Fifine "

class son3(son2):
    brokenCar=  " "
    brokenhOME= " "

gu=son3()
print(gu.Laptop1)

copa=son3()
print(copa.money)

gari=son3()
print(gari.car)

#ex 3

class Dadu:

    Asset = "1 crore"



class Baba1(Dadu):

    Asset1 = "50 lakh"



class Baba2(Dadu):

    Asset2 = "50 lakh"



class Baba1_Son1(Baba1):

    Asset1_1 = "25 lakh"



class Baba1_Son2(Baba1):

    Asset1_2 = "25 lakh"



class Baba2_Son1(Baba2):

    Asset2_1 = "25 lakh"



class Baba2_Son2(Baba2):

    Asset2_2 = "25 lakh"



print(Dadu.Asset)

print(Baba1.Asset, Baba1.Asset1)

print(Baba2.Asset, Baba1.Asset1)

print(Baba1_Son1.Asset1, Baba1_Son1.Asset,Baba1_Son1.Asset1_1)

print(Baba1_Son2.Asset1, Baba1_Son2.Asset,Baba1_Son2.Asset1_2)

print(Baba2_Son1.Asset,Baba2_Son1.Asset2,Baba2_Son1.Asset2_1)

print(Baba2_Son2.Asset2,Baba2_Son2.Asset,Baba2_Son2.Asset2_2)

