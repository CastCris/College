import flask

app=flask.Flask(__name__)

@app.route("/")
def display_login()->None:
	return flask.render_template('login.html')
###
@app.route("/login_or_signin",methods=["POST","GET"])
def login()->None:
	message=":D"
	print(request.method)


if __name__=="__main__":
	app.run(debug=True)
