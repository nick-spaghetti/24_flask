from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.route('/')
def home_page():
    'shows home page'
    html = '''
        <html>
            <body>
                <h1>home page</h1>
                <p>welcome to my simple app</p>
                <a href="/hello">go to hello page</a>
            </body>
        </html>
    '''
    return html


@app.route('/hello')
def index():
    'return to homepage'
    return render_template('hello.html')


@app.route('/lucky')
def show_lucky_num():
    'example of simple dynamic template'
    num = randint(1, 100)
    return render_template('lucky.html', lucky_num=num)


@app.route('/form')
def show_form():
    return render_template('form.html')


@app.route('/old-home-page')  # old route
def redirect_to_home():
    return redirect('/')  # redirect to new
