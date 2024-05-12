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


def validMarketOrder(userInput: list):
    if len(userInput) != 3:
        print("market orders should have 2 parameters: market side qnt")
    else:
        orderType, side, qnt = userInput

        if isValidEnum(Side, side):            
            try:
                qnt = int(qnt)
            except:
                print("qnt parameter should be an integer")
                return None
            
            return orderType, side, qnt
        else:
            print("Side value should be buy or sell")
            return None
        
def validCancel(userInput: list):
    if len(userInput) != 3:
        print("cancel command should be: cancel order order_id")
    else:
        _, orderStr, id = userInput

        if orderStr != "order":
            print("cancel command should be: cancel order order_id")
        else:
            try:
                id = int(id)
            except:
                print("order_id should be an integer")
                return None
            return id

def validUpdate(userInput: list):
    l = len(userInput)
    if l < 4 or l > 5:
        print("update command should be: update order order_id price qty")
    else:

        modify = []*(l-3)
        _, orderStr, id, *_ = userInput

        modify = userInput[3:]

        if orderStr != "order":
            print("update command should be: update order order_id price qty")
        else:
            try:
                id = int(id)
            except:
                print("order_id should be an integer")
                return None
            
            for att in modify:
                if att != "price" and att != "qty":
                    print("chose to update price, qty or both")
                    return None
                
            return id, modify
        
def noMatch():
    print("Not a valid command. Valid commands are: limit, market, end")