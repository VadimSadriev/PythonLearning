from flask import Flask,session
from Decorators import check_logged_in

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello from simple webapp'


@app.route('/page1')
@check_logged_in
def page1() -> str:
    return 'this is page1'


@app.route('/page2')
@check_logged_in
def page2() -> str:
    return 'this is page2'


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You now logged out'


@app.route('/status')
def check_status() -> str:
    # useless func since we got decorator
    if 'logged_in' in session:
        return 'you are currently loged in'
    return 'You not logged in'


def check_logged_in() -> bool:
    if 'logged_in' in session:
        return True
    return False


app.secret_key = 'YouWillNeverGuess'


if __name__ == '__main__':
    app.run(debug=True)

