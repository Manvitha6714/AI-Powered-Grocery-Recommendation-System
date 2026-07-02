import random
import pandas as pd

random.seed(42)

# Products
products = [
    "Milk", "Bread", "Butter", "Cheese", "Yogurt", "Eggs",
    "Tea", "Coffee", "Sugar", "Soft Drink", "Fruit Juice",
    "Biscuits", "Chips", "Chocolate", "Cookies", "Popcorn",
    "Apple", "Banana", "Orange", "Grapes","Jam",
    "Tomato", "Onion", "Potato", "Carrot",
    "Rice", "Wheat Flour", "Cooking Oil", "Salt", "Spices",
    "Soap", "Shampoo", "Conditioner", "Toothpaste", "Toothbrush",
    "Detergent", "Dishwashing Liquid", "Tissue Paper",
    "Chicken", "Fish"
]

# Shopping patterns
patterns = {
    "Milk": ["Bread", "Butter", "Cheese"],
    "Bread": ["Butter", "Jam"],
    "Tea": ["Biscuits", "Sugar"],
    "Coffee": ["Milk", "Sugar"],
    "Rice": ["Cooking Oil", "Salt", "Spices"],
    "Chicken": ["Cooking Oil", "Spices"],
    "Fish": ["Spices"],
    "Shampoo": ["Conditioner"],
    "Toothpaste": ["Toothbrush"],
    "Soap": ["Shampoo"],
    "Chips": ["Soft Drink"],
    "Chocolate": ["Cookies"],
    "Apple": ["Banana"],
    "Yogurt": ["Fruit Juice"]
}

transactions = []

invoice = 100001

for _ in range(5000):

    basket = set()

    main = random.choice(products)
    basket.add(main)

    if main in patterns:
        for item in patterns[main]:
            if random.random() < 0.8:
                basket.add(item)

    while len(basket) < random.randint(3, 8):
        basket.add(random.choice(products))

    for item in basket:
        transactions.append([
            invoice,
            item,
            random.randint(1, 3)
        ])

    invoice += 1

df = pd.DataFrame(
    transactions,
    columns=["InvoiceNo", "Description", "Quantity"]
)

df.to_csv("data/grocery_dataset.csv", index=False)

print("Dataset created successfully!")
print(df.head())