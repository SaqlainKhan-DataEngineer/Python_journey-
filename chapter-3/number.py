#type
x=4
y=10.5
z=10+9j 
print(type(x))
print(type(y))
print(type(z))
# conveert type 
x="24" #string ma bhi agr numeric value  ho to he int ma convert ho gai warna ni 
x= int(x)
print(type(x))
# complex 
x = 3
y=9
print(complex(x,y)) 

#basic math operator 
print(2+3)
print(10-5)
print(5*10)
print(8/2)
print(9//2)
print(6**4)
print(23%7)  
#rounding 
#abs use to get a non negative value 
x=1 
y=5 
print(abs(x-y))
#round 
x=79.4 
print(round(x))
import math
y=29.5
print(math.floor(y)) 
z=33.2
print(math.ceil(z)) 
p=35.506324
print(math.trunc(p)) 
print(round(p,2)) 
#to use ceil and floor we have to import math 
 
#challenge #print random number and whtther the number is even or odd
import random 
num=(random.randint(1,100))  
print(num%2)  
# this is used to genrate a random number   
# validation 
x=70.1
print(x.is_integer()) 
x=70
print(isinstance(x,complex))  
