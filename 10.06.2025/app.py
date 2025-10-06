import flask
import math

app = flask.Flask(__name__)
app.config["SECRET_KEY"] = '123445678'

products = [
        {"id": 1, "name": "Notebook Gamer X", "price": 5200.00},
        {"id": 2, "name": "Mouse wireless", "price": 150.00},
        {"id": 3, "name": "Mechanical Keyboard" , "price":350 },
        {"id": 4, "name": "Display 27 inches", "price":1800 },
        {"id": 5, "name": "Vibrator", "price": 10 }
]

@app.route('/')
def index()->object:
    flask.session["products"] = products

    return flask.redirect('/products_by_page/1');

@app.route('/products_by_page/<index>')
def product_list_by_page(index)->object:
    page = int(index)
    per_page = 5

    #
    start = (page-1) * per_page
    end = start + per_page

    total_pages = math.cell(len(products) / per_page)

    products_page = products[start:end]

    print(products_page)

    return 'AAAAA'
    """
    #
    flask.session["page_start"] = start
    flask.session["page_end"] = end

    return flask.render_template('products_by_page')
    """

if __name__ == "__main__":
    app.run(debug=True)
