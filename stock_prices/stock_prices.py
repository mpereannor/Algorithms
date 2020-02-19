#!/usr/bin/python

import argparse

'''
For this problem, we essentially want to find the maximum difference between the smallest and largest prices in the list of prices, but we also have to make sure that the max profit is computed by subtracting some price by another price that comes _before_ it; it can't come after it in the list of prices. 

 So what if we kept track of the `current_min_price_so_far` and the `max_profit_so_far`? 
'''
 
'''
 1. Understand
 -What types of input can we expect? 
  -valid
    -integer
  -invalid
    -decimal
    -string
    -char
  -edge case
    -netative numbers
    
 2. Plan
  -Iterative or Recursive Approach? 
    -first pass 
      -recursive
    -second pass  
      -iterative
      
 3. Execute
 
 4. Revise
'''
 
def find_max_profit(prices): #iteration 
  
  current_profit = prices[1] - prices[0]
  for i in range(0, len(prices) - 1):
    for j in range(1, len(prices) - 1):
      if j > i: 
        if prices[j] - prices[i] > current_profit: 
              current_profit = prices[j] - prices[i]
              
  return current_profit
  
  #find current_profit by subtracting index[0] from index[1]
  #loop through array with current_index[i] ==> starts from len(arr) - 1 and do a nested loop inside the array  with index[j] ==> starts from one len(arr)
  # if j > i  
  # if  sub index[j] from index[i] > current profit
  # then current_profit == index[j] - index[i]
  
  #return current_profit 
  
  # 3. plan
  #recursion
    #pseudo- code
    #base case
    #while there's a buy at index[0] greater than 0 
    
    #execute 
       #loop through the array of prices and find the highest price 
    
        #at index[highest_price] split array into two - with highest_price as final length of array

       
    #loop through array containing index[highest_index] and find the lowest price 
    
    # while len(prices[0]) < 0:
    #   return price[0]
      # for i in range(len(prices)):
      #   highest_price = i
    
      #   l1 = prices[:len(prices[hignest_price])]
    
        # for j in range(len(l1)):
        #   l2 = prices()
    





































if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))