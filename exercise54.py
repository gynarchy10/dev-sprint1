# This is where Exercise 5.4 goes
# Name: Jenna Gopilan 

def is_triangle (side1, side2, side3):
    if side1 > side2 + side3:
        print "No"
    elif side2 > side1 + side3:
        print "No"
    elif side3 > side1 + side2:
        print "No"
    else:
        print "Yes"
        
def ask_sticks ():
    stick1 = int(float(raw_input ("Give me the first stick length! \n")))
    stick2 = int(float(raw_input ("What about the length of the second stick eh? \n")))
    stick3 = int(float(raw_input ("Good, now what about the last stick's length? \n")))
    is_triangle (stick1, stick2, stick3)
    
ask_sticks()