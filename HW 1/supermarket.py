"""Name: Fan Zhang
Penn ID: 70912620
Statement of work: I worked alone without help on this homework"""
# import the random module
# use "winnings = random.randint(2, 10)" to generate a random int from 2 - 10 and store in a variable "winnings"
import random

# unit price of a lottery ticket
constant_lottery_unit_price = 2

# unit price of an apple
constant_apple_unit_price = .99

# unit price of a can of beans
constant_canned_beans_unit_price = 1.58

# unit price of a soda
constant_soda_unit_price = 1.23

# the user has initial $5 for shopping
money = 5

# the user has spent $0 initially
money_spent = 0

# the amounts of lottery tickets, apples, cans of beans, and sodas the user has purchased
lottery_amount, apple_amount, canned_beans_amount, soda_amount = 0, 0, 0, 0

# print a welcome message to the user along with a list of products and their unit prices
print ("Welcome to the supermarket!  Here's what we have in stock:")
print ("- Lottery tickets cost $2 each")
print ("- Apples cost $0.99 each")
print ("- Cans of beans cost $1.58 each")
print ("- Sodas cost $1.23 each")

#Tell the user how much money they have available and ask if they want to purchase a lottery ticket
print ("Your currently available balance is $5.")
lottery_ticket_decision = input("First, would you like to purchase a $2 lottery ticket for a chance at winning $2-$10? Please enter y or n")

#If the user inputs "y" or "Y", process a lottery ticket purchase
lottery_win_probability = random.randint(0,2)
amount_of_lottery_tickets = 0
if lottery_ticket_decision == "y" or lottery_ticket_decision == "Y":
    #if the user wins, calculate their winnings
    if lottery_win_probability == 0:
        winnings = random.randint(2, 10)
        #deduct the $2 the user spent on the lottery ticket and increase the lottery tickets purchased by 1
        lottery_amount = lottery_amount + 1
        money = money - constant_lottery_unit_price * lottery_amount + winnings
        #print a congratulatory message to the user telling them the value of the lottery ticket if the user won the lottery
        print ("Congratulations! You won $", winnings, "!")
    #if the user loses, print a message informing them that they did not win the lottery, and deduct the $2 the user spent on the lottery ticket from their available money and increase the amount of lottery tickets purchased by 1
    else:
        #print a message informing them that they did not win the lottery
        print ("Sorry, you did not win the lottery.")
        #deduct the $2 the user spent on the lottery ticket 
        money = money - 2
        #increase the lottery tickets purchased by 1
        amount_of_lottery_tickets = amount_of_lottery_tickets + 1
        winnings = 0
        lottery_amount = lottery_amount + 1
        
else:
    #if the user inputs "n" or "N", print a message saying that no lottery tickets were purchased and move on
    if lottery_ticket_decision == "n" or lottery_ticket_decision == "N":
        winnings = 0
        print ("No lottery tickets were purchased.")
        
#Tell the user how much money they have available
print ("Your current available balance is $", money,".")

#ask if the user wants to purchase apples
apple_purchase_decision = input("Would you like to purchase apples? y or n")
#if the user inputs "y" or "Y", process an apple purchase
if apple_purchase_decision == "y" or apple_purchase_decision == "Y":
    #ask how many apples the user wants to buy
    apple_purchase_amount = input("How many apples would you like to purchase?")
    #if the user entered valid integer input
    if (apple_purchase_amount.isnumeric()):
        #cast the input to an integer
        apple_purchase_amount = int(apple_purchase_amount)
        #calculate the money the user will need to pay
        total_price_apple = round((apple_purchase_amount * constant_apple_unit_price),2)
        #print the amount the user wants to purchase and how much it will cost
        print("You want to buy ", apple_purchase_amount, "apple(s). This will cost $", total_price_apple, ".")
        #if the user does not have enough money to pay, print "Not enough money" and move on
        if total_price_apple > money:
                print("Not enough money. No apples purchased.")
        #if the user has enough money, add the number of apple(s) purchased to the variable reprensenting the total amount of apples that the user has purchased and decrease the money that the user has left
        else:
                apple_amount = apple_amount+apple_purchase_amount
                money = round((money - total_price_apple),2)             
    else:
        #catch the error if the input cannot be cast in an integer and print a friendly message reminding the user that only numerical values are accpeted and move on
        print("Sorry, only numerical values are accepted. No apples selected.")
            
