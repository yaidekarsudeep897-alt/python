#1
i=0

while i<=10:
    x=0
    while x<i:
        print("sudeep",end="  ")
        x+=1
    print("")
    i+=1

#2
    i=1
is_failed=True
while is_failed:
    if i%2!=0:
        continue 
    print(f"try{i}")   
    i=i+1
    if i>100:
        break

#3

available_seats = 5

while available_seats > 0:
    print(f"{available_seats} seats available.")
    booking = input("Do you want to book a seat? (yes/no): ").lower()
    
    if booking == "yes":
        available_seats -= 1
        print("Seat booked!")
    else:
        print("No booking made.")

print("All seats are booked!")

#Write a program that counts from 1 to 10 using a while loop.

i=0
while i<=10:
    print(i)
    i+=1
    if i%2==0:
        continue
    i+=1

#Create a program that prints all odd numbers between 1 and 20 using a while loop.

i=1
while i<=20:
    if i%2!=0:
        print(i)
    i+=1

#Write a program that simulates a bus ticket booking system. 
# The bus has 8 seats. Each time a seat is booked, the available seats decrease. 
# When there are no seats left,
#  the loop stops and displays a message saying "All seats are booked."

available_seat=8

while available_seat>0:
    print(f"{available_seat} seat available.")
    booking=input("Do you want to booking seat? (yes/no)").lower()


    if booking=="yes":
        available_seat-=1
        print("seat booked")
    else:
        print("No booking mode")

print("All seats are booked!")


#Write a program that counts down from 10 to 1 using a 
# while loop and prints "Happy New Year!" after the countdown is over.


i=10

while i>=1:
    print(i)
    i-=1

print("Happy New Year!")