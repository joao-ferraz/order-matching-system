# order-matching-system

This is a simplified implementation of an order matching system.

## Overview

This project simulates an exchange with only one asset and two order types: limit and market. The orders and other available commands are typed in the terminal, following a specified sintax. The order book follows a price-time priority, in wich orders with updated prices also lose time priority. When the market is closed the unfufilled sell and buy order books are printed.

## Usage

run the project in the "src" file with the command:

```bash
python3 ./main.py
```

there are 5 available commands:

#### limit
Limit orders are executed instantly if there is a corresponding match on the order book, otherwise they are added to the queue.

limit syntax: limit side price qty

#### market
market orders are executed instantly if there is a corresponding match, otherwise the system writes a message "No Liquidity"

market sintax: market side qty

#### cancel

To cancel orders use the order_id provided after creating an order, cancelled orders will be removed from the order book.

calcel sintax: cancel order order_id

#### update

Update command allows to edit an orders price or qty, or both. Only orders with price changes will lose time priority on the order book and receive a new id. Price changes that enable a trade will cause the edited order to be executed.

update sintax: update order order_id att1 att2(optional)

att1 and att2 can be "price" or "qty"

a message on the terminal will request the new value to be assigned.

#### end
 "Closes the market", prints the sell and buy orderbooks, and finishes the program