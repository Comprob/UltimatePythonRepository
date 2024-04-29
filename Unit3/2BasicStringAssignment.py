# ========== 3.2.1 ==========

# str=input("Please type in a string: ")
# nu=int(input("Please type in a amount: "))
# print(str*nu)

# ========== 3.2.2 ==========

# n1=input("Please type in string 1: ")
# n2=input("Please type in a string 2: ")
# len1=len(n1)
# len2=len(n2)
# if len1>len2:
#     print(n1 + " is longer")
# elif len1<len2:
#     print(n2 + "is longer")
# else:
#     print("The string are equally long")
# # ========== 3.2.3 ==========

# wo=input("Please type in a string: ")
# index=len(wo)
# while index > 0 :
#     letter=wo[index-1]
#     index=index-1
#     print(letter)


# ========== 3.2.4 ==========

# word=input("Please type in a string: ")
# letter1=word[1]
# letter2=word[len(word)-2]
# if letter1==letter2:
#     print("The second and the second to last charcters are " + letter1)
# elif letter1!=letter2:
#     print("The second and the second to last charcters are differnet")

# ========== 3.2.5 ==========

# nu=int(input("width: "))

# print("#" * nu)
# ========== 3.2.6 ==========

# width=int(input("Width: "))
# height=int(input("Height: "))
# while height>0:
#     height=height-1
#     print("#" * width)

# ========== 3.2.7 ==========

# while sen!="":
#     sen=input("Please type in a string: ")
#     lenth=len(sen)
#     print(sen)
#     print("-" * lenth)
    



# ========== 3.2.8 ==========

# word=input("Please type in a string: ")
# length=len(word)
# total=20-length
# nu="*"*total
# print(nu+word)

# ========== 3.2.9 ==========

word=input("word: ")
outside=("*"*30)

the=len(word)
print(outside)
total=30-the
# ind1=total/2
# ind2=total/2
ind2=" "*total/2
ind1=" "*total/2
if len(word) % 2==0:
    ind=ind+1
print(the)
print("*" + ind1 + word + " "*ind + "*")
print(outside)

