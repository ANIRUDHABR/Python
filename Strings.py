#A string is a sequential set of characters.we can access a character by using bracket operator.
sub = "Python"
print sub[0] #This is going to print the first letter "P"
#Remeber we can't give a float values inside the brackets like sub[1.5]. It gives a TypeError.
print '\n'
#Getting the length of the given string.We have len() function to do our work.
print len(sub) #It prints 6. 
print '\n'
#We can alternatively use negative indicies.
print sub[-1] #It prints the character "n".This shows that it reads the string from the reverse order.
print '\n'
#Line 3 to 8 is a simple traversal program,it shows a simple working of sequences and length operations.
sub = 'python'
index=0
while index < len(sub):
	print(sub[index])
	index = index+1
print '\n'
print sub[-6]   
	
print '\n'	
	
#This is for string slicing.
#The values inside the square braces have nothing to do with index valuue of the given string.
example = 'Python is best'
print example[10:13] #note: Prints only "bes", not the last character "t".
print example[:1] #prints p.
print example[0:6] #prints python. 

#Strings are immutable 
#we can't alter the given string. Because strings are immutable. we can only overcome this problem by creating a new string which is variation on the original.
#Below program gives the idea of the above statements.
print '\n'
greetings = 'Hello World!'
new_greetings = 'J' + greetings[1:]
print new_greetings #Prints Jello worls!.
new_greetings = 'J' + greetings[:2] 
print new_greetings #Prints "jhe" as output.
new_greetings = 'J' + greetings[7:] 
print new_greetings #Prints "Jorld!" as output.

#LOOPING & COUNTING
#The following program counts the number of times the letter "P" appers in the given string.
print '\n'
example = "python is best programming language"
count = 0
#Maintainance of proper intendation is very necessary here.
for letter in example:
	if letter == 'p':
		count = count + 1
print count	#prints 2(remember the case sensitivity)
#Above statement also demonstartes another pattern of computation called a counter.


#THE in OPERATOR
# the word "in" is a boolean operator that takes two strings and returns True if the first appears as a substring in the second.
print '\n'
'z' in 'python' #prints 'True' and this works only in python ide >>> not in the file
print '\n'
#STRING COMPARISION
#The comparison works on the strings.To see if two strings are equal.
if sub == 'python': #declared in line number 13
	print 'yeah! Its equal'

if sub < 'Python':
	print('your subject'+ sub +',comes before Python')
elif sub > 'Python':
	print('your subject'+ sub +',comes after Python') #this statement will be returned.
else:
	print('All right,python')


