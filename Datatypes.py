# Data types : None, Numeric, List, Tuple, Set, String, Range, Dictionary
#List, Tuple, Set, String, Range are known as Sequences because their output will be in a sequence
#None ., it is the other form of NULL.

# numeric ., it has int,float,complex,bool.
 
#float
num = 2.5
type(num)        #output: float // type function is used to define a type

#int
num = 2
type(num)        #output: int

#complex
num = 6+8j       #here j is an imaginary number, used i maths 
type(num)       #output: complex

#conversion
a = 2.5         #can convert the form, here a is a float
b = int(a)      #we defined it for b with int
type(b)          #so here the output will be int...converted float into int

#boolean
a = 5           
b = 8
b > a           #output : true 
b < a           #output : false
int(True)       #output : 1
int(False)      #output : 0
c = b < a
type(c)         #ouput : bool,   because it's a boolean type

#list
ls = [2,6,3,9,2,0]      #list is defined by [] brackets
type(ls)                #output : list

#tuple
tu = (45,66,1,22,54,89) #tuple is defined by ()brackets
type(tu)                 #output : tuple

#set
st = {44,89,1,11,80}     #set is defined by {} brackets
type(st)                 #output: set

#string
num = "load"             #string defined by "" or ''
type(num)                 #output: str

#range
range(15)              #output : range(0,15)
list(range(15))       #output : [0,1,2,.....13,14] just to see the range values we used list type 
list(range(6,20,3))    #output : [6,9,12,15,18]  (6,20,3) 6 and 20 represents the starting range and ending range, 3 represent the gaps between the values from starting to ending.

#dictionary
dit = {'Ben':'Good','Martin':'Bad','Sam':'Average'}   #  {keys:values,k:v,....}
dit                        #output : same dit values
dit.keys()   #output : Ben,martin,sam....prints only the keys
dit['Martin']  #output : 'Bad'
dit.get('Sam')  #output : 'Average'  ....we can also fetch values by using get
