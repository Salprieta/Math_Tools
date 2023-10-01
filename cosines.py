import math
import sys
from winreg import SetValue

print("Type 1 if you have 3 sides")
print("Type 2 if you have 2 sides and an angle in between")
print("Type 3 if you have a corresponding side and angle + a side")

def three_sides():  
    while True:
        try:
            side_A = float(input("Side A\n"))
            side_B = float(input("Side B\n"))
            side_C = float(input("Side C\n"))
            break
        except ValueError:
            print("Must be number")
        
    print(math.degrees(math.acos((side_C**2+side_B**2-side_A**2)/(2*side_C*side_B))))
    print(math.degrees(math.acos((side_C**2+side_A**2-side_B**2)/(2*side_C*side_A))))
    print(math.degrees(math.acos((side_A**2+side_B**2-side_C**2)/(2*side_A*side_B))))
        
def two_sides():
    while True:
        try:
            side_A = float(input("Side A\n"))
            side_B = float(input("Side B\n"))
            angle_C = float(input("Angle of Missing Side\n"))
            break
        except ValueError:
            print("Must be number")
    print(math.sqrt(side_A**2+side_B**2-2*side_A*side_B*math.cos(math.radians(angle_C))))

def corresponding():
    while True:
        try:
            side_A = float(input("Side with corresponding angle\n"))
            side_B = float(input("Other Side\n"))
            angle_A = float(input("Corresponding angle\n"))
            break
        except ValueError:
            print("Must be number")
    print((2*side_B*math.cos(math.radians(angle_A))+math.sqrt((2*side_B*math.cos(math.radians(angle_A)))**2 - 4*(side_B**2-side_A**2)))/2)

choice = input("Options 1-3\n")
if choice == "1":
    three_sides()
elif choice == "2":
    two_sides()
elif choice == "3":
   corresponding() 
else:
    sys.exit()