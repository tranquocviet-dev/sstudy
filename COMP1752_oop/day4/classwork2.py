from classwork1 import Item

class Inventory:
    def __init__(self, name, *item_list:Item):
        item_dict = {}
        for item in item_dict:
            item_dict[item.proid] = item
        self.__item_dict = item_dict
        self.name = name

    def add(self, new:Item):
        if new.proid in self.__item_dict:
            print('Item already exist')
            return
        else:
            self.__item_dict[new.proid] = new
            return

    def remove(self, rem:Item):
        if rem.proid not in self.__item_dict:
            print('Item doesnt exist')
            return
        else:
            del self.__item_dict[rem.proid]
            return

    def add_quantity(self, item_id:int, amount:int):
        if item_id not in self.__item_dict:
            print('id not found')
            return
        elif amount < 0:
            print('value cant be below 0')
            return
        else:
            self.__item_dict[item_id].add_amount(amount)

    def decrease_quantity(self, item_id:int, amount:int):
        if item_id not in self.__item_dict:
            print('id not found')
            return
        elif amount < 0:
            print('value cant be below 0')
            return
        elif amount >= self.__item_dict[item_id].price:
            print('value too high')
            return
        else:
            self.__item_dict[item_id].decrease_amount(amount)
            return
 
    def get_highest(self):
        cur_highest_id = 0
        cur_highest_price = 0
        for proid in self.__item_dict:
            if cur_highest_price < self.__item_dict[proid].price:
                cur_highest_id = proid
                cur_highest_price = self.__item_dict[proid].price
        print(f'the item with the highest price is {self.__item_dict[cur_highest_id].name}')

if __name__ == "__main__":
    pen = Item(10, 'pen', 4, 20)
    pencil = Item(12, 'pencil', 7, 20)
    table = Item(15, 'table', 20, 20)
    inv = Inventory('inv')
    inv.add(pen)
    inv.add(pencil)
    inv.add(table)
    inv.get_highest()
    inv.remove(table)
    inv.get_highest()
