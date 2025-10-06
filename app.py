import flask

app = flask.Flask(__name__)

products = [
        {"id": 1, "name": "Notebook Gamer X", "price": 5200.00},
        {"id": 2, "name": "Mouse wireless", "price": 150.00},
        {"id": 3, "name": "Mechanical Keyboard" , "price":350 },
        {"id": 4, "name": "Display 27 inches", "price":1800 },
        {"id": 5, "name": "Vibrator", "price": 10 }
]

@app.route('/')
def index()->object:
    return '<h1>Hello World!</h1>'

if __name__ == "__main__":
    app.run(debug=True)
