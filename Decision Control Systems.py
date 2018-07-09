# WAP for Finding max and min ages using looping statements

Ms_Dhoni = int(input('Enter Ms Dhoni"s Age :'))  # User Inputs Ages
Virat_Kohli = int(input('Enter Virat_Kohli"s Age :'))
Hardik_Pandya = int(input('Enter Hardik_Pandya"s Age :'))

print('Age of Ms_Dhoni is %d yrs and of Virat_Kohli is %d yrs and that of Hardik_Pandya is %d yrs' % (Ms_Dhoni, Virat_Kohli, Hardik_Pandya))
print("\n-------------For Checking Maximum Age-------------------------\n")

if (Ms_Dhoni > Virat_Kohli)and(Ms_Dhoni > Hardik_Pandya):
    print("# Age of Senior Most player is ->", Ms_Dhoni)
elif (Virat_Kohli > Ms_Dhoni)and(Virat_Kohli > Hardik_Pandya):
    print("# Age of Senior Most player is->", Virat_Kohli)
else:
    print("Age of Senior Most player is->", Hardik_Pandya)

print("\n--------------------------For checking Minimum Age----------------\n")

if (Ms_Dhoni < Virat_Kohli) and (Ms_Dhoni < Hardik_Pandya):
    print("Age of Junior Most player is ->", Ms_Dhoni)
elif (Virat_Kohli < Ms_Dhoni) and (Virat_Kohli < Hardik_Pandya):
    print("Age of Junior Most player is->", Virat_Kohli)
else:
    print("Age of Junior Most player is->", Hardik_Pandya)
print("\n-------------------------End of the program---------------------------\n")


# PRize Distribution Program

points = int(input("Enter your points Scored :"))
if 1 <= points <= 50:
    print("Sorry! No prize this time.")
elif 51 <= points <= 150:
        print("Wooden Dog")
elif 151 <= points <= 180:
        print("Fanny bag")
elif 181 <= points <= 200:
        print("Chocolates")
else:
    print("its over\n")

# ProgrAm For diffrentiating between Rectangle nd Square

dim1 = float(input('Enter the value :'))
dim2 = float(input('Enter the value :'))
dim3 = float(input('Enter the value :'))
dim4 = float(input('Enter the value :'))

print('----------------------------CheCking figureS---------------')
if dim1 == dim2 and dim3 == dim4 and dim2 == dim3:
    Perimeter = 4 * dim1
    Area = dim1 ** 2
    print("this iz a Square!! having area %f sq.units and its perimeter is %f units\n" % (Area, Perimeter))
elif dim1 == dim3 and dim2 == dim4:
    Perimeter = 2 * (dim1 + dim2)
    Area = dim1 * dim2
    print("this iz a Rectangle!! having area %f sq.units and its perimeter is %f units\n" % (Area, Perimeter))
else:
    print("!! some other figure dimensions !!\n")

# Python program to check if the input year is a leap year or not

year = int(input("Enter the YeAr u want 2 check !!\n"))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year\n".format(year))
        else:
            print("{0} is not a leap year\n".format(year))
    else:
        print("{0} is a leap year\n".format(year))
else:
    print("{0} is not a leap year\n".format(year))

# Cost Manipulation ProgrAm

print('------------------Welcome to AksK Trading CompAny------------------------------')
units = int(input("Please enter no. of units you want to buy: "))
print("Purchased Quantity :", units, 'units')

if units > 10:
    print("------------------------------------------------------------------")
    print("Congrats!! You will get a 10% discount. ")
    print('total cost to be paid will be : Rs', (units*100)-0.1*(units*100))
    print("Thanks!! For coming. Visit Again!!")
else:
    print("------------------------------------------------------------------")
    print("Total cost of units to be paid: Rs", (units*100))
    print("Thanks!! For coming. Visit Again!!")

print("--------------------------End of the program--------------------")
