from flask import Flask, request, render_template, redirect, flash, jsonify
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

debug = DebugToolbarExtension(app)

# set a 'SECRET_KEY' to enable the Flask session cookies
# app.config['SECRET_KEY'] = 'key'
app.secret_key = 'secret'

COMPLIMENTS = ["cool", "clever", "tenacious", "awesome", "Pythonic"]


@app.route('/')
def home_page():
    '''return home '''
    html = '<html><body><h1>home</h1><p>welcome to my simple app</p><a href="/hello">go to hello page</a></body></html>'
    return html


# @app.route('/hello')
# def index():
#     'return to homepage'
#     return render_template('hello.html')


# # @app.route('/lucky')
# # def show_lucky_num():
# #     'example of simple dynamic template'
# #     num = randint(1, 100)
# #     return render_template('hello.html', lucky_num=num)


# @app.route('/lucky')
# def show_lucky_num():
#     num = randint(1, 10)
#     return render_template('lucky.html', lucky_num=num, msg='you are so lucky')


# @app.route('/goodbye')
# def say_goodbye():
#     '''return simple goodbye '''
#     html = '<html><body><h1>goodbye</h1></body></html>'
#     return html


# @app.route('/search')
# def search():
#     term = request.args['term']
#     return f'<h1>searching for {term}</h1>'


# @app.route('/post', methods=['POST'])
# def post_demo():
#     return 'you made a post request'


# @app.route('/post', methods=['GET'])
# def get_demo():
#     return 'you made a get request'


# @app.route('/add-comment')
# def add_comment_form():
#     '''show form for adding a comment'''
#     return '''
# 		<form method="POST">
# 			<input name="comment" type="text" placeholder="comment" />
# 			<input name="username" type="text" placeholder="username" />
# 			<button>submit</button>
# 		</form>
# 	'''


# @app.route('/add-comment', methods=['POST'])
# def add_comment():
#     '''handle adding comment'''
#     comment = request.form['comment']
#     username = request.form['username']
#     # todo: save that into a database
#     print(request.form)
#     return f'''
#     <h1>saved your comment</h1>
#     <ul>
#     <li>username: {username}</li>
#     <li>comment: {comment}</li>
#     </ul>
#     '''


# users = {
#     'whiskey': 'whiskey the dog',
#     'spike': 'spike the porcupine'
# }


# # < ------  # brackets turn that into a variable
# @app.route('/user/<username>')
# def show_user_profile(username):  # < ------  # passed as keyword argument
#     """show user profile for user"""
#     name = users[username]
#     return f'<h1>profile for {name}</h1>'


# posts = {
#     1: 'i like chicken tenders',
#     2: 'i hate mayo',
#     3: 'double rainbow all the way',
#     4: 'yolo omg kill me'
# }


# @app.route('/posts/<int:post_id>')
# def find_post(post_id):
#     print('post_id is a ', type(post_id))
#     # post_id = POSTS[id]
#     post_id = POSTS.get(id, 'post not found')
#     return f'<p>{post_id}</p>'


# @app.route('/r/<subreddit>/comments/<int:post_id>')
# def show_comments(subreddit, post_id):
#     return f'<h1>viewing comments for {post_id} from the {subreddit} subreddit</h1>'


# @app.route('/form')
# def show_form():
#     return render_template('form.html')


# compliments = ['cool', 'clever', 'tenacious', 'awesome', 'pythonic']


# @app.route('/greet')
# def get_greet():
#     username = request.args['username']
#     nice_thing = choice(compliments)
#     return render_template('greet.html', username=username, compliment=nice_thing)


# @app.route('/spell/<word>')
# def spell_word(word):
#     return render_template('spell_word.html', word=word)


# @app.route('/form-2')
# def show_form():
#     return render_template('form_2.html')


# @app.route('/greet-2')
# def get_greeting_2():
#     username = request.args['username']
#     wants = request.args['wants_compliments']
#     nice_things = sample(compliments, 3)
#     return render_template('greet_2.html', username=username, wants_compliments=wants, compliments=nice_things)


# @app.route('/old-home-page')  # old route
# def redirect_to_home():
#     return redirect('/')  # redirect to new


movies = {'amadeus', 'chicken run', 'dances with wolves'}


@app.route('/movies')
def show_all_movies():
    '''show list of all movies in fake db'''
    return render_template('movies.html', movies=movies)


@app.route('/movies/new', methods=['post'])
def add_movie():
    # raise
    import pdb
    pdb.set_trace()
    title = request.form['title']
    if title in movies:
        flash('movie already included', 'error')
    else:
        movies.add(title)
        flash('created your movie', 'success')
    return redirect('/movies')


# @app.route('/your/route')
# def your_route():
#     flash('message for user')
#     return redirect('/somewhere/else')

@app.route('/movies/json')
def get_movies_json():
    '''route that returns json'''
    # return "{'boyhood': '{'year': 2015}'}"
    return jsonify(list(movies))


# @app.route('/example-json')
# def example_json_route():
#     '''return with some json'''
#     info = {'name': 'whiskey', 'cute': 'hella'}
#     return jsonify(info)
