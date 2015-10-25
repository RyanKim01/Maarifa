from flask import Flask, render_template, Response, request
from flask_restful import Resource, Api
import json
import requests

app = Flask(__name__)
api = Api(app)

def request_all_lessons(subject, level):
    r = requests.get('http://maarifa.herokuapp.com/api/lesson')
    data = r.json()
    lesson_list = []
    for lessons in data['objects']:
        if subject in lessons.values():
            if lessons["lesson_level"] == level:
                lesson_list.append(lessons)

    return lesson_list

def request_lesson(subject, level, title):
    r = requests.get('http://maarifa.herokuapp.com/api/lesson')
    data = r.json()
    lesson_list = []
    for lessons in data['objects']:
        if subject in lessons.values():
            if lessons["lesson_level"] == level and lessons["lesson_title"] == title:
                return lessons["lesson_content"]

    return lesson_list

class Lessons(Resource):

    def post(self):
        return "TODO"

    def get(self, subject, level, title=None):

        if not title:
            lesson_list = request_all_lessons(subject, level)

            return Response((render_template("topics.html", subject=subject, level=level, topics=lesson_list)), mimetype="text/html")
        else:
            content = request_lesson(subject, level, title)
            # return Response((render_template("content.html", lessontitle=title, content=content)), mimetype="text/html")
            return Response((render_template("addition.html", lessontitle=title)), mimetype="text/html")


api.add_resource(Lessons, '/<string:subject>/<int:level>', '/<string:subject>/<int:level>/<string:title>')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Math')
def math():
    return render_template("levelchoice.html", subject="Math")

@app.route('/English')
def eng():
    return render_template("levelchoice.html", subject="English")

@app.route('/Science')
def sci():
    return render_template("levelchoice.html", subject="Science")

if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
