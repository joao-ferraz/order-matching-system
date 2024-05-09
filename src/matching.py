from order import *

def findMatch(order: Order, orderBook: list):

    if order.price >= orderBook[0].price:
        #match qnt
        orderBook[0].qnt = 0
    else:
        return -1
