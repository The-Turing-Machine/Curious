from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify
import os
import data as data
import scheduler as s
import threading
from flask.ext.cors import CORS


app = Flask(__name__)
CORS(app)

class Thread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        s.main()
        self.exit()

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/data')
def send_data():
    return jsonify({'post_data':data.all_social_media_link,'tag_data':data.top_tags})

    # return str(data.all_social_media_link)

if __name__ == "__main__":
    thread_main = Thread()
    thread_main.start()
	port = int(os.environ.get('PORT', 5000))
	app.run(debug=True,threaded=True,host='0.0.0.0',port=port)
