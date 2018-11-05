#testing push crap from home.
from flask import request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:homer@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):

    post_id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(120))
    post_body = db.Column(db.String(120))
    post_date = db.Column(db.DateTime)

    def __init__(self, name):
        self.name = name


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        post_name = request.form['post']
        new_post = Post(post_name)
        db.session.add(new_post)
        db.session.commit()

    posts = Post.query.filter_by(completed=False).all()
    completed_tasks = Post.query.filter_by(completed=True).all()
    return render_template('posts.html',title="Get It Done!", 
        posts=posts, completed_posts=completed_posts)

        <form action="https://duckduckgo.com" method="get">
            <label for="search-term">Search term:</label>
            <input id="search-term" type="text" name="q" />
            <input type="submit" />
        </form>

# TODO The /blog route displays all the blog posts.

# TODO You're able to submit a new post at the /newpost route. 
# After submitting a new post, your app displays the main blog page.

# TODO You have two templates, one each for the /blog (main blog listings) 
# and /newpost (post new blog entry) views. 
# Your templates should extend a base.html template which includes some 
# boilerplate HTML that will be used on each page.

# TODO In your base.html template, you have some navigation links that 
# link to the main blog page and to the add new blog page.

# TODO If either the blog title or blog body is left empty in the new post form, 
# the form is rendered again, with a helpful error message and any 
# previously-entered content in the same form inputs.

# TODO For both use cases we need to create the template for the page that will display an individual blog, 
# so start by making that. All it need do is display a blog title and blog body. 
# Next, we'll tackle the use cases one at a time.

# TODO Use Case 1: 
# We click on a blog entry's title on the main page and go to a blog's individual entry page.

# TODO Use Case 2: 
# After adding a new blog post, instead of going back to the main page, 
# we go to that blog post's individual entry page.

# TODO Bonus Missions 
# 1. Add a CSS stylesheet to improve the style of your app. You can read about how to do so here.

# 2. Display the posts in order of most recent to the oldest (the opposite of the current order). 
# You can either use the id property that has been created using auto-incrementing, 
# or - a more sophisticated method - you can add a DateTime property to the Blog class 
# (and drop and re-create the table) that will store the date the post was created in the database. 
# For an example of an app with a DateTime column, check out this quickstart guide.
