##"Two motorcycles are traveling at different speeds (vel1 and vel2) and are separated by a distance 'dis.' The motorcycle behind is traveling at a higher speed than the first one. A Python script is requested to prompt the user for the distance between the motorcycles in kilometers and their respective speeds. The script should then return the time it will take for motorcycle 2 to catch up with motorcycle 1."

Distance = int(input("Distance in KM: "))

Motorcycle1 = int(input("Speed of Motorcycle 1: "))

Motorcycle2 = int(input("Speed of Motorcycle 2: "))

time = (Distance / (Motorcycle2 - Motorcycle1))

print("The motorcycles will meet in:", int(time * 60), "minutes")
