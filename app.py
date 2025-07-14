import flask
import subprocess
from features import *
#
user=None
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
app.secret_key='12345'

@app.before_request
def before_request()->None:
    define_users()
    define_notices()

@app.route('/')
def index():
    define_users()
    define_notices()
    """
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
    if not user:
        return flask.redirect(flask.url_for('login_display'))
    else:
        return flask.redirect(flask.url_for('index_display'))

@app.route('/login_display')
def login_display()->object:
    return flask.render_template('login.html',user=user)
@app.route('/login_authenticate',methods=['POST'])
def login_authenticate()->object:
    global user_control
    global user
    #
    if flask.request.method=='POST':
        username=flask.request.form['username']
        passphrase=flask.request.form['passphrase']
        #
        if not username or not passphrase:
            flask.flash("Preenchar todos os dados")
            return flask.render_template('login.html')
        #
        user=user_control.get_user(username.lower())
        if not user:
            flask.flash(f"The user {username} doesn't exist","danger")
            return flask.redirect(flask.url_for("login_display"))
        user.get_infos(DIVISOR_VAR_CONTENT)
        passphrase_user=(user.get_attr("passphrase"))[0]
        user.display_cli()
        print(passphrase_user)
        #
        if passphrase==passphrase_user:
            return flask.redirect(flask.url_for('index_display'))
        flask.flash("Deu ruim, faz de novo o login","danger")
        return flask.render_template('login.html')

@app.route('/index_display')
def index_display()->None:
    global notice_control
    #
    notices=notice_control.get_notices(DIVISOR_VAR_CONTENT)
    return flask.render_template('index.html',search='*',user=user)
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
