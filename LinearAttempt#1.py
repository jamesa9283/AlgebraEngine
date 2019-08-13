#Consider an equation of form, Ax + B = Cx + D

z = input('Enter your function:')
Variables=[]
Variables.extend(z.split(" "))
n="+"
i=0 #loop counter
length = len(Variables)  #list length 
while(i<length):
	if(Variables[i]==n):
		Variables.remove (Variables[i])
		# as an element is removed	
		# so decrease the length by 1	
		length = length -1  
		# run loop again to check element							
		# at same index, when item removed 
		# next item will shift to the left 
		continue
	i = i+1
Variables.remove("=")
Variables_x = []
for elem in Variables:
	if elem.endswith("x"):
		Variables_x.append(elem)
		Variables.remove(elem)
i=0 #loop counter
length = len(Variables_x)  #list length 
while(i<length):
	y=Variables_x[i]
	p=y.split("x")
	Variables_x.extend(p)
	Variables_x.remove (Variables_x[i])
	# as an element is removed	
	# so decrease the length by 1	
	length = length -1  
	# run loop again to check element							
	# at same index, when item removed 
	# next item will shift to the left 
	continue
	i = i+1
Variables_x.pop(1)
Variables_x.pop()
Variables_x = [int(i) for i in Variables_x]
Variables = [int(i) for i in Variables]
a=Variables_x[0]-Variables_x[1]
b=-Variables[0]+Variables[1]
print(b/a)
