# ========== 4.2.1 ==========

# def greatest_number (n1,n2,n3):

#     if n1>n2 and n1>n3:
#         big=n1
#         return big
#     elif n2>n1 and n2>n3:
#         big=n2
#         return big 
#     elif n3>n1 and n3>n2:
#         big=n3
#         return big 
#     else:
#         big=0
#         return big


# n1 = greatest_number(3,4,1)
# n2 = greatest_number(99,-4,7)
# n3 = greatest_number(0,0,0)

# winner = greatest_number(n1, n2, n3)
# print("winner is", winner)

# ========== 4.2.2 ==========

# def same_chars (w1,n1,n2):
#     if n2>len(w1):
#         false="false"
#         return false
#     l1=(w1[n1])
#     l2=(w1[n2])
#     if l1==l2:
#         true="true"
#         return  true
#     if l1!=l2:
#         false="false"
#         return false
            

# print(same_chars("Programmer",6,7))
# print(same_chars("Programmer",0,4))
# print(same_chars("Programmer",0,12))


# ========== 4.2.3 ==========

# def first_word (first):

#     w1=(first[0:2])
#     return w1

# def second_word (second):
#     w2=(second[3:6])
#     return w2
# def last_word (last):
#     w3=(last[25:31])
#     return w3
# print(first_word("It was a dark and stormy python")) 
# print(second_word("It was a dark and stormy python")) 
# print(last_word("It was a dark and stormy python"))