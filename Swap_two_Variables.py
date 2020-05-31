#Swap 2 variables

a = 5
b = 6

temp = a      #here we assigning a third variable temp to store the value of a so that it will print both a and b
a = b
b = temp       
#after print(a) and print (b)
                             #output : 6
                             #output : 5 
            
#other way, without using any third variable
a = 8
b = 4
a = a + b
b = a - b
a = a - b
#after print(a) and print(b)       #output : 4
                                   #output : 8
                                   #still this method consume extra bits and memory so,,
        
#the simple way to swap two variables by,
a = 3
b = 9
a,b = b,a
print(a)                        #output : 9
print(b)                        #output : 3
