# # ========== 2.3.1 ==========
# while True:
#     print("Hi")
#     non=input("would you like to conitnue (Say no if your would like to disconinue) ")

#     if non=="no":
#         break
    


# ========== 2.3.2 ==========

# while True:
#     no=int (input("Please type in a number (0 to exit): "))
#     from math import sqrt
#     if no>0:
#         print(sqrt(no))
#     elif no==0:
#         print("Exiting...")
#         break
#     elif no<0:
#         print("invalid number")
        
# ========== 2.3.3 ==========
# number = 5
# print("Countdown!")
# while True:
#   print(number)
#   number = number - 1
#   if number == 0:
   
#     break

# print("Now!")

# ========== 2.3.4 ==========

# passw=input("password: ")
# while True:
#     pas=input("Repeat Password: ")
#     if pas!=passw:
#         print("They do not match!")
#     elif pas==passw:
#         print("user account created!")
#         break

# ========== 2.3.5 ==========

# pin=4321
# tries=int(0)
# while True:
#     tries=tries+1
#     npin=int (input("Pin: "))
#     if pin!=npin:
#         print("WRONG")
#     if pin==npin:
#         print ("Correct! It took only " + str (tries) + (" attempts!"))

# ========== 2.3.6 ==========

# year=int(input("Year: "))
# ly = 0
# while True:
#     if ly % 4==0 and ly % 100 !=0: 
#         print(year)
#     print("The next leap year after 2024 is " + str (ly))
    

# ========== 2.3.7 ==========

# sentence=" "
# while True:
#     word=input("Please type in a word: ")
  
#     sentence=sentence+" "+word   
#     if word=="end":
#         print(sentence)
#         break
    



# ========== 2.3.8 ==========

# sentence=" "
# lw=" "
# while True:
#     word=input("Please type in a word: ")
#     if lw==word:
#         break
#     lw=word
    
#     sentence=sentence+" "+word   
#     if word=="end":
#         print(sentence)
#         break
    

# ========== 2.3.9 ==========
# sen=" "
# total=0
# number=0
# mean=0
# pos=0
# neg=0
# mean=0

# while True:
#     nu=int(input("Please type in integer numbers. type in 0 to finish "))   
#     if nu==0:
#             print("numbers typed in " + str (total))
#             print("sum of numbers: " + str (number))
#             print("Mean of numbers " + str (mean))
#             print("postive number " + str (pos))
#             print("negative numbers " + str (neg))
#             break
#     sen=sen+" "+ str (nu)
#     total=total+1
#     number=number+nu
#     if nu>0:
#         pos=pos+1
#     if nu<0:
#         neg=neg+1
#     mean=number/total
  
    
