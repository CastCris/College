"""
import flask
import subprocess
#
app=flask.Flask(__name__)

@app.route('/')
def view_login()->object:
    return flask.render_template('login.html',fail=0)

@app.route('/process_login',methods=['POST'])
def check_login()->object:
    if flask.request.method=='POST':
        username=flask.request.form['username'].lower()
        passphrase=flask.request.form['passphrase'].lower()
        if username in database.keys() and database[username]==passphrase:
            return flask.redirect(flask.url_for('home_page_display'))
        return flask.render_template('login.html',fail=1)

@app.route('/home_page_display')
def home_page_display()->None:
    global notices
    #
    define_notices()
    print(notices)
    return flask.render_template('index.html',search='*',notices=notices)
@app.route('/home_page_search',methods=['POST'])
def home_page_search()->None:
    global notices
    #
    if flask.request.method=='POST':
        pattern=flask.request.form['pattern'].lower()
        for i in notices:
            search_result=match_item(i.type,pattern)
        return flask.render_template('index.html',notices=notices,search=pattern)

if __name__=='__main__':
    app.run(debug=True)
"""
from features import *

tst=User("./database/users/Ronaldo.opa.txt")
tst.get_infos(DIVISOR_VAR_CONTENT)
tst.display_cli()

"""
tst=Notice("./database/notices/Pele_vivo.txt")
tst.get_infos(DIVISOR_VAR_CONTENT)
tst.display_cli()
"""
