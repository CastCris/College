import flask
import os

app = flask.Flask(__name__)
app.secret_key = os.urandom(25)

dados_biography = {
        "santos_dumont" : {
            "name" : "Santos Dumont",
            "bio" : "Alberto Santos de Doumont foi um aeronauta, esportista e inventor brasileiro..."
        },
        "merie_curie" : {
            "name" : "Marie Curie",
            "bio" : "Marie Sktodowska Curie foi uma física e química polonesa naturalizada..."
        },
        "Albert": {
            "name" : "Albert Einstein",
            "bio" : "Albert Einstein foi um físico teórico alemão que desenvolveu a teoria da relatividade geral"
        }
}

@app.route("/")
def index()->object:
    flask.session["character_names"] = list(dados_biography.keys())
    flask.session["character_all"] = dados_biography

    return flask.render_template('index.html')

@app.route("/biography/<person>")
def biography_auth(person)->object:
    if person not in dados_biography.keys():
        flask.session["message"] = "Person not found"
        return flask.redirect('/')

    flask.session["message"] = '';
    
    flask.session["character_choosen"] = dados_biography[person]

    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
