from flask import Flask, render_template, \
    redirect, url_for, session, request, flash

app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('report.html')


if __name__ == '__main__':
    app.run(debug=True)