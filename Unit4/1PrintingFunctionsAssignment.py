# ========== 4.1.1 ==========
def line(l,w):
    print(l*w[0:1])
    

# line(7, "%")
# line(10, "LOL")
# line(3,"*")
# line(7, "robert")

# ========== 4.1.2 ==========

# def box_of_hashes(hieght):
#     while 0<hieght:
#         line(10,"#")
#         hieght=hieght-1
        


# box_of_hashes(5)
# print()
# box_of_hashes(2)


# ========== 4.1.3 ==========

# def  box_of_hashes(high):
#     num=0
#     while num<high:
#         line(10,"#") 
#         num=num+1
# box_of_hashes(5)
# print("")
# box_of_hashes(2)


# ========== 4.1.4 ==========


# def square_of_hashes(hieght,word):
#     num=0
#     while num<hieght:
#         line(hieght,word)
#         num=num+1
       

# square_of_hashes(5,"*")
# print()
# square_of_hashes(3,"o")




# ========== 4.1.5 ==========

# def triangle (length):
#     nu=0
#     amount=1
#     while nu<length:
#         line(amount, "#")
#         amount=amount+1
#         nu=nu+1

# triangle(6)
# print()
# triangle(3)

# ========== 4.1.6 ==========

# def shape (n1,w1,n2,w2):
#     amount=1
#     num=-0
#     while True:
#         line(amount,w1)
#         num=num+1
        
#         if num==n1:
#                 num=0
#                 break
#         if amount!=n1:
#              amount=amount+1
#     while num<n2:
#          line(amount,w2)
#          num=num+1
            

# shape(5, "X", 3, "*")
# print()
# shape(2, "o", 4, "+")
# print()
# shape(3, ".", 0, ",")


# ========== 4.1.7 ==========
    
# def spruce(nu):
#     num=0
#     amount=1
#     print("a spruce!")
#     while num<nu:
#         line(amount,"*")

# spruce(5)
# spruce(3)