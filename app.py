import flask
import subprocess
#
database={'1':'2'}
#
class Noticia:
    def __init__(self,titulo:str,conteudo:str,type:str)->None:
        self.title=titulo.lower()
        self.content=conteudo.lower()
        self.type=type.lower()

def define_notices()->None:
    global notices
    #
    notices=[]
    notices.append(Noticia('Pele reviveu','QWERTYUIO','Entreterimento'))
    notices.append(Noticia('Jordan morreu','1234567890','Comédia'))

def match_item(item:str,pattern:str)->str:
    pipe1 = subprocess.Popen(["echo",item],stdout=subprocess.PIPE) 
    pipe2 = subprocess.Popen(["grep","-E",pattern],stdin=pipe1.stdout,stdout=subprocess.PIPE) 
    pipe1.stdout.close()
    
    result,_ =pipe2.communicate() 
    result = result.decode().strip() 

    return result
#
app=flask.Flask(__name__)

@app.route('/')
def view_login()->object:
    return flask.render_template('login.html',fail=0)

@app.route('/process_login',methods=['POST','GET'])
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
@app.route('/home_page_search')
def home_page_search()->None:
    if flask.request.method=='POST':
        pattern=flask.request.form['pattern'].lower()
        return flask.render_template('index.html',notices=notices,search=pattern)

if __name__=='__main__':
    app.run(debug=True)