# advance challenege 
text="968-maria, (D@t@ Enginner);; 27y  " #name : maria |role: data enginner | age:27  
name=text[4:9]
role=text[12:25].replace('@','a')
age=text[-5:-3]
cleaned=(f"name : {name} |role: {role} | age:{age}") 
print(cleaned.lower())
rollnumber="22r"
print("".join(filter(str.isdigit,rollnumber)))

#second way 
text = "968-Maria, ( D@t@ Engineer );; 27y.. "

# Clean name
name = text.split('-')[1].split(',')[0].strip().lower()
# Clean role
role = text.split('(')[1].split(')')[0].replace('@','a').strip().lower()

# Clean age (sirf numbers pakarna)
age = "".join(filter(str.isdigit, text.split(';')[-1]))

print(f"name: {name} | role: {role} | age: {age}") 

 
#to get digit from string
print("".join(filter(str.isdigit,"saqlain500"))) 


#raw_data = "EMP101#Zaid_Khan*| ( Python-Developer ) |; Salary-85k++" 

#name: "zaid khan"role: "python developer"salary: "85" 
text="EMP101#Zaid_Khan*| ( Python-Developer ) |; Salary-85k++"
name=text.split('#')[1].split('*')[0].replace('_',' ').lower() 
role=text.split('(')[1].split(')')[0].replace('-',' ').lower().strip()
salary=("".join(filter(str.isdigit,(text.split(';')[1].split('-')[1].replace('+',''))))) 
print(name)
print(role) 
print(salary) 
 #name : maria |role: data enginner | age:27  
text="968-maria, (D@t@ Enginner);; 27y"
print(text.find("m"))  # really good use to check the position 
print(text[text.find("-")+1:].replace('@','a').replace(';','').replace('y','').replace(',','').replace('(','').replace(')',''))  
