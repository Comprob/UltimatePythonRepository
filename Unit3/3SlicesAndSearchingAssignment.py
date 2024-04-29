# ========== 3.3.1 ==========

# word=input("Please type in a string: ")
# lent=len(word)
# nu=0
# lent=lent+1
# while nu!=lent:
#     part=word[0:nu]
#     nu=nu+1
#     print(part)

    # print(lent)




# ========== 3.3.2 ==========
    
# word=input("Please type in a string: ")
# lent=len(word)
# nu2=lent+1
# nu=lent
# while nu!=-1:
#     part=word[nu:nu2]
#     nu=nu-1
#     if nu==-1:
#         nu=nu
#     print(part)

# ========== 3.3.3 ==========

# word=input("Please type in a string: ")
# if "a" in word:
#     print("a found")
# else:
#     print("a not found")
# if "e" in word:
#     print("e found")
# else:
#     print("e not found")
# if "o" in word:
#     print("o found")
# else:
#     print("o not found")
    
    

# ========== 3.3.4 ==========

# word=input("Please type in a word: ")
# cha=input("Please type in a character: ")
# cha1=(word.find(cha))
# if cha1 + 3> len(word):
#     print("")
# else:
#     print(word[cha1:cha1+3])

# ========== 3.3.5 ==========

# word=input("Please type in a word: ")
# letter=input("Please type in a character: ")
# while True:
#     if len(word) == 0:
#         break
    # found_position=word.find(letter)

#     if found_position == -1:
#         break

    
    # result = word[found_position:found_position+3]
#     print(result)
#     word = word[found_position + 1:]



    # if len(word) == 0:
    #     break
    # print= word [2:]

# ========== 3.3.6 ==========

word=input("Please type in a string: ")
sub=input("Please type in a substring: ")

# while True:
index=(word.find(sub))
index=index+1
org=index
word=word[index: ]
index=(word.find(sub))
# print(index)
index=index+org
# print(index)
if index<org:
    print("The substring does not occur twice in the string")
else:
    print("The second occurence of the substring is at index "  ,index)
