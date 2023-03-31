from flask import Flask, render_template, request
import subprocess
import re

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def execute_command():
    if request.method == 'POST':
        command = request.form['message']
        if re.match('^[&a-zA-Z0–9\$\{\}]{1,20}$', command):
            try:
                cmd = '/usr/games/cowsay ' + command + '--test'
                output = subprocess.check_output(cmd,shell=True)
            except subprocess.CalledProcessError as error:
                output = error.output
            return render_template('index.html', output=output.decode('utf-8'))
        else:
            return render_template('index.html',error='Nu-mi place ce vrei sa faci ...')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
