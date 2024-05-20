
def scrabble_score(word):
    ind=0
    ind2=word[ind]
    list1=["a,e,i,o,u,l,n,s,t,r"]
    list2=["d,g"]
    list3=["b,c,m,p"]
    list4=["f,h,v,w,y"]
    list5=["k"]
    list8=["j,x"]
    list10=["q,z"]
    nu=0
    while ind<=len(word):
        ind=ind+1
        if ind2 in list1:
            nu=nu+1
        elif ind2 in list2:
            nu=nu+2        
        elif ind2 in list3:
            nu=nu+3
        elif ind2 in list4:
            nu=nu+4
        elif ind2 in list5:
            nu=nu+5
        elif ind2 in list8:
            nu=nu+8
        elif ind2 in list10:
            nu=nu+10
    print(nu)




print( scrabble_score("hello"))
print( scrabble_score("world"))
print( scrabble_score("zebra"))
print(  scrabble_score("xylphone"))
