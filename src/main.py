from order import *
from heapq import *
from validate import *

userInput = input()

if userInput.strip():
    userCommand = userInput.split()
else:
    userCommand = "No words in the input"

sellOrderBook = []
buyOrderBook = []


while userCommand[0] != "end":

    userInput = input()

    if userInput.strip():
        userCommand = userInput.split()

        match userCommand[0]:

            case "limit":

                try:
                    orderType, side, price, qnt = validLimitOrder(userCommand)
                except:
                    continue
       
                newOrder = Order(orderType, side, qnt, price)
        
                if newOrder.side == Side.BUY.value:
                    newOrder.invertPrice()
                    heappush(buyOrderBook, newOrder)
                else:
                    heappush(sellOrderBook, newOrder)

                #tries to match
                
                # add to order book if match not found
                                   
            case "market":
                print(OrderType.MARKET)
        
    else:
        userCommand = "No words in the input"


for i in range(len(buyOrderBook)):
    print(heappop(buyOrderBook))


