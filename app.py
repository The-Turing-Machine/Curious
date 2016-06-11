from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import os
import data as data
import scheduler as s
import threading

app = Flask(__name__)

class Thread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        s.main()
        self.exit()

@app.route('/')
def homepage():
    thread_main = Thread()
    thread_main.start()
    return render_template('index.html')

@app.route('/data')
def send_data():
    return data.all_social_media_link

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(threaded=True,host='0.0.0.0',port=port)
