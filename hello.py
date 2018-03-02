import os
import random
import uuid
from flask import Flask, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/root/testapi/uploads'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def msg():
    msgs = [
    'I think what he meant was, there is a choice function in the Python Library for a reason',
    'If you want to randomly select more than one item from a list, or select an item from a set, I would recommend using random.sample instead.',
    'I propose a script for removing randomly picked up items off a list until it is empty',
    'Feature engineering is often the most impactful thing you can do to improve quality of models and a place where I often see beginners (and experts for that matter) get stuck',
    'Given that entire scientific careers, books, and conferences are built around the topic of feature engineering, and at least IMO good ML tools live or die with good feature engineering (in its broadest sense, for you deep learning fanatics :-)) that doesnt seem like more than the bare minimum Id expect from any ML "crash-course"',
    'Although Im normally skeptical of AI/ML courses, that section on feature engineering dos-and-do-nots is new and surprisingly under-discussed. Its very useful even outside of AI/ML.',
    'They are sales-culture oriented, and their product HAPPENS TO BE technology. In fact you could argue, the only way to win big enterprise contracts in the first place, is to be a sales-culture company.',
    'If only people knew how often employees of companies like this scrambled to build something in a mad panic because some exec made a promise to a client about software that wasnt even designed yet.',
    ]
    return random.choice(msgs)


@app.route('/face', methods=['POST'])
def process_face():
    if 'file' not in request.files:
        return jsonify(status='error', reason='no file submitted'), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify(status='error', reason='no file submitted'), 400
    if file and allowed_file(file.filename):
        filename = str(uuid.uuid4())
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify(status='success', reason='', text=msg()), 200
