from order import *
from heapq import *

def findMatch(order: Order, checkOrderBook: list, addOrderBook: list):

    if checkOrderBook and order.price >= checkOrderBook[0].price:
        bestOrder = checkOrderBook[0]

        if order.qnt > bestOrder.qnt:

            order.qnt = order.qnt - bestOrder.qnt
            print(f"Trade, price: {abs(bestOrder.price)}, qty: {bestOrder.qnt}")
            heappop(checkOrderBook)
            findMatch(order, checkOrderBook, addOrderBook)

        else:
            bestOrder.qnt = bestOrder.qnt - order.qnt
            if bestOrder.qnt == 0:
                print(f"Trade, price: {abs(bestOrder.price)}, qty: {order.qnt}")
                heappop(checkOrderBook)
            else:
                print(f"Trade, price: {abs(bestOrder.price)}, qty: {order.qnt}")
    else:
        order.invertPrice()
        heappush(addOrderBook, order)

        
def matchMarketOrder(order: Order, checkOrderBook: list):

    if checkOrderBook:
        bestOrder = checkOrderBook[0]
        if order.qnt > bestOrder.qnt:
            order.qnt = order.qnt - bestOrder.qnt
            print(f"Trade, price: {abs(bestOrder.price)}, qty: {bestOrder.qnt}")
            heappop(checkOrderBook)
            matchMarketOrder(order, checkOrderBook)

        else:
            bestOrder.qnt = bestOrder.qnt - order.qnt
            if bestOrder.qnt == 0:
                print(f"Trade, price: {abs(bestOrder.price)}, qty: {order.qnt}")
                heappop(checkOrderBook)
            else:
                print(f"Trade, price: {abs(bestOrder.price)}, qty: {order.qnt}")
    else:
        print("No Liquidity")