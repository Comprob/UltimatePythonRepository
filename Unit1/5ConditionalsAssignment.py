
print("########## 1.5.1 ##########")
sp=int (input("please type in a number: "))
if sp==1984:
    print ("orwell")

print("########## 1.5.2 ##########")
av=int (input("please type in a number: "))
if av<+0:

    print ("the absolute vale of this number is:" + str (av*-1)) 

print("########## 1.5.3 ##########")
nm=input ("what is your name? ")

if nm!="Jerry":
   pow=int (input ("how many portion of soup?"))
   print ("the total cost is " + str (pow *5.9)) 
print ("next please!")

print("########## 1.5.4 ##########")
nu=int (input("Type in a number: "))
if nu<1000:
    print("This number is smaller than 1000")
if nu<100:
    print("this number is smaller than 100")
if nu<10:
    print("this number is smaller than 10")
print("Thank you")
print("########## 1.5.5 ##########")
nu1=int (input("Number 1: "))
nu2=int (input("Number 2: "))
op=input ("Operation:")
if op=="add":
    print (nu1+nu2)
if op=="subtract":
    print (nu1-nu2)
if op=="multiply":
    print (nu1/nu2) 
print("########## 1.5.6 ##########")
f=int (input("Type in a temperature"))
c=int (f*-32)
print(str (f) + " degree Farhernheit equals " + str (f-32*5/9) + " degrees Celsius" )
if c<0:
    print ("Brr! it's cold in here!")

print("########## 1.5.7 ##########")
work=int (input("Hourly wage: "))
hours=int (input("Hours worked: "))
day=input ("Day of the week: ")
total=int (work*hours)
if day!= "Sunday":
    print("daily wages" + str (total) + " ")
if day=="Sunday":
    print("daily wages " + str (total*2))
    

print("########## 1.5.8 ##########")
points = int(input("How many points are on your card? "))
if points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")

print("You now have", points, "points")

print("########## 1.5.9 ##########")
print("what is the weather forecast for tomorrow?")
temp=int (input("Temperatue (C)"))
rain=input ("Will it rain (yes/no):")
print("wear jeans and a t-shirt")
if temp >=10:
    print("I recommend a sweater as well")
if temp >=0:
    print("I recommend a sweater as well")
    print("take a jacket with you")
if rain=="yes" :
    print("I think gloves are in order")  
    print("Don't forget your umbrella!")

