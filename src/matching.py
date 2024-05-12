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

def cancelOrder(orderId, buyOrderBook, sellOrderBook):

    # O(N) cancel

    for heapIndex, order in enumerate(buyOrderBook):
        if orderId == order.id:
            buyOrderBook.pop(heapIndex)
            buyOrderBook.sort()
            print("Order cancelled")
            return

    for heapIndex, order in enumerate(sellOrderBook):
        if orderId == order.id:
            sellOrderBook.pop(heapIndex)
            sellOrderBook.sort()
            print("Order cancelled")
            return
        
    print(f"No order with id: {orderId}")

