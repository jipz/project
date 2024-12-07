class Item:
  def __init__(self, name, price):
    self.name = name
    self.price = price


class Cart:
  def __init__(self, name):
    self.name = name
    self.cargo = []
  
  def put_in(self, item):
    self.cargo.append(item)
    
  def show_item(self):
    return self.cargo
  
  def show_price(self):
    total_price = 0
    for item in self.cargo:
      total_price += item.price
    
    return total_price

if __name__ == "__main__":
  cartA = Cart("A")
  itemA = Item("a", 150)
  itemB = Item("b", 310)
  cartA.put_in(itemA)
  cartA.put_in(itemB)
  print(cartA.show_price())
