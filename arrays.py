import array as arr
array3=arr.array('i',[1,2,3,4,5,2,2])
print("original array:"+str(array3))
print("number of occurences of number 2 in the said array: "+str(array3.count(2)))
array3.reverse()
print("reverse the order of the items")
print(str(array3))