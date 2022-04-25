import MainScores
from Live import load_game, welcome
from flask import render_template, Flask
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__, static_folder=dir_path, static_url_path='')

print(welcome("Tzachi"))
load_game()
#MainScores.score()

# @app.route('/')
# def score_server():
#     return app.send_static_file('blog.html')
#
# if __name__ == '__main__':
#    app.run(threaded=True, port=5000)