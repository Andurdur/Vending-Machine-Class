'''
Andy Vo
Assignment 10.1
This program will imitate a vending machine.
'''
#list and dictionary for the items in the vending machine
vendingmachine_list = ['Coke', 'Pepsi', 'Sprite', 'Lays', 'Cheetos', 'Funyuns', 'M&Ms', 'Reeses Peanut Butter Cups', 'Gummy Worms']
vendingmachine_dict = {'Coke':0.65, 'Pepsi':0.65, 'Sprite':0.65, 'Lays':0.50, 'Cheetos':0.50, 'Funyuns':0.50, 'M&Ms':1, 'Reeses Peanut Butter Cups':1.10, 'Gummy Worms':1.10}

#This class represents a small vending machine
class VendingMachine:
    #class variable
    coin_type = 'Quarters only'
    def __init__(self, item_name_list, coin_amount):
        #set the list of items and quarter coins amount based on constructor arguments
        #all data variables are private
        self.__item_name = item_name_list
        self.__coin_amount = coin_amount
        #set cost and balance to 0
        self.__cost = 0
        self.__balance = 0
    #method that calculates the total cost of the item list
    def totalcost(self):
        #for loop that iterates through each item in the list
        for item in self.__item_name:
            #looks for the price of each item in the dictionary and adds to the cost data variable
            self.__cost += vendingmachine_dict[item]
        #returns total price
        return self.__cost
    #method that calculates the amount of quarters inserted
    def balance(self):
        #adds the total balance of quarters into the balance data variable
        self.__balance += (self.__coin_amount * .25)
        #returns balance
        return self.__balance
    #method that shows the whole menu of items in the vending machine with prices
    def menu(self):
        #welcome message
        print("Welcome to the Vending Machine")
        #display each item w/ price
        print(f'Current available items: {vendingmachine_dict}')
    #set method for items
    def set_item(self, item_name):
        #for loop to iterate through each item in the list
        for item in item_name:
            #if the item is in the vending machine set the item list as the item list data variable
            if item in vendingmachine_list:
                self.__item_name = item_name
            #else raise a ValueError with an error message
            else:
                raise ValueError("Invalid item name. Item must be in the vending machine.")
    #set method for the amount of quarters
    def set_coinamount(self, coin_amount):
        #if amount of quarters are less than 0, ValueError raises and error message
        if coin_amount < 0:
            raise ValueError("Balance cannot be a negative number.")
        #else the amount of quarters is set to the data variable
        else:
            self.__coin_amount = coin_amount
    #get method for items
    def get_item(self):
        #returns the list of items
        return self.__item_name
    #get method for amount of quarters
    def get_coin_amount(self):
        #returns the amount of quarters
        return self.__coin_amount

#Main Function
def main():
    #Input arguments for the class
    item_names = ['Coke', 'Lays', 'Gummy Worms']
    coin_amount = 3
    #set class to variable
    snack_purchase = VendingMachine(item_names, coin_amount)
    #if statements using the set methods to raise errors and stop once errors are raised
    if snack_purchase.set_item(item_names) == ValueError:
        snack_purchase.set_item(item_names)
    elif snack_purchase.set_coinamount(coin_amount) == ValueError:
        snack_purchase.set_coinamount(coin_amount)
    #pass if no errors are raised
    else:
        pass
    #displays the selection of items w/ prices
    snack_purchase.menu()
    #prints the type of coins allowed to be inserted in the machine
    print(snack_purchase.coin_type)
    #prints message for the amount of inserted quarters and item list using get methods
    print(f'Inserted {snack_purchase.get_coin_amount()} quarters')
    print(f'Selected: {snack_purchase.get_item()}')
    #calculates the remaining balance after transaction
    remaining_balance = snack_purchase.balance() - snack_purchase.totalcost()
    #if remaining balance is less than 0, message saying insufficent amount of funds will show
    if remaining_balance < 0:
        print('You do not have a sufficent amount of quarters to purchase these items.')
    #else will print the items purchased using the get method for items and shows the remaining balance 
    else:
        print(f'Items Purchased: {snack_purchase.get_item()}.\nRemaining Balance: ${remaining_balance:.2f}.')



if __name__ == '__main__':
    main()



