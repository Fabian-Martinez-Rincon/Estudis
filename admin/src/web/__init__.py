from flask import Flask, render_template

def create_app(env='dev', static_folder='../../static'):
    app = Flask(__name__, static_folder=static_folder)


    @app.get('/')
    def home():
        return render_template('home.html')
        


    return app