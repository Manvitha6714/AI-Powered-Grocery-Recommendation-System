import streamlit as st
from model import recommend, get_products, get_statistics

emoji = {
    "Milk": "🥛",
    "Bread": "🍞",
    "Butter": "🧈",
    "Cheese": "🧀",
    "Tea": "🍵",
    "Coffee": "☕",
    "Biscuits": "🍪",
    "Chocolate": "🍫",
    "Cookies": "🍪",
    "Apple": "🍎",
    "Banana": "🍌",
    "Orange": "🍊",
    "Rice": "🍚",
    "Chicken": "🍗",
    "Fish": "🐟",
    "Soft Drink": "🥤",
    "Fruit Juice": "🧃",
    "Eggs": "🥚",
    "Yogurt": "🥣",
    "Cooking Oil": "🫒",
    "Sugar": "🍚",
    "Salt": "🧂",
    "Tomato": "🍅",
    "Potato": "🥔",
    "Carrot": "🥕",
    "Onion": "🧅",
    "Soap": "🧼",
    "Shampoo": "🧴",
    "Conditioner": "🧴",
    "Toothpaste": "🪥",
    "Toothbrush": "🪥",
    "Detergent": "🧴",
    "Dishwashing Liquid": "🧽",
    "Tissue Paper": "🧻"
}

st.set_page_config(
    page_title="🛒 AI Grocery Recommendation System",
    page_icon="🛒",
    layout="wide"
)
st.sidebar.title("📌 About")
st.sidebar.write("""
This application recommends grocery products that are frequently purchased together.

### Technologies
- Python
- Streamlit
- Pandas
- MLxtend
- Apriori Algorithm

### Dataset
Synthetic Grocery Dataset
5000 Transactions
40 Products
""")

st.sidebar.info(
    """
    This application recommends products that are frequently
    purchased together using the Apriori Algorithm.

    **Tech Stack**
    - Python
    - Streamlit
    - Pandas
    - MLxtend
    """
)

st.title("🛒 Market Basket Recommendation System")

st.markdown("""
### Discover products that customers frequently purchase together.

This application uses **Market Basket Analysis** with the **Apriori Algorithm**
to recommend products based on historical shopping patterns.
""")
stats = get_statistics()

col1, col2, col3 = st.columns(3)

col1.metric("🧾 Transactions", stats["Transactions"])
col2.metric("🛍️ Products", stats["Products"])
col3.metric("📈 Rules", stats["Rules"])

product = st.selectbox(
    "Select Product",
    get_products()
)
if st.button("🔍 Recommend"):

    if product.strip() == "":
        st.warning("Please enter a product name.")
    else:
        import time

    with st.spinner("Finding recommendations..."):
        time.sleep(1)
        result = recommend(product)

        if result.empty:
            st.error("No recommendations found.")
        else:
            st.success(f"Top recommendations for **{product}**")

            st.subheader("Recommended Products")

            for _, row in result.iterrows():

                product_name = row["Recommended Product"]

                icon = emoji.get(product_name, "🛒")

                st.markdown(f"## {icon} {product_name}")
                st.write(f"⭐ Confidence : {row['confidence']:.2%}")
                st.write(f"📈 Lift : {row['lift']:.2f}")
                st.divider()
                st.markdown("---")

st.caption(
    "Developed by Manvitha | Python • Streamlit • Apriori • MLxtend"
)
                