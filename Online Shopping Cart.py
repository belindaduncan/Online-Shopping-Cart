# Online Shopping Cart:
# Step 1: Build the ItemToPurchase class with the following specifications:
#   Attributes (name, price, quantity)
#   item_name (string) (input)
#   item_price (float) (float(input)
#   item_quantity (int) (int(input)
#   Default constructor - def __init__(self)
#   Initializes item's name = "none", item's price = 0, item's quantity = 0
#   Method
#   print_item_cost()


class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(total)}")

    def get_total_cost(self):
        return self.item_price * self.item_quantity

# Step 2: In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class.
# Use a loop to create multiple items (mod 4 lesson)

items = []

for i in range(2):
    print(f"\nItem {i + 1}")
    item = ItemToPurchase()
    item.item_name = input("Enter the item name:\n")
    item.item_price = float(input("Enter the item price:\n"))
    item.item_quantity = int(input("Enter the item quantity:\n"))
    items.append(item)

# Step 3: Add the costs of the two items together and output the total cost
# Loop through items to print and total

print("\n=== TOTAL COST ===")
total = 0
for item in items:
    item.print_item_cost()
    total += item.get_total_cost()

print(f"\nTotal: ${total:.2f}")