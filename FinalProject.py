#Vignesh Peddi
#PROMPT: Create a stock trading program
import pandas as pd#import libraries
import yfinance as yf
import yahoofinancials
import requests
from yahoo_fin import stock_info as si
from alpha_vantage.timeseries import TimeSeries
from os import system, name   
# import sleep to show output for some time period 
from time import sleep   
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
def menu():
  print("\n1. Buy/Sell Stocks\n2. Analyze Stocks\n3. Check Balance\n")
  n = input("Choose option: ")
  return n
def searching(x,y):
  returner = 'n'
  search = x

  found = -1  #starting with a value of -1 because INDEX values are not negative
            #will hold searched-for item's location if found; will stay negative if not found

  list_length = len(y) #len() is the length function; it finds the number of items in the list passed to it

  for i in range(0, list_length):

    #this for loop allows us to look through an entire list, from top to bottom

     #updating the search loop counter


    if search == y[i]:

        #SEARCHED ITEM HAS BEEN FOUND when above if condition is TRUE
        #if statement runs the actual "search"
        #compares what you are looking for (search) against every possible option (each value stored in the list ou are searching through)
    
        found = i   #the searched for item is found at this location point along with the rest of the data from the                 original record

  if found >= 0: #item has been found

    #when if statement is TRUE we've found what we're looking for
    returner = 'y'
  return returner, found
def searching1(x, y, z):
  min = 0
  max = z
  search = input("Stock Name")
  guess = int((min+max)/2)
  while min < max and search != x[guess]:
    if search < name[guess]: #what we're looking for has a value less than the middle point        #revalue max to have a cap at the middle point        #cutting out top (higher value) half of list        
      max = guess - 1    
    else: #what we're looking for has a value greater than the middle point        #revalue min to have a base/start at the middle point         #cutting out the bottom (lower value) half of list        
      min = guess + 1

#FUNCTIONS---------------------------------------------
def swap(n, j):    
  t = n[j]    
  n[j]= n[j + 1]    
  n[j + 1] = t
def wlmenu():
  print("\n\nMENU\n1. Stock Info\n2. Stock Price\n3. Reccomendations\n4. Actions")
  n = input("Choose option: ")
  return n
print("\n\nWelcome to Vignesh's Paper Trading Program!\n\n")
print("In this program you will be given $1000 of fake money to spend on stocks to test your investing skills. You will be able to use a multitude of analyzing tools to determine the best stocks to buy!")
stockown = []#names of the stock you own
accountval = 1000#starting amount of money
option = menu()#prompt user with a menu
while True:
  clear()
  while option == "1":
    clear()
    stock = input("Would you like to buy or sell: ")
    clear()
    if stock == "buy":
      clear()
      stkname = input("Stock Name: ")
      clear()
      stockown.append(stkname)
      stkprice = si.get_live_price(stkname)#get price of stock
      accountval -= stkprice#subtract stock price from account value
      if accountval < 0:
        accountval += stkprice
        print("YOU DONT HAVE ENOUGH MONEY!")
      else:
        print("You have just bought",stkname,"for $",int(stkprice),"\nACCOUNT BALNCE: $",int(accountval))
      sleep(3)
      clear()
      option = menu()
    if stock == "sell":
      clear()
      stkname = input("Stock Name: ")
      clear()
      returnedvalue = searching(stkname, stockown)[0]
      if returnedvalue == 'y':
        stkprice = si.get_live_price(stkname)#get price of stock
        stockown[searching(stkname, stockown)[1]] = "null"
        accountval += stkprice
        print("You have just sold",stkname,"for $",int(stkprice),"\nACCOUNT BALNCE: $",int(accountval))
        sleep(3)
        clear()
        option = menu()
  while option == "2":
    number = wlmenu()
    if number == '1':
      clear()
      ticker = input("Stock Name: ")
      clear()
 
      keys = 'M75PQCYU3GJYFEFC'

      time = TimeSeries(key=keys, output_format='pandas')
      data = time.get_intraday(symbol=ticker, interval = '60min', outputsize='compact')#get data of the stock

      print(ticker)
      print(data)
      sleep(3)
      clear()
      option = menu()
    if number == '2':
      clear()
      ticker = input("Stock Name: ")
      stkprice = si.get_live_price(ticker)
      print(ticker,"PRICE: $", int(stkprice))
      sleep(3)
      clear()
      option = menu()
  while option == '3':
    clear()
    print("ACCOUNT BALANCE: $",accountval)
    sleep(3)
    clear()
    option = menu()
    clear()



