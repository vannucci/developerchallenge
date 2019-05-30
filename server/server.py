import logging
from flask import Flask, request, send_from_directory

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.errorhandler(500)
def server_error(e):
    #log the error and stacktrace
    logging.exception('An error occurred during request')
    return 'An internal error occurred', 500

if __name__ == "__main__":
    app.run()