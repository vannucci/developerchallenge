import logging
from flask import Flask, request, send_from_directory, render_template

app = Flask(__name__)
app._static_folder = './static'

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     return render_template('index.html')

@app.errorhandler(500)
def server_error(e):
    #log the error and stacktrace
    logging.exception('An error occurred during request')
    return 'An internal error occurred', 500

if __name__ == "__main__":
    app.run()