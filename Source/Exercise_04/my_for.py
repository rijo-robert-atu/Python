iterable_variable = [1,2,3,4,5,6]

#for item in iterable_variable:
	# For each item, execute this code block
#	print(item)
for item in iterable_variable:
    if item%2 == 0:
     continue
     # missing continue in the lectures notes
    print(item)