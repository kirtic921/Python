# Pet food Recommendation
# Problem: Recommend  a type of pet food based on pet's species and age. (e.g., Dog: <2years - puppy food ; Cat: >5years - senior cat food)

pet=input("Enter the species of your pet: ")
pet_age=input("Enter age: ")
ipet_age=int(pet_age)

if(pet=='Cat'):
    if(ipet_age<2):
        status='Puppy cat food'
    elif(ipet_age>=2 and ipet_age<=5):
        status='Adult cat food'
    else:
        status='Senior cat food'

elif(pet=='Dog'):
    if(ipet_age<2):
        status='Puppy Dog food'
    elif(ipet_age>=2 and ipet_age<=5):
        status='Adult Dog food'
    else:
        status='Senior Dog Food'


print("Your pet needs a", status)