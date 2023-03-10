from flask import Flask, session, request, render_template, redirect, make_response, flash
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.secret_key = 'oh-so-secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# make flask errors be real errors not html pages with error info
# app.config['TESTING'] = True
app.testing = True
app.debug = True
# cole says this is a bit of a hack, but don't use flask debugtoolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
toolbar = DebugToolbarExtension(app)


def calc_taxes(income):
    '''calculate taxes owed for this income'''
    ...


@app.route('/taxes', methods=['post'])
def taxes():
    '''calculate taxes from web form'''
    income = request.form.get('income')
    owed = calc_taxes(income)
    return render_template('taxes.html', owed=owed)


# @app.before_request
# def print_cookies():
#     print(request.cookies)


# @app.route('/')
# def home_page():
#     'shows home page'
#     html = '''
#         <html>
#             <body>
#                 <h1>home page</h1>
#                 <p>welcome to my simple app</p>
#                 <a href="/hello">go to hello page</a>
#             </body>
#         </html>
#     '''
#     return html


# @app.route('/hello')
# def index():
#     'return to homepage'
#     return render_template('hello.html')


# @app.route('/lucky')
# def show_lucky_num():
#     'example of simple dynamic template'
#     num = randint(1, 100)
#     return render_template('lucky.html', lucky_num=num)


# @app.route('/form')
# def show_form():
#     return render_template('form.html')


# @app.route('/old-home-page')  # old route
# def redirect_to_home():
#     return redirect('/')  # redirect to new


# @app.route('/later-cookie')
# def later():
#     '''an example page that can use that cookie'''
#     fav_color = request.cookies.get('fav_color', '<unset>')
#     return render_template('later-cookie.html', fav_color=fav_color)


# @app.route('/demo')
# def res_demo():
#     return '<h1>hello</h1>'


# @app.route('/demo')
# def res_demo():
#     content = '<h1>hello</h1>'
#     res = make_response(content)
#     res.set_cookie('jolly_rancher_flavor', 'grape')
#     return res


# @app.route('/form-cookie')
# def show_form():
#     '''show form that prompts for favorite color'''
#     return render_template('form-cookie.html')


# @app.route('/handle-form-cookie')
# def handle_form():
#     '''return form response; include cookie for browser'''
#     fav_color = request.args['fav_color']
#     # get html to send back.  normally we'd return this, but we need to do it in pieces, so we can add a cookie first
#     html = render_template('response-cookie.html', fav_color=fav_color)
#     # in order to set a cookie from flask, we need to deal with the response a bit more directly than usual.  first, lets make a response obj from that html
#     resp = make_response(html)
#     # lets add a cookie to our response.  there are lots of other options here.  see the flask docs for how to set cookie expiration, domain it should apply to, or path
#     resp.set_cookie('fav_color', fav_color)
#     return resp


# @app.route('/some-route')
# def some_route():
#     '''set fav_number in session'''
#     sesstion['fav_number'] = 42
#     return 'okay, i put that in the session'


# @app.route('/form-session')
# def show_session_form():
#     '''show form that prompts for nickname and lucky number'''
#     return render_template('form-session.html')


# @app.route('/handle-form-session')
# def handle_session_form():
#     '''return agreeable response and save to session'''
#     # get nickname and lucky number from form and put them into the session -- this will automatically trigger flasks session machinery, so it will now send out a cookie with a session id.  since we're using the standard 'store session data as a cookie', it will include that
#     session['nickname'] = request.args['nickname']
#     session['lucky_number'] = int(request.args['lucky_number'])
#     # since we stored this in the session, we don't even need to pass it to the template directly -- jinja templates automatically have access to session information
#     # return render_template('response-session.html', nickname=session['nickname'], lucky_number=session['lucky_number'])
#     return render_template('response-session.html')


# @app.route('/secret-invite')
# def show_secret_invite():
#     if session.get('entered-pin', False):
#         return render_template('invite.html')
#     else:
#         return redirect('/login-form')


# @app.route('/login')
# def verify_secret_code():
#     secret = 'chickens_are_great'
#     entered_code = request.args['secret_code']
#     if entered_code == secret:
#         session['entered-pin'] = True
#         return redirect('/secret-invite')
#     else:
#         return redirect('/login-form')


# @app.route('/login-form')
# def show_login_form():
#     return render_template('login-form.html')


# def adder(x, y):
#     '''add two numbers together
#     >>> adder(3, 5)
#     8
#     >>> adder(-1, 50)
#     49
#     '''
#     return x + y


# assert adder(1, 1) == 2, '1 + 1 is not 2'

# def reverse_str(s):
#     '''returns reverse of input str (s)'''
#     return s[::-1]


# def is_palindrome(s):
#     '''boolean method to check whether given string is palindrome'''
#     rev = reverse_str(s)
#     return s.lower() == rev.lower()


# def factorial(n):
#     '''calculates factorial iteratively'''
#     if not (isinstance(n, int) and n >= 0):
#         raise ValueError("'n' must be a non-negative integer")
#     if n == 0:
#         return 1
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result

# @app.route('/')
# def index():
#     '''show homepage'''
#     # keep a count of how many times a page is visited
#     session['count'] = session.get('count', 0) + 1
#     return render_template('index.html')


# @app.route('/fav-color', methods=['post'])  # post route
# def fav_color():
#     '''show favorite color'''
#     fav_color = request.form.get('color')
#     # extracts color from form data sent with the post request.  looking for color that has ben passed through as the post req data
#     return render_template('color.html', fave_color=fav_color)


# @app.route('/redirect-me')
# def redirect_me():
#     '''redirect user to homepage'''
#     return redirect('/')
