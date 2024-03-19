import os

from flask import Flask, request, render_template, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from prometheus_flask_exporter import PrometheusMetrics

# Settings
UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
metrics = PrometheusMetrics(app)

# static information as metric
metrics.info('image_view', 'Web Image Viewer', version='1.0.0')
by_path_counter = metrics.counter(
    'by_path_counter', 'Request count by request paths',
    labels={'path': lambda: request.path}
)


@app.route('/')
@by_path_counter
def view_pictures():  # put application's code here
    image_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('view_pictures.html', images=image_files)
    # return 'Hello World!'


@app.route("/pictures/<path:filename>")
def download_picture(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route("/upload", methods=["GET", "POST"])
@by_path_counter
def upload_picture():
    if request.method == "POST":
        # check if the post request has the file part
        if 'picture' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['picture']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('view_pictures'))
    else:
        return render_template("upload.html")


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    app.run()
