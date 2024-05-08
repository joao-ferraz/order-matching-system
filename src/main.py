from order import *


userInput = input()

if userInput.strip():
    userCommand = userInput.split()
else:
    userCommand = "No words in the input"



while userCommand[0] != "end":
    #print("O comando é: " + userCommand[0])

    userInput = input()

    if userInput.strip():
        userCommand = userInput.split()

        match userCommand[0]:

            case "limit":

                # sintax comando limit
                if len(userCommand) != 4:
                    print("limit orders should have 3 parameters: limit side price qnt")
                else:
                    orderType, side, price, qnt = userCommand

                    if isValidEnum(Side, side):
                        print("ok side")
                    else:
                        print("Side value should be buy or sell")

                    # checa preço e qnt
                    try:
                        price = float(price)
                    except:
                        print("price parameter should be a number")
                    
                    try:
                        qnt = int(qnt)
                    except:
                        print("qnt parameter should be an integer")

                    
                    newOrder = Order(orderType, side, qnt, price)
                    print(vars(newOrder))

                    
                
            case "market":
                print(OrderType.MARKET)
        
    else:
        userCommand = "No words in the input"




