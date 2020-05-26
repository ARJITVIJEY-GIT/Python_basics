#dictionary  It holds key:value pair  , uses {}


data = {1:'arjit', 2:'vijey', 4:'ben', 5:'jerry'}
print(data)
print(data[2])

data.get(4)            #ouput ben
data.get(3)           #3 is not defined,,,output: there won't be an error and also the output was empty
print(data.get(3))       #if we print this the output will be displayed as "None"

data.get(5,'not found')  #here the ouput will be "jerry", not found not print here
data.get(3,'not found')     #since 3 is not defined, now the output not be empty, it will print as "not found"

Items = ['Ice','Cake','Milk','Egg']
made_in = ['Iceland','New york','India','Brazil']
data = dict(zip(Items,made_in))         # "zip" will join the two variable values, "dict" will change both into a dictionary
print(data)

data['Cake']                     #print as New york
data['Chocolate'] = 'Europe'          #to add additional key to the dictionary
print(data)
del data['Egg']             #to delete the key in the dictionary
print(data)

prog = {'Ice':'Iceland', 'Cake':'New york', 'Milk':['India','Srilanka'], 'Chocolate':{'Dairymilk':'France','Kitkat':'Italy', 'Milkybar':'Germany'}}  #Adding a dictionary inta a dictionary
prog['Milk']         #prints 'India' & 'Srilanka'
prog['Milk'] [1]    #prints 'Srilanka'
prog['Chocolate']       #prints all the value
prog['Chocolate'] ['Milkybar']    #prints only the 'Germany'
print(prog) 
print(data)



