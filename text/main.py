from flask import Flask, render_template, request, redirect, url_for
from config import DevConfig
#from sentiment import get_all_words, get_tweets_for_model, remove_noise,process
from datetime import timedelta

app = Flask(__name__)
app.config['DEBUG'] =True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
app.config.from_object(DevConfig)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/sentiment', methods=['GET','POST'])
def sentiment():
    if request.method == 'POST':
        import requests
        userinput = request.form.get('result')
        abc = requests.post('http://text-processing.com/api/sentiment/', data={"text": str(userinput)})
        return render_template('result.html', A= str(userinput), B=str(abc.text))
    return render_template('sentiment.html')

#app.route('/sentiment', methods=['GET','POST'])
#def sentiment():
 #   if request.method == 'POST':
 #      custom_tweet = request.form.get('result')
 #       a,b,c,d,e = process(custom_tweet)
 #       return render_template('result.html', A=a, B=b, C=c, D=d, E=e)
 #   return render_template('sentiment.html')

@app.route('/result', methods=['GET','POST'])
def result():
    return render_template('result.html')

@app.route('/return')
def back():
 	return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run()