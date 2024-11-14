#Create dictionary

person={
    "name":"Tamjid",
    "age":4200,
    "Hobbies":"stone",
    "best_freind":"Tridib"
}
#accsessing value
print(person["age"])
print(person["Hobbies"])
# add value
person["city"]="Dhaka"
person["school_name"]="ESS"
print(person)
del person["city"]
print(person)
# looping
for key,value in person.items():
    print(key,":",value)

# 
print(person.keys())
print(person.values())
print(person.items())