from flask import Flask, request, redirect, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
#import cgi
import os
import jinja2


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:homer@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

#app = Flask(__name__)
#app.config['DEBUG'] = True

class Blog(db.Model):

    post_id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(120))
    post_body = db.Column(db.String(120))
    #post_date = datetime.utcnow()
    post_date = db.Column(db.DateTime)

    #def __init__(self, name):
        #self.name = name
    def __init__(self, title, body, date ):
        self.title = post_title 
        self.body = post_body
        self.date = datetime.utcnow()


#@app.route('/', methods=['POST', 'GET'])
@app.route('/',)
def index():
    template = jinja_env.get_template("blog.html")
    return template.render()

@app.route('/blog', methods=['GET', 'POST'])
def blog():
    if request.method == 'POST':
        post_name = request.form['post']
        new_post = post(post_name)
        db.session.add(new_post)
        db.session.commit()
    else:
        ##posts = Blog.query.fetchall()
        ##posts = Blog.fetchall()
        posts = Blog.query.all()
        ##completed_tasks = Task.query.filter_by(completed=True).all()
        return render_template('blog.html',title="Blog Posts!",posts=posts) #completed_tasks=completed_tasks)


@app.route('/new_post', methods=['POST'])
def new_post():
    template = jinja_env.get_template("new_post.html")
    return template.render()


if __name__ == '__main__':
    app.run()
    
    #posts = Post.query.filter_by(completed=False).all()
    #completed_tasks = Post.query.filter_by(completed=True).all()
    #return render_template('posts.html',title="Get It Done!", 
        #posts=posts, completed_posts=completed_posts)

#return redirect('/')

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
