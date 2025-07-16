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
    global user
    #
    user=None
    if "USER" in flask.request.cookies:
        user=User(flask.request.cookies.get("user"))
        user.get_infos()
        user.display_cli()
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
    return flask.render_template('account/login.html',user=user)
@app.route('/login_authenticate',methods=['POST'])
def login_authenticate()->object:
    global user_control
    global user
    #
    if flask.request.method=='POST':
        username=flask.request.form['username']
        passphrase=flask.request.form['passphrase']
        #
        user=user_control.get_user(username)
        if not user:
            flask.flash(f"The user {username} doesn't exist","error")
            return flask.redirect(flask.url_for("login_display"))
        user.get_infos(DIVISOR_VAR_CONTENT)
        passphrase_user=(user.get_attr("passphrase"))[0]
        user.display_cli()
        print(user.get_attr("path_infos"))
        print(user.__dict__)
        #
        if passphrase==passphrase_user:
            response=flask.make_response("Set cookie user")
            response.set_cookie("USER",user.get_attr("path_infos")[0])
            print(response.cookie.get("USER"))
            return flask.redirect(flask.url_for('index_display'))
        flask.flash("Deu ruim, faz de novo o login","error")
        return flask.redirect(flask.url_for("login_display"))
@app.route('/sign_display')
def sign_display()->object:
    return flask.render_template('account/sign.html')
@app.route('/create_account',methods=['POST'])
def create_account()->object:
    global user_control
    #
    if flask.request.method=='POST':
        user_name=flask.request.form['user_name']
        user_pass=flask.request.form['user_passphrase']
        user_plus=flask.request.form['plus_infos']
        if user_control.get_item(user_name):
            return flask.render_template('sign.html',message="This user already exist, create other")
        #
        attr={}
        attr["NAME"]=[user_name]
        attr["PASSPHRASE"]=[user_pass]
        attr_plus=get_attr_from_str(user_plus,DIVISOR_VAR_CONTENT)
        attr.update(attr_plus)
        #
        user_control.create_item(user_name,attr,DIVISOR_VAR_CONTENT)
        return flask.redirect(flask.url_for('login_display'))
@app.route('/change_pass_display')
def change_pass_display()->object:
    return flask.render_template('account/change_passphrase.html')
@app.route('/change_pass_auth',methods=['POST'])
def change_pass_auth()->object:
    global user_control
    #
    if flask.request.method=='POST':
        user_name=flask.request.form['user_name']
        user_pass=flask.request.form['user_pass']
        #
        user_pass_new=flask.request.form['user_pass_new']
        #
        if not user_control.get_item(user_name):
            return flask.render_template('account/change_pass.html',message="This user doesn't exist, create one")
        user=user_control.get_user(user_name)
        user.get_infos(DIVISOR_VAR_CONTENT)
        user.display_cli()
        if user_pass==user.get_attr("passphrase")[0]:
            user_control.update_item(user_name,"passphrase",user_pass_new,DIVISOR_VAR_CONTENT)
            return flask.redirect(flask.url_for('login_display'))
        return flask.render_template("account/change_pass.html",message="Invalid passphrase")
@app.route("/logout")
def logout()->object:
    flask.request.set_cookie("user",'',expires=0)
    user=None

    return flask.redirect(flask.url_for('index'))

@app.route('/index_display')
def index_display()->object:
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
