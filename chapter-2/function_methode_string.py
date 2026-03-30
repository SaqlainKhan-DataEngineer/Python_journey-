#type 
age =24 
print(type(age)) #type function is used to check the data type of a variable 

#str
height = 5.10 
print( ' my height is :' + str(height)) 
#str function is used to convert a number to a string data type  
height =str(height) 
print(type(height)) 
height = height + " feet" 
print(height) 

height = 1000 
print(type(height)) 
height = height +10 
print (height)  

#len 
text = """saqlain waryah is a professional trader and now learning a 
new programming language python he wants to become a data engineer 
 in future and he is working hard to achieve his goal his goal is to move
 abroad to master to get international degree and then he got a chance to work in faang"""
print(len(text)) #len function is used to check the length of a string data type 
# count 
print(text.count("to ")) #count function is used to count the number of times an specific word or character appears in a string data type 


# transformation 
text = """saqlain waryah is a professional trader and now learning a 
new programming language python he wants to become a data engineer 
 in future and he is working hard to achieve his goal his goal is to move
 abroad to master to get international degree and then he got a chance to work in faang""" 
print(text.replace('to','').replace('saqlain','saqlainsajjad')) #replace function is used to replace a specific word or character with another word or character in a string data type  
# challeneg convert the messy phone number to a clean phone number  format with only difgits
phone_number ="+49 (176) 123-4567" 
print(phone_number.replace("+","").replace(" ","").replace("(","").replace(")","").replace("-",""))  

#join string
name = "saqlain sajjad "
age = "21"
print (name + age) 
print ("muhtasham sajjad "+"saqlain sajjad")   

age =22
height= 5.10
name = ("saqlain")
is_student = (True) 
bodycount = (None)  

print (f"my name is {name},My age is {age},my height is {height},my student status is {is_student},i like to kill{bodycount}")
print(f"{{this is f string }}") 
print(f"2 +3 ={{nothing }}")   
#split 
text = """saqlain waryah is a professional trader and now learning a 
new programming language python he wants to become a data engineer 
 in future and he is working hard to achieve his goal his goal is to move
 abroad to master to get international degree and then he got a chance to work in faang"""  
print(text.split(" ")) 
# * operaotr  
print('10'*3)

#extracting 
# indexing only charter from striing 
text = """saqlain waryah is a professional trader and now learning a 
new programming language python he wants to become a data engineer 
 in future and he is working hard to achieve his goal his goal is to move
abroad to master to get international degree and then he got a chance to work in faang""" 

print(text[10])
# slicing  to get a multiple charter from string this technique is called silicing 
text = """saqlain waryah is a professional trader and now learning a 
new programming language python he wants to become a data engineer 
 in future and he is working hard to achieve his goal his goal is to move
abroad to master to get international degree and then he got a chance to work in faang""" 
text1=text[-1]
text2=text[1]
print(text1,text2)

# cleaning 
text = """  saqlain waryah is a professional trader and now learning a 
new programming language python he wants to become a data engineer 
in future and he is working hard to achieve his goal his goal is to move
abroad to master to get international degree and then he got a chance to work in faang  """    
noofstrip = len(text) - len(text.strip())   
cleandata = len(text) == len(text.strip()) 
cleaned_text = text.strip() 
after_result = len(cleaned_text) == len( text.strip())  
print("how many strip",noofstrip) 
print('is my data clean',cleandata) 
print("is my data clean after cleaning",after_result)  # great logic building   

# best use case before using the data trimm the space and lowercase our data 
# advance challenege 
text="968-maria, (D@t@ Enginner);; 27y  " #name : maria |role: data enginner | age:27 
cleaningletter=text.replace('@','a')  
slicing_removeunnecessary=text[4:] 
replace_semicolon=text.replace(';','')
print(cleaningletter,slicing_removeunnecessary,replace_semicolon)