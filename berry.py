from flask import Flask, session, request, render_template, redirect, make_response, flash
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.secret_key = 'oh-so-secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.before_request
def print_cookies():
    print(request.cookies)


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


@app.route('/later-cookie')
def later():
    '''an example page that can use that cookie'''
    fav_color = request.cookies.get('fav_color', '<unset>')
    return render_template('later-cookie.html', fav_color=fav_color)


@app.route('/demo')
def res_demo():
    return '<h1>hello</h1>'


@app.route('/demo')
def res_demo():
    content = '<h1>hello</h1>'
    res = make_response(content)
    res.set_cookie('jolly_rancher_flavor', 'grape')
    return res


@app.route('/form-cookie')
def show_form():
    '''show form that prompts for favorite color'''
    return render_template('form-cookie.html')


@app.route('/handle-form-cookie')
def handle_form():
    '''return form response; include cookie for browser'''
    fav_color = request.args['fav_color']
    # get html to send back.  normally we'd return this, but we need to do it in pieces, so we can add a cookie first
    html = render_template('response-cookie.html', fav_color=fav_color)
    # in order to set a cookie from flask, we need to deal with the response a bit more directly than usual.  first, lets make a response obj from that html
    resp = make_response(html)
    # lets add a cookie to our response.  there are lots of other options here.  see the flask docs for how to set cookie expiration, domain it should apply to, or path
    resp.set_cookie('fav_color', fav_color)
    return resp


@app.route('/some-route')
def some_route():
    '''set fav_number in session'''
    sesstion['fav_number'] = 42
    return 'okay, i put that in the session'


@app.route('/form-session')
def show_session_form():
    '''show form that prompts for nickname and lucky number'''
    return render_template('form-session.html')


@app.route('/handle-form-session')
def handle_session_form():
    '''return agreeable response and save to session'''
    # get nickname and lucky number from form and put them into the session -- this will automatically trigger flasks session machinery, so it will now send out a cookie with a session id.  since we're using the standard 'store session data as a cookie', it will include that
    session['nickname'] = request.args['nickname']
    session['lucky_number'] = int(request.args['lucky_number'])
    # since we stored this in the session, we don't even need to pass it to the template directly -- jinja templates automatically have access to session information
    # return render_template('response-session.html', nickname=session['nickname'], lucky_number=session['lucky_number'])
    return render_template('response-session.html')


@app.route('/secret-invite')
def show_secret_invite():
    if session.get('entered-pin', False):
        return render_template('invite.html')
    else:
        return redirect('/login-form')


@app.route('/login')
def verify_secret_code():
    secret = 'chickens_are_great'
    entered_code = request.args['secret_code']
    if entered_code == secret:
        session['entered-pin'] = True
        return redirect('/secret-invite')
    else:
        return redirect('/login-form')


@app.route('/login-form')
def show_login_form():
    return render_template('login-form.html')
