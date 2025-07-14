import flask
import subprocess
from features import *
#
def define_users()->None:
    global user_control
    #
    user_control=User_Manager("./database/users")
def define_notices()->None:
    global notice_control
    #
    notice_control=Notice_Manager("./database/notices")
#
app=flask.Flask(__name__)

@app.route('/')
def view_login()->object:
    """
    define_users()
    define_notices()
    for i in user_control.get_item_all():
        print(i)
        tst=User(i)
        tst.get_infos(DIVISOR_VAR_CONTENT)
        tst.display_cli()
    for i in notice_control.get_item_all():
        print(i)
        tst=Notice(i)
        tst.get_infos(DIVISOR_VAR_CONTENT)
        tst.display_cli()
    """
    #
    return flask.render_template('login.html',fail=0)

@app.route('/authenticate',methods=['POST'])
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
