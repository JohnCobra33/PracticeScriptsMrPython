#The director of a school is organizing a study trip and needs to determine how much to charge each student and how much to pay the travel company for the service. The charging scheme is as follows:

#If there are 100 or more students, the cost per student is 65 euros.
#For 50 to 99 students, the cost is 70 euros.
#For 30 to 49 students, the cost is 95 euros.
#For fewer than 30 students, the bus rental cost is 4000 euros, regardless of the number of students.
#Create an algorithm to determine the payment to the bus company and the amount each student must pay for the trip.

students = int(input("Enter the number of students attending the trip: "))

if students >= 100:
    print("The price would be 65€ per student, total:", students * 65)
elif students >= 50:
    print("The price would be 70€ per student, total:", students * 70)
elif students >= 30:
    print("The price would be 95€ per student, total:", students * 95)
else:
    print("The price per student is:", 4000 / students, "total 4000")
