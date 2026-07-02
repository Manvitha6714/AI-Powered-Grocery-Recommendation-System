from flask import Flask, render_template, request
from model import get_products, recommend

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    products = get_products()

    recommendations = None
    selected_product = ""

    if request.method == "POST":

        selected_product = request.form["product"]

        recommendations = recommend(selected_product)

    return render_template(
        "index.html",
        products=products,
        recommendations=recommendations,
        selected_product=selected_product
    )

if __name__ == "__main__":
    app.run(debug=True)