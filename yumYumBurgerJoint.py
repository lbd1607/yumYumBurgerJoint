#Laura Davis
#13 March 2016
#Ch 5 Programming Challenge: Yum Yum Burger Joint
#This program will calculate the cost of purchasing a meal
#at Yum Yum Burger Joint. The program will allow the user to 
#select items from the menu then it will calculate the total
#and add the 6% sales tax. It will print the customer receipt
#to the screen.

#This is the main function.
def main(): 
	print "Welcome to Yum Yum Burger Joint! May I take your order?"
	print 
#Declare variables	
	endProgram = "no"
	endOrder = "no"	
	totalBurger = 0
	burgerCount = 0
	totalFry = 0
	fryCount = 0
	totalSoda = 0
	sodaCount = 0
	total = 0
	option = 0

	while endProgram == "no":
#Reset variables
		endOrder = "no"
		totalBurger = 0
		totalFry = 0
		totalSoda = 0
		total = 0
		
#Order loop
		while endOrder == "no":
			print "Enter 1 for Yum Yum Burger"
			print "Enter 2 for Grease Yum Fries"
			print "Enter 3 for Soda Yum"
			option = input("Enter now --> ")
			if option == 1:
				totalBurger = getBurger(totalBurger)
			elif option == 2:
				totalFry = getFry(totalFry)
			else:
				option == 3
				totalSoda = getSoda(totalSoda)
			endOrder = raw_input("Do you want to end your order? (Enter no to add more items) --> ")
			print 
		total = calcTotal(totalBurger, totalFry, totalSoda, total)
		printReceipt(total)			
		endProgram = raw_input("Do you want to end the program? (Enter no to process a new order) --> ")
		print 
		
#This function will calculate the total price for the quantity of burgers ordered.
def getBurger(totalBurger):
	burgerCount = input("Enter the number of burgers you want --> ")
	totalBurger = totalBurger + burgerCount * .99
	return totalBurger
#This function will calculate the total price for the quantity of fries ordered.
def getFry(totalFry):
	fryCount = input("Enter the number of fries you want --> ")
	totalFry = totalFry + fryCount * .79
	return totalFry
#This function will calculate the total price for the quantity of sodas ordered.
def getSoda(totalSoda):
	sodaCount = input("Enter the number of sodas you want --> ")
	totalSoda = totalSoda + sodaCount * 1.09
	return totalSoda
#This function will calculate the total of the orders.
def calcTotal(totalBurger, totalFry, totalSoda, total):
	subtotal = totalBurger + totalFry + totalSoda
	tax = subtotal * .06
	total = subtotal + tax
	return total
#This module prints the customer receipt. 
def printReceipt(total):
	print "The total price is $", total
	
#calls main
main()	
