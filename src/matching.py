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
    heapIndex, side = findOrder(orderId, buyOrderBook, sellOrderBook)

    if side == Side.BUY:
        buyOrderBook.pop(heapIndex)
        buyOrderBook.sort()
        print("Order cancelled")

    elif side == Side.SELL:
        sellOrderBook.pop(heapIndex)
        sellOrderBook.sort()
        print("Order cancelled")
    else:
        print(f"No order with id: {orderId}")

def findUpdateOrder(orderId, buyOrderBook, sellOrderBook, attToModify):

    heapIndex, side = findOrder(orderId, buyOrderBook, sellOrderBook)

    if side == Side.BUY:
        order = buyOrderBook[heapIndex]
    elif side == Side.SELL:
        order = sellOrderBook[heapIndex]
    else:
        print(f"No order with id: {orderId}")
        return
    
    for att in attToModify:
        if att == "price":
            print("Type new order price:", end=' ')
            newPrice = float(input())
            order.price = newPrice

            if side == Side.BUY:
                buyOrderBook.sort()
            else:
                sellOrderBook.sort()
        else:
            print("Type new order qty:", end=' ')
            newqnt = int(input())
            order.qnt = newqnt

    print("Order updated")

def findOrder(orderId, buyOrderBook, sellOrderBook):

    for heapIndex, order in enumerate(buyOrderBook):
        if orderId == order.id:
            return heapIndex, Side.BUY

    for heapIndex, order in enumerate(sellOrderBook):
        if orderId == order.id:
            return heapIndex, Side.SELL
    
    return -1, None
