# dedine a string to iterate over
for this_letter in "Rijo Robert":
	#Specify which letter to test for
	if this_letter == "b":
	 #found the test letter
	   print(f"woo hoo, found the letter{this_letter}!")
	   # Exit the current loop
	   break
	else:
	 #Didn't find the letter
         print(f"Aww man, I didn't found the {this_letter}!")
	 
 # The break will stop at the point where the condition satifes, but continue will not 