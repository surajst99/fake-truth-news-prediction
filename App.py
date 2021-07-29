from flask import request,render_template,Flask
from flask.signals import request_tearing_down
import numpy as np
from nltk.corpus import stopwords
import re
import pickle
stopwrds = stopwords.words('english')


model_fpath ='./static/fake_true_model.sav'
clf = pickle.load(open(model_fpath, 'rb'))
vect_path = './static/vectorizer.sav'
vect = pickle.load(open(vect_path, 'rb'))




def preprocess_text(text:str) -> str:
    text = text.lower()
    text = [t for t in re.findall('\w+',text) if t not in stopwrds ]
    text = [t for t in text if len(t) > 1]
    return " ".join(text)



Passowrd = 'SURAJ123'
Email = 'suraj99'


App = Flask(__name__)  # initialize Flask 


@App.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        login = request.form.get('Email')
        password = request.form.get('Password')
        

        print(login)
        if (login == 'suraj99') & (password =='SURAJ123'):
            return render_template('index.html')
        else:
            return "<h1>Credntial Failed</h1>"
    return render_template('Login-page.html')

@App.route("/text",methods =['GET','POST'])

def type_prediction():
    if request.method == 'POST':
        text = request.form.get('text')
        
        vector = vect.transform([text])
        type = clf.predict(vector)

        return render_template('index.html',text =text[0],type =type)
    return render_template("index.html")



if __name__=='__main__':
    App.run(debug=True)