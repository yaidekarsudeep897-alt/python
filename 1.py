#input and output 
boy_name=input("Boy Name:")
boy_age=int(input("Boy Age:"))
girl_name=input("Girl Name:")
girl_age=int(input("Girl Age:"))

age_diff=abs(boy_age - girl_age)

print(f"{boy_name}  loves {girl_name} .Age Differnce is {age_diff}")

print(boy_name+" loves "+girl_name + " .Age Differnce is " + str(age_diff))


#concatenation
first_name="Yaidekar"
last_name="Sudeep"
full_name=first_name+" "+last_name
print(full_name)

#Repeatetion
message="Hello,World! "
print(message*10)

#string methods
clg="My college is KIT! "
print(clg.upper())
print(clg.lower())
print(clg.strip()*5)
print(clg.replace("KIT","Karavali"))
print(len(clg))

#slicing string
hero="Kichcha Sudeep"
print(hero[::3])
print(hero[6:])
print(hero[:14])
print(hero[0:7])