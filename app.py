import flask

amazin_database={
       "Ronaldo":["12","abcd@efg"]
       }

app=flask.Flask(__name__)
app.secret_key='1234567890'


@app.route('/')
def load_page()->None:
    print(flask.g)
    if not "user" in flask.request.cookies:
        return flask.redirect(flask.url_for("login_display"))
    return flask.redirect(flask.url_for("index_display"))

@app.route('/login_display')
def login_display()->None:
    return flask.render_template('login.html')
@app.route('/login_auth',methods=['POST'])
def login_auth()->None:
    if flask.request.method=='POST':
        user_name=flask.request.form['user_name']
        user_email=flask.request.form['user_email']
        user_pass=flask.request.form['user_pass']
        #
        user=None
        if user_name in amazin_database.keys():
            user=amazin_database[user_name]
        if user and  user_pass in user and user_email in user:
            flask.g.user_name=user_name
            response=flask.make_response(flask.redirect('/'))
            response.set_cookie("user",';'.join(user),max_age=10)

            return response
        #
        if not user:
            flask.flash("Invalid user name","danger")
        elif not user_pass in user:
            flask.flash("Invliad user passphrase","danger")
        elif not user_email in user:
            flask.flash("Invalid user email","danger")
        return flask.redirect(flask.url_for("login_display"))
@app.route("/logout")
def logout()->None:
    response=flask.make_response(flask.redirect('/'))
    response.set_cookie('user','',max_age=0)

    return response

@app.route("/index_display")
def index_display()->None:
    return flask.render_template("index.html")


if __name__=='__main__':
    app.run(debug=True)
