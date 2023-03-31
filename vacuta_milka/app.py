from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def execute_command():
    if request.method == 'POST':
        command = request.form['message']
        try:
            cmd = '/usr/games/cowsay ' + command 
            output = subprocess.check_output(cmd,shell=True)
        except subprocess.CalledProcessError as error:
            output = error.output
        return render_template('index.html', output=output.decode('utf-8'))
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
