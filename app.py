from flask import Flask, render_template

app = Flask(__name__)

inventario = [
    {"nombre": "Arroz", "precio": 2.50, "cantidad": 20},
    {"nombre": "Azúcar", "precio": 1.80, "cantidad": 15},
    {"nombre": "Aceite", "precio": 3.20, "cantidad": 10},
    {"nombre": "Leche", "precio": 1.25, "cantidad": 30},
    {"nombre": "Harina", "precio": 2.00, "cantidad": 18},
    {"nombre": "Café", "precio": 4.50, "cantidad": 12},
    {"nombre": "Sal", "precio": 0.90, "cantidad": 25}
]

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/inventario")
def mostrar_inventario():
    return render_template("inventario.html", inventario=inventario)

if __name__ == "__main__":
    app.run(debug=True)
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)