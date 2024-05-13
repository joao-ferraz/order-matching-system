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
        heapify(buyOrderBook)
        print("Order cancelled")

    elif side == Side.SELL:
        sellOrderBook.pop(heapIndex)
        heapify(sellOrderBook)
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
    newPrice = None
    for att in attToModify:
        if att == "price":
            print("Type new order price:", end=' ', flush=True)
            newPrice = float(input())
            order.price = newPrice
        else:
            print("Type new order qty:", end=' ', flush=True)
            newqnt = int(input())
            order.qnt = newqnt

    if newPrice == order.price:
        newOrder = Order(order.type, order.side, order.qnt, order.price, False)

        if side == Side.BUY:
            buyOrderBook.pop(heapIndex)
            heapify(buyOrderBook)
            findMatch(newOrder,sellOrderBook, buyOrderBook)
        else:
            sellOrderBook.pop(heapIndex)
            heapify(sellOrderBook)
            newOrder.invertPrice()
            findMatch(newOrder,buyOrderBook, sellOrderBook)

        print(f"Order updated, new id: {newOrder.id}")
    else:
        print("Order updated")


def findOrder(orderId, buyOrderBook, sellOrderBook):

    for heapIndex, order in enumerate(buyOrderBook):
        if orderId == order.id:
            return heapIndex, Side.BUY

    for heapIndex, order in enumerate(sellOrderBook):
        if orderId == order.id:
            return heapIndex, Side.SELL
    
    return -1, None
