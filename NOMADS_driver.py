import sys
sys.path.append('./static/')

import os
from NOMADS_pipeline import pipeline
from NOMADS_io import load_file, dump_file
from werkzeug.utils import secure_filename
from flask import Flask, render_template, redirect, url_for, session, request, send_file


UPLOAD_FOLDER = './static/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#NOTE: this is only a single user application
#being run on a desktop. THIS MUST BE CHANGED
#if the app is to deploy online
app.secret_key='NOMADS_key'


def clear_session():
    for key in session.keys():
        session.pop[key]
    return


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(url_for('index'))
        my_file = request.files['file']
        filename = os.path.join(app.config['UPLOAD_FOLDER'],
                                secure_filename(my_file.filename))
        my_file.save(filename)
        session['input_data_path'] = filename
        return redirect(url_for('launch_pipeline'))


@app.route('/launch_pipeline', methods=['GET'])
def launch_pipeline():
    input_data = None
    try:
        input_data = load_file(session['input_data_path'])
    except:
        flash('Error: Could not load data file')
        clear_session()
        return redirect(url_for('index'))

    output_data = pipeline(input_data)
    output_data_path = './static/results/output.tiff'
    session['output_data_path'] = output_data_path
    dump_file(output_data_path, output_data)
    return redirect(url_for('results'))


@app.route('/results')
def results():
    return send_file(session['output_data_path'],
                     attachment_filename='NOMADS_output.tiff')


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000)