else:
    #if the user inputs "n" or "N", print a message saying that no apples were purchased and move on
    if apple_purchase_decision == "n" or apple_purchase_decision == "N":
        print ("No apples were purchased.")
        
#Tell the user how much money they have available
print ("Your current available balance is $", money,".")

#ask if the user wants to purchase canned beans
canned_beans_purchase_decision = input("Would you like to purchase canned beans? y or n")
#if the user inputs "y" or "Y", process a bean purchase
if canned_beans_purchase_decision == "y" or canned_beans_purchase_decision == "Y":
    #ask how many cans of beans the user wants to buy
    canned_beans_purchase_amount = input("How many cans of beans would you like to purchase?")
    #if the user entered valid integer input
    if (canned_beans_purchase_amount.isnumeric()):
        #cast the input to an integer
        canned_beans_purchase_amount = int(canned_beans_purchase_amount)
        #calculate the money the user will need to pay
        total_price_beans = round((canned_beans_purchase_amount * constant_canned_beans_unit_price),2)
        #print the amount the user wants to purchase and how much it will cost
        print("You want to buy ", canned_beans_purchase_amount, "can(s) of beans. This will cost $", total_price_beans, ".")
        #if the user does not have enough money to pay, print "Not enough money" and move on
        if total_price_beans > money:
                print("Not enough money. No cans of beans purchased.")
        #if the user has enough money, add the number of canned beans purchased to the variable reprensenting the total amount of canned beans that the user has purchased and decrease the money that the user has left
        else:
                canned_beans_amount = canned_beans_amount + canned_beans_purchase_amount
                money = round((money - total_price_beans),2)             
    else:
        #catch the error if the input cannot be cast in an integer and print a friendly message reminding the user that only numerical values are accpeted and move on
        print("Sorry, only numerical values are accepted. No cans of beans selected.")
            
else:
    #if the user inputs "n" or "N", print a message saying that no apples were purchased and move on
    if canned_beans_purchase_decision == "n" or canned_beans_purchase_decision == "N":
        print ("No canned beans were purchased.")
        
#Tell the user how much money they have available
print ("Your current available balance is $", money,".") 

#ask if the user wants to purchase soda
soda_purchase_decision = input("Would you like to purchase soda? y or n")
#if the user inputs "y" or "Y", process a soda purchase
if soda_purchase_decision == "y" or soda_purchase_decision == "Y":
    #ask how many soda the user wants to buy
    soda_purchase_amount = input("How many soda would you like to purchase?")
    #if the user entered valid integer input
    if (soda_purchase_amount.isnumeric()):
        #cast the input to an integer
        soda_purchase_amount = int(soda_purchase_amount)
        #calculate the money the user will need to pay
        total_price_soda = round((soda_purchase_amount * constant_soda_unit_price),2)
        #print the amount the user wants to purchase and how much it will cost
        print("You want to buy ", soda_purchase_amount, "sodas. This will cost $", total_price_soda, ".")
        #if the user does not have enough money to pay, print "Not enough money" and move on
        if total_price_soda > money:
                print("Not enough money. No sodas purchased.")
        #if the user has enough money, add the number of sodas purchased to the variable reprensenting the total amount of sodas that the user has purchased and decrease the money that the user has left
        else:
                soda_amount = soda_amount + soda_purchase_amount
                money = round((money - total_price_soda),2)           
    else:
        #catch the error if the input cannot be cast in an integer and print a friendly message reminding the user that only numerical values are accpeted and move on
        print("Sorry, only numerical values are accepted. No sodas selected.")
            
else:
    #if the user inputs "n" or "N", print a message saying that no apples were purchased and move on
    if soda_purchase_decision == "n" or soda_purchase_decision == "N":
        print ("No sodas were purchased.")
        
#Tell the user how much money they have available
print ("Your current available balance is $", money,".")
#tell the user the number of lottery tickets purchased, amount of lottery winnings, numbers of apples purchased, numbers of cans of beans purchased and numbers of sodas purchased, and a goodbye message
print("Lottery ticket(s) purchased:",lottery_amount)
print("Lottery winnings: $", winnings)
print("Apple(s) purchased:", apple_amount)
print("Can(s) of beans purchased:", canned_beans_amount)
print("Soda(s) purchased:", soda_amount)
print("Thank you for shopping with us. Good bye!")
        
        

    
    

