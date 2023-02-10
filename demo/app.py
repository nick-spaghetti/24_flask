from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home_page():
    '''return home '''
    html = '<html><body><h1>home</h1><p>welcome to my simple app</p><a href="/hello">go to hello page</a></body></html>'
    return html


@app.route('/hello')
def say_hello():
    '''return simple hello greeting'''
    html = '<html><body><h1>hello</h1></body></html>'
    return html


@app.route('/goodbye')
def say_goodbye():
    '''return simple goodbye '''
    html = '<html><body><h1>goodbye</h1></body></html>'
    return html


@app.route('/search')
def search():
    term = request.args['term']
    return f'<h1>searching for {term}</h1>'


@app.route('/post', methods=['POST'])
def post_demo():
    return 'you made a post request'


@app.route('/post', methods=['GET'])
def get_demo():
    return 'you made a get request'


@app.route('/add-comment')
def add_comment_form():
    '''show form for adding a comment'''
    return '''
		<form method="POST">
			<input name="comment" type="text" placeholder="comment" />
			<input name="username" type="text" placeholder="username" />
			<button>submit</button>
		</form>
	'''


@app.route('/add-comment', methods=['POST'])
def add_comment():
    '''handle adding comment'''
    comment = request.form['comment']
    username = request.form['username']
    # todo: save that into a database
    print(request.form)
    return f'''
    <h1>saved your comment</h1> 
    <ul>
    <li>username: {username}</li>
    <li>comment: {comment}</li>
    </ul>
    '''


users = {
    'whiskey': 'whiskey the dog',
    'spike': 'spike the porcupine'
}


# < ------  # brackets turn that into a variable
@app.route('/user/<username>')
def show_user_profile(username):  # < ------  # passed as keyword argument
    """show user profile for user"""
    name = users[username]
    return f'<h1>profile for {name}</h1>'


posts = {
    1: 'i like chicken tenders',
    2: 'i hate mayo',
    3: 'double rainbow all the way',
    4: 'yolo omg kill me'
}


@app.route('/posts/<int:post_id>')
def find_post(post_id):
    print('post_id is a ', type(post_id))
    # post_id = POSTS[id]
    post_id = POSTS.get(id, 'post not found')
    return f'<p>{post_id}</p>'


@app.route('/r/<subreddit>/comments/<int:post_id>')
def show_comments(subreddit, post_id):
    return f'<h1>viewing comments for {post_id} from the {subreddit} subreddit</h1>'
