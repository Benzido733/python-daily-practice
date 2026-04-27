guests = open ("guests.txt", "w") 

initial_guests =["Bob" ,"Andrea" , "Manual" , "Polly" , "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")

guests.close()

guests = open ("guests.txt", "r")   
print("Here is the list of guests:")
print(guests.read())
guests.close()