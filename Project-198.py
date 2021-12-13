class Customer():
    items = []
    
    def __init__(self) -> None:
        pass
    
    def add_item(self, i_item,i_quantity, i_amount):
        if not i_item:
            return(False)
        
        quantity = i_quantity
        
        if not i_quantity:
            quantity = 1
            pass
        
        self.items.append(
            {"item": i_item, "quantity": float(quantity), "amount": float(i_amount)}
        )
        
        return(True)
        
        
    
    def delete_last_item(self):
        self.items.pop()
    
    def clear_contumer(self):
        self.items = []
    
    def get_items(self):
        items = []
        for x in self.items:
            items.append(x.item)
        return(items)
    
    def calculate_total(self):
        total = 0
        for x in self.items:
            total += float(x["amount"])
        return(total)
    
    def print_bill(self):
        print(45*"_")
        print("|"+"_"*15+("Py Hypermarket")+"_"*15+"|")
        print(45*"_")
        
        for x in self.items:
            print("|  "+x["item"]+(" "*int((20-len(x["item"]))-0.5))+"      "+str(x["quantity"])+"      "+str(x["amount"])+"    |")
        print("|"+43*"_"+"|")
        print("|  "+"Total: "+str(self.calculate_total())+(" "*int((41-len("Total: "+str(self.calculate_total())))-0.5))+" |")
        print(45*"_")

while True:
    customer = Customer()
    
    while True:
        if customer.add_item(
            input("Enter Item Name: "),
            input("Enter Item Quantity: "),
            input("Enter Item Amount: ")):
            print()
        else:
            break
    
    customer.print_bill()
    
    
    pass
