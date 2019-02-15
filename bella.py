print ("Bella's age categories\n")
 
print("")
try:
    year= int(input("please enter your year of birth: (numbers)\n"))
    age = 2019 - year
    age = int(age)
    if age <18:
        print('Minor')
    if age >=18 and age <=36:
        print("Youth")
    if age >=36:
        print("Elder")

except:
        print("please write in figures or numbers")
