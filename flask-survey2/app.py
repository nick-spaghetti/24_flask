from flask import Flask, request, render_template, redirect, flash, session, make_response
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys

app = Flask(__name__)
app.secret_key = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
responses_key = 'responses'
current_survey_key = 'current_survey'
debug = DebugToolbarExtension


@app.route('/')
def show_pick_survey_form():
    return render_template('pick_survey.html', surveys=surveys)


@app.route('/begin', methods=['post'])
def pick_survey():
    survey = surveys[survey_id]
    survey_id = request.form['survey_code']
    if request.cookies.get(f'completed_{survey_id}'):
        return render_template('already_done.html')
    session[current_survey_key] = survey_id
    return render_template('survey_start.html', survey=survey)


@app.route('/answer', methods=['post'])
def handle_question():
    choice = request.form['answer']
    text = request.form.get('text', '')
    responses = session[responses_key]
    responses.append({'choice': choice, 'text': text})
    session[responses_key] = responses
    survey_code = session[current_survey_key]
    survey = surveys[survey_code]
    if(len(responses) == len(survey.questions)):
        return redirect('/complete')
    else:
        return redirect(f'/questions/{len(responses)}')


@app.route('/questions/<int:qid>')
def show_question(qid):
    responses = session.get(responses_key)
    survey_code = session[current_survey_key]
    survey = surveys[survey_code]
    if (responses is None):
        return redirect('/')
    if (len(responses) == len(survey.questions)):
        return redirect('/complete')
    if (len(responses) != qid):
        flash(f'invalid question id: {qid}')
        return redirect(f'/questions/{len(responses)}')
    question = survey.questions[qid]
    return render_template('question.html', question_num=qid, question=question)


@app.route('/complete')
def say_thanks():
    responses = session[responses_key]
    survey_id = session[current_survey_key]
    survey = surveys[survey_id]
    html = render_template('complete.html', survey=survey, responses=responses)
    response = make_response(html)
    response.set_cookie(f'completed_{survey_id}', 'yes', max_age=60)
    return response
