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
