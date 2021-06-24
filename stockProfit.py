
test = [1, 2, 3, 5, 10, 4, 14, 0]

def maxProfit(stockPriceList) -> int:

    maxProfit = 0
    
    for i in range(len(stockPriceList)):
        
        buy = stockPriceList[i]

        for j in range(len(stockPriceList[i+1:])):

            sell = stockPriceList[i+j+1]

            if -buy + sell > maxProfit:
                maxProfit = -buy + sell

    return maxProfit


print(maxProfit(test))




