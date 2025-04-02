from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/products')
def products():
    product_list = ['Cars', 'Motorcycles', 'Vans', 'Bicycles', 'Lorrys']
    return render_template("products.html", products=product_list)

@app.route('/api/products')
def api_products():
    product_list = ['Cars', 'Motorcycles', 'Vans', 'Bicycles', 'Lorrys']
    return jsonify({'products': product_list})

@app.route('/subscribe/form')
def subscribe_form():
    return render_template("subscribe_form.html")

@app.route('/subscribe', methods=['POST'])
def subscribe():
    name = request.form.get('name')
    email = request.form.get('email')
    return render_template("subscribe.html", name=name, email=email)

@app.route('/product/<int:pid>')
def product(pid):
    product_list = ['Cars', 'Motorcycles', 'Vans', 'Bicycles', 'Lorrys']
    if pid < len(product_list):
        return "<h1>Product " + product_list[pid] + "</h1>"
    else: 
        return "<h1>Product id not found"


if __name__ == '__main__':
    app.run(port=5001, debug=True)