import csv
from random import randint

from typing import List, Tuple

WALLET = 2000

class Item:
    def __init__(self, name: str, price: int, one_per_n: int):
        self.name = name
        self.price = price
        self.one_per_n = one_per_n
    
class Shop:
    def __init__(self, items: List[Item]):
        self.items = items
    
    def sell(self, shopping_list: List[int]) -> Tuple[int]:
        if len(shopping_list) != len(self.items):
            return [-1, 0]
        sum_price = 0
        sum_prize = 0
        for n_item, item in zip(shopping_list, self.items):
            sum_price += n_item*item.price
            n_hit = 0
            for i in range(n_item):
                is_hit = randint(1, item.one_per_n) == item.one_per_n
                if is_hit:
                    n_hit += 1
            sum_prize += item.price * n_hit
        if sum_price > WALLET:
            return [0, -1]
        return sum_price, sum_prize
    
if __name__ == "__main__":
    items = [
        Item('A', 125, 11),
        Item('B', 80, 8),
        Item('C', 50, 5),
        Item('D', 1000, 100),
        Item('E', 150, 14),
        Item('F', 500, 33)
    ]
    
    shop = Shop(items)

    with open('./shopping_list.csv') as f:
        shopping_lists = [[int(e) for e in line.split(',')] for line in f.readlines()]
    
    with open('./results.csv', 'w') as f:
        f.write('合計,購入,当たり\n')
        for i, shopping_list in enumerate(shopping_lists):
            sum_price, sum_prize = shop.sell(shopping_list)
            if sum_price == -1:
                print(f'{i+1}: 商品種類の数が足りません')
                continue
            if sum_prize == -1:
                print(f'{i+1}: 購入金額が{WALLET}円を超えています')
                continue
            all_item_price = sum_price + sum_prize
            print(f'{i+1}: {all_item_price}円 (購入: {sum_price}円, 当たり: {sum_prize}円)')
            f.write(f'{all_item_price},{sum_price},{sum_prize}\n')



        
            

        
        
        
