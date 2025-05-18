set0={1,2,3}
print(set0)
set1={1.0,"hi",(1,2,3)}
print(set1)
set2={1,1,2,3,4,5,5}
print(set2)
set3=set([1,2,3,4])
print(set3)
set4=([1,2,3,4,5])
print("original set: ",set4)
set4.pop()
print("after removing the last element of this set: ")
print(set4)