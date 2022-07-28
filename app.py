from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config["SECRET_KEY"] = 'madlib'

debug = DebugToolbarExtension(app)


@app.route('/')
def choose_story():
    '''Show stories to choose from'''

    return render_template('story-selector.html', stories=stories.values())

@app.route('/questions')
def question_form():
    '''Generate homepage and madlib questions'''

    story_id = request.args['story_id']
    story = stories[story_id]
    prompts = story.prompts

    return render_template('home.html', prompts=prompts, story_id=story_id, title=story.title)

@app.route('/story')
def generate_story():
    '''Generate Madlib story'''
    story_id = request.args['story_id']
    story = stories[story_id]
    text = story.generate(request.args)

    return render_template('story.html', text=text, title=story.title)