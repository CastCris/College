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
app.config['VERSION']='1.0.0'

@app.before_request
def before_request()->None:
    global user
    #
    user=None
    if "user" in flask.request.cookies:
        user=User(flask.request.cookies.get("user"))
        user.get_infos(DIVISOR_VAR_CONTENT)
        user.display_cli()
    flask.g.user=user
    #
    light=0
    if "light" in flask.request.cookies:
        light=flask.request.cookies.get("light");
    flask.g.light=light
    #
    flask.g.message=""
    #
    flask.g.notices=None

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

@app.route('/get_light')
def get_light():
    return {'light':flask.g.light}

@app.route('/login_display')
def login_display()->object:
    if not user:
        return flask.render_template('account/login.html')
    return flask.redirect(flask.url_for('index_display'))
@app.route('/login_auth',methods=['POST'])
def login_auth()->object:
    global user_control
    global user
    #
    if flask.request.method=='POST':
        username=flask.request.form['username']
        passphrase=flask.request.form['passphrase']
        #
        user=user_control.get_user(username,DIVISOR_VAR_CONTENT)
        if not user:
            flask.g.message="The user {} doesn't exist".format(username)
            return flask.render_template("account/login.html")
        passphrase_user=(user.get_attr("passphrase"))[0]
        user.display_cli()
        # print(user.get_attr("path_infos"))
        # print(user.__dict__)
        #
        if passphrase==passphrase_user:
            response=flask.make_response(flask.redirect('/'))
            response.set_cookie("user",user.get_attr("path_infos")[0])
            return response
        flask.g.message="The passprase is incorrect"
        return flask.render_template("account/login.html")
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
            return flask.render_template('account/sign.html')
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
            flask.g.message="The user {} doesn't exist".format(user_name)
            return flask.render_template('account/change_passphrase.html')
        user=user_control.get_user(user_name,DIVISOR_VAR_CONTENT)
        user.display_cli()
        if user_pass==user.get_attr("passphrase")[0]:
            user_control.update_item(user_name,"passphrase",user_pass_new,DIVISOR_VAR_CONTENT)
            return flask.redirect(flask.url_for('login_display'))
        flask.g.message="The passphrase is incorrect"
        return flask.render_template("account/change_passphrase.html")
@app.route("/logout")
def logout()->object:
    response=flask.make_response(flask.redirect("/"))
    response.set_cookie('user','',expires=0)

    return response

@app.route('/index_display')
def index_display()->object:
    global notice_control
    #
    notices=notice_control.get_notices(DIVISOR_VAR_CONTENT)
    flask.g.notices=notices
    return flask.render_template('index.html')
@app.route('/index_search',methods=['GET'])
def index_search()->None:
    global notice_control
    #
    if flask.request.method=='GET':
        pattern=flask.request.args['pattern'].lower()
        notices=notice_control.get_notices_filter(pattern,DIVISOR_VAR_CONTENT)
        for i in notices:
            i.display_cli()
        flask.g.notices=notices
        return flask.render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)

