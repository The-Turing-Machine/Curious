from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import os


app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Homepage!!'

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(threaded=True,port=port)
