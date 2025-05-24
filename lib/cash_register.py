class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.last_transaction = 0  

    def add_item(self, title, price, quantity=1):
        self.last_transaction = price * quantity
        self.total += self.last_transaction
        self.items.extend([title] * quantity)  

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        if not self.items:
            return  
        self.total -= self.last_transaction
        
        last_item = self.items[-1]
        
        count = 0
        for item in reversed(self.items):
            if item == last_item:
                count += 1
            else:
                break
        self.items = self.items[:-count]  