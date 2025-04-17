import pandas as pd

n = int(input("enter n"))
asking_prices = pd.Series([int(input("enter asking price")) for i in range(n)])
fair_prices = pd.Series([int(input("enter fair price")) for i in range(n)])

good_deal = asking_prices[asking_prices < fair_prices].index.tolist()

print(good_deal)
