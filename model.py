import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Load Dataset
df = pd.read_csv("data/grocery_dataset.csv")

# Create Basket
basket = (
    df.groupby(["InvoiceNo", "Description"])["Quantity"]
      .sum()
      .unstack()
      .fillna(0)
)

# Convert to Boolean
basket = basket > 0

# Generate Frequent Itemsets
frequent_itemsets = apriori(
    basket,
    min_support=0.02,
    use_colnames=True
)

# Generate Rules
rules = association_rules(
    frequent_itemsets,
    metric="lift",
    min_threshold=1
)

rules = rules.sort_values(
    by="lift",
    ascending=False
)


def recommend(product_name):

    product_name = product_name.lower()

    recommendations = rules[
        rules["antecedents"].apply(
            lambda items: any(
                item.lower() == product_name
                for item in items
            )
        )
    ].copy()

    recommendations = recommendations.sort_values(
        by="lift",
        ascending=False
    )

    recommendations["Recommended Product"] = recommendations[
        "consequents"
    ].apply(
        lambda x: ", ".join(list(x))
    )

    return recommendations[
        [
            "Recommended Product",
            "confidence",
            "lift"
        ]
    ]


def get_products():
    return sorted(df["Description"].unique())


def get_statistics():
    return {
        "Transactions": df["InvoiceNo"].nunique(),
        "Products": df["Description"].nunique(),
        "Rules": len(rules)
    }