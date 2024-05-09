from order  import *

def validLimitOrder(userInput: list):

    if len(userInput) != 4:
        print("limit orders should have 3 parameters: limit side price qnt")
    else:
        orderType, side, price, qnt = userInput

        if isValidEnum(Side, side):
            # checa preço e qnt
            try:
                price = float(price)
            except:
                print("price parameter should be a number")
                return None
            
            try:
                qnt = int(qnt)
            except:
                print("qnt parameter should be an integer")
                return None
            
            return orderType, side, price, qnt

        else:
            print("Side value should be buy or sell")
            return None
       