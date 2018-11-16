from builtins import print, property
#---------------------------------------------List-------------------------------------------------
num=[90,55,10,20,30,40]
print(min(num))

print(max(num))
print(sum(num))
print(len(num))
print(num[-1])
print(num[-6])
num=['saurabh','singh',12.5,56,'S']
print(num)
num2=['i am','second','bro',12,93,0.8]
mill=[num,num2]
print(mill)

print(num.append(45))
print(num)
num.insert(1,'i am at 1 index')
print(num)

num.remove('S')
print(num)

num.pop(len(num)-2)
print(num)

print(num2)
num2.clear()
print(num2)
num2=['i am','second','bro',12,93,0.8]
print(num2)
del num2[3:]
print(num2)

num2.extend([12,93,0.8,17,18,19,20,21,22,23])
print(num2)

#sum(num2)
#print(num2)
del num2[0:3]
print(num2)
print(sum(num2))

num2.sort()
print(num2)

tuple=(50,40,30,20,10)
print(tuple)
#commit2
#-----------------------------------tuple--------------------------------------------------
tup1=(1,1,1,3,5,6)
tup1.count
print(tup1.count)
print(tuple[0])

#tup1[1]=33  tuple in python is immutable ,once we created value ,we can not change it



#----------------------Set----------------------------------------------------------------
set={22,25,14,21,5}
print(set)
print(set)
set2 ={98,52,101,105,11,53,11}
print(set2)
