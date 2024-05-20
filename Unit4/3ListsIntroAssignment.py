# ========== 4.3.1 ==========
# list=[1,2,3,4,5]
# inx=0

# while inx!=-1:
#     inx=int(input("Index: "))
#     new=input("New value: ")
#     print ("before", list)
#     list[inx] = new
#     print ("after", list)




# ========== 4.3.2 ==========

# num=0
# long=int(input("How many items: "))
# sen=" "
# list=[]
# while num<long:
#     word=input("Item: ")
#     list.append(word)
#     num=num+1
# print(list)


# ========== 4.3.3 ==========

# print("d=add, r=remove, x=exit")
# word="x"
# sen=[]
# d=int(1)
# ln=0
# while word=="x":
#     w=input("add, remove, or exit: ")
#     if w=="a":    
#         sen.append(d)
#         d=d+1
#         ln=ln+1
#         print(sen)
#     elif w=="r":
        
#         sen.remove(ln)
#         ln=ln-1
#         d=d-1
#         print(sen)
#     elif w=="x":
#         print("Bye!")
#         break
        

# ========== 4.3.4 ==========

lw=" "
list=[]
total=0
while True:
    word=input("Word: ")
    if word in list:
        break
    list.append(word)
    print(list)
    total=total+1

print("You typed in", total, "different words")







