#Stores the key with a value, value being the price
mcDict = {
    "1. McStandard": 3.45,
    "2. McGordo": 5.10,
    "3. McChonk": 6.93
}

#Intially prints the selection string statement
print("Choose either of the burgers below\n", "Type: 1, 2, 3\n")


# Goes through each key and value in the dictionary
for key, value in mcDict.items() :
    print(key, "which costs", "$", value, )

# Puts a line break after the print loop
print("")


#Now, asks the user for the input and checks what they chose
chosenBurger = ""
chosenBurgerIndex = int(input())

#Check which one the user picked and get the dictionary key again
if chosenBurgerIndex == 1:
    chosenBurger = "McStandard"
elif chosenBurgerIndex == 2:
    chosenBurger = "McGordo"
elif chosenBurgerIndex == 3:
    chosenBurger = "McChonk"
else:
    print("Input a real number, not words...")




#Ask the user whether they want cheese or not
print("You chose the", chosenBurger, "would you like to add cheese for only $1.23\n", "Type 'yes' or 'no'\n")
cheeseInput = input()

#Adds a blank line to make it look cleaner
print("")
cheeseBool = False
cheesePrice = 0
#Checks whether the user wants cheese
if cheeseInput == "yes" or cheeseInput == "Yes" or cheeseInput == "y" or cheeseInput == "Y":
    print("Okay, you added cheese to the", chosenBurger, "would you like to make it a combo?\n")
    cheeseBool = True
    cheesePrice = 1.23
else:
    print("Okay, cheese isn't your think for the", chosenBurger, "would you like to make it a combo?\n", "Type 'Yes' or 'No'")
    cheeseBool = False




#Input whether they want a combo or not
firstComboInput = input()
comboArray = ["small", "medium", "large", "noCombo"]
comboPriceArray = [2.63, 3.76, 4.89, 0]

#These are being added to the coressponding arrays in the if and else wayyy below
combo = " "
comboPrice = 0

#First ask whether they do want a combo
if firstComboInput == "y" or firstComboInput == "yes" or firstComboInput == "Yes" or firstComboInput == "Y":
    print("Okay, what kind of combo would you like?\n", "Would you like a small, medium, or large?\n")
    secondComboInput = input()
    #Now, ask them whether they want a small, medium, or large
    if secondComboInput == "small" or secondComboInput == "Small" or secondComboInput == "S" or secondComboInput == "s":
        print("Okay, you'll receive a small", chosenBurger, "combo")
        combo = comboArray[0]
        comboPrice = comboPriceArray[0]
    elif secondComboInput == "medium" or secondComboInput == "Medium" or secondComboInput == "medium" or secondComboInput == "m":
        print("Okay, you'll receive a medium", chosenBurger, "combo")
        combo = comboArray[1]
        comboPrice = comboPriceArray[1]
    elif secondComboInput == "large" or secondComboInput == "Large" or secondComboInput == "L" or secondComboInput == "l":
        print("Okay, you'll receive a large", chosenBurger, "combo")
        combo = comboArray[2]
        comboPrice = comboPriceArray[2]
    else:
        print("Sir you needed to write a valid combo, please start your order over\n")
else:
    print("Okay, you'll only get the", chosenBurger, "without the combo")
    combo = comboArray[3]
    comboPrice = comboPriceArray[3]




#Now, let's make the actual calculator yet before, let's make the if else statement
totalPrice = 0
mcStandardSum = mcDict["1. McStandard"] + cheesePrice + comboPrice
mcGordoSum = mcDict["2. McGordo"] + cheesePrice + comboPrice
mcChonkSum = mcDict["3. McChonk"] + cheesePrice + comboPrice


#Adding the numbers below now
if chosenBurgerIndex == 1 and combo == comboArray[0]:
    currentPrice = mcStandardSum
    totalPrice = currentPrice
elif chosenBurgerIndex == 2  and combo == comboArray[0]:
    currentPrice = mcGordoSum
    totalPrice = currentPrice
elif chosenBurgerIndex == 3 and combo == comboArray[0]:
    currentPrice = mcChonkSum
    totalPrice = currentPrice
elif chosenBurgerIndex == 1 and combo == comboArray[1]:
    currentPrice = mcStandardSum
    totalPrice = currentPrice
elif chosenBurgerIndex == 2 and combo == comboArray[1]:
    currentPrice = mcGordoSum
    totalPrice = currentPrice
elif chosenBurgerIndex == 3 and combo == comboArray[1]:
    currentPrice = mcChonkSum
    totalPrice = currentPrice
elif chosenBurgerIndex == 1  and combo == comboArray[2]:
    currentPrice = mcStandardSum
    totalPrice = currentPrice
elif chosenBurgerIndex == 2 and combo == comboArray[2]:
    currentPrice = mcGordoSum
    totalPrice = currentPrice
elif chosenBurgerIndex == 3 and combo == comboArray[2]:
    currentPrice = mcChonkSum
    totalPrice = currentPrice
elif chosenBurgerIndex == 1  and combo == comboArray[3]:
    currentPrice = mcStandardSum
    totalPrice = currentPrice
elif chosenBurgerIndex == 2 and combo == comboArray[3]:
    currentPrice = mcGordoSum
    totalPrice = currentPrice
elif chosenBurgerIndex == 3 and combo == comboArray[3]:
    currentPrice = mcChonkSum
    totalPrice = currentPrice
elif chosenBurgerIndex == 1 and combo == comboArray[4]:
    currentPrice = mcChonkSum
    totalPrice = currentPrice
elif chosenBurgerIndex == 2 and combo == comboArray[4]:
    currentPrice = mcGordoSum
    totalPrice = currentPrice
elif chosenBurgerIndex == 3 and combo == comboArray[4]:
    currentPrice = mcChonkSum
    totalPrice = currentPrice
else:
    print("code is broken")


#Now, calculate the taxes
taxedTotalPrice = (totalPrice * 0.89) + totalPrice

#The final price is set in stone now
finalPrice = round(taxedTotalPrice, 2)


#Let's make a receipt
def create_receipt():
    print("\nYou ordered the", chosenBurger, combo, "and your final price is below\n")
    print("\t\t\t ", "$", "Final Price:" finalPrice)
    print("Thank you for buying food from a ripped off McDonald's!")
    print("--------------------------------------------")

#now, let's call the receipt
create_receipt()
