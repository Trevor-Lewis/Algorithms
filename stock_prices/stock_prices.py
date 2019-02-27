#!/usr/bin/python

import argparse

def find_max_profit(prices):
    # set min price to 0 index
    minPrice = prices[0]
    # takes index 1 minus minPrice and sets maxProfit with that value
    maxProfit = prices[1] - minPrice
    # loop through each element in array
    for currentPrice in prices[1:]:
        # populate maxProfit using max() to calculate max 
        maxProfit = max(currentPrice - minPrice, maxProfit)
        # populate minPrice by using min() to calculate min
        minPrice = min(currentPrice, minPrice)

    return maxProfit

# print(find_max_profit([1050, 270, 1540, 3800, 2]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))