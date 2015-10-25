from flask import Flask, render_template, Response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Topics(Resource):

    def post(self):
        return "TODO"

    def get(self, subject, level):

        topname = subject+" at "+str(level)

        return Response((render_template("content.html", topicname=topname)), mimetype="text/html")

api.add_resource(Topics, '/sub/', '/sub/<string:subject>/<int:level>')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sub/math')
def math():
    return render_template("levelchoice.html", subject="Math", sublink="sub/math")

@app.route('/sub/eng')
def eng():
    return render_template("levelchoice.html", subject="English", sublink="sub/eng")

@app.route('/sub/sci')
def sci():
    return render_template("levelchoice.html", subject="Science", sublink="sub/sci")

if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
