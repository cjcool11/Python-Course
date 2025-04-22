def calculateprofits(arr,array_size):
    profit = 0
    for i in range(1,array_size):
        if arr[i] > arr[i-1]:
            profit += arr[i] - arr[i-1]
        return profit
    
stock_prices = [143,567,768,987]
stock_price_length = len(stock_prices)
print("Max profit: ",calculateprofits(stock_prices,stock_price_length))