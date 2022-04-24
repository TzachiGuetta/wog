from flask import render_template, Flask
import flask
import Utils
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__, static_folder=dir_path, static_url_path='')


def score():
    try:
        file = open(Utils.score_file_name, "r")
        score = int(file.readline())
        html_generator('temp.html', score)
    except Exception as err1:
        html_generator('errortemp.html', err1)


def html_generator(file_name, text):
    app = flask.Flask('my app')
    # if __name__ == "__main__":
    with app.app_context():
        rendered = render_template(file_name, \
                                   title='Scores Game', \
                                   people=[{"name": text}])
    with open('blog.html', 'w') as file:
        file.write(rendered)


# @app.route('/')
# def score_server():
#     score()
#     return app.send_static_file('blog.html')
#
# if __name__ == '__main__':
#     app.run(threaded=True, port=5001)
#
# score_server()