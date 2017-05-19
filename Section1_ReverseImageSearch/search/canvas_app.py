import os
from canvas import Canvas
from flask import Flask, render_template, request, jsonify, send_from_directory

# creating  a flask instance
app = Flask(__name__)


# index page
@app.route('/')
def index():
    return render_template('results_template.html')


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('../resources/img/', path)


@app.route('/search', methods=['POST'])
def search():
    if request.method == "POST":

        RESULTS_ARRAY = []

        # get url
        f = request.files["img"]

        f.save(f.filename)

        image_url = f.filename

        try:

            c = Canvas()

            results = c.search(image_url)

            for (_, image) in results:
                RESULTS_ARRAY.append({"image": image})

            return jsonify(results=RESULTS_ARRAY[:20])

        except:
            # return error
            jsonify({"sorry": "Sorry, no results! Please try again."}), 500


# run
if __name__ == '__main__':
    app.run('127.0.0.1', debug=True)
