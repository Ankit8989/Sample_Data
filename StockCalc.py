import numpy as np

stock = np.array(['TCS', 'SBI', 'TCS', 'Reliance', 'SBI', 'Reliance', 'SBI'])
qnt = np.array([12, 10, 8, 15, 5, 10, 20])
stock_purchase_price =  np.array([2000, 280, 2100, 1250, 300, 1200, 290])

def func1():
    res =  qnt * stock_purchase_price
    return res.sum()

def func2():
    val = 0
    for i in range(len(stock)):
        if stock[i] == 'SBI':
            val += (qnt[i] * stock_purchase_price[i])
    return val


def func3():
    tot_sbi_stock_price = problem2(stock, qnt, stockPurchasePrice)
    total_qnt = 0
    total_stock = 0
    # for i in range(len(stock)):
    #     if stock[i] == 'SBI':
            total_qnt += (qnt[i])
            total_stock += (qnt[i] * stock_purchase_price[i])
    resp = total_stock / total_qnt
    return resp


def func4():
    amount =  qnt * stock_purchase_price
    max_val = amount.max()
    for i in range(len(amount)):
        if amount[i] == max_val:
            return stock[i]

def func5(new_stocks):
    res = dict()
    for key, val in new_stocks.items():
        total_qnt, total_stock = 0, 0
        for i in range(len(stock)):
            if stock[i] == key:
                total_qnt += (qnt[i])
                total_stock += qnt[i] * stock_purchase_price[i]
        res[key] = (val * total_qnt) - total_stock
    return res



print("total amount invested in the stocks- ", func1())

print("amount is invested in sbi- ", func2())

print("the average of stock price of sbi- ", func3())

print("stock maximum amount is invested- ", func4())

new_stocks = {'TCS': 2300, 'SBI': 350, 'Reliance': 1400}
print("total profit with updated stocks- ", func5(new_stocks))

