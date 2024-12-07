from src.shopping import Item, Cart
import pandas as pd


cartA = Cart("A")
itemA = Item("a", 10)
itemB = Item("b", 310)
cartA.put_in(itemA)
cartA.put_in(itemB)
print(cartA.show_price())

data = {
    "A": [10, 40, 50],
    "B": [30, 20, 60],
    "C": [20, 80, 10],
    "D": ["X", "Y", "Z"]  
}

df = pd.DataFrame(data)
print(df)