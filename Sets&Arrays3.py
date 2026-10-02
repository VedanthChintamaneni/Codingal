import array as arr

array_num = ['why', 'goodbye', 'bye', 'sup', 'hello', 'hi']
print("Original array: "+str(array_num))

print("Number of occurrences of the number 3 in the said array: "+str(array_num.count(3)))

array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))