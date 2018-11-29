from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:homer@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Blog(db.Model):

    # specify the data fields that should go into columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(2048))
    date = db.Column(db.DateTime) 

    #def __init__(self, id, title, body):
    def __init__(self, title, body):
    #def __init__(self, post_title):
        #self.id = id
        self.title = title
        self.body = body
        self.date = datetime.utcnow()

"""
    def __repr__(self):
        return '<Blog #r>' % self.title
        #return '<Blog>' % self.title
"""
# TODO The /blog route displays all the blog posts.

@app.route('/')
def index():
    all_blog_posts = Blog.query.all()
    return render_template('blog.html', posts=all_blog_posts)
    #return render_template('blog.html', posts=posts)
    

# DISPLAYS IND BLOG POSTS
@app.route('/blog')
def show_blog():
    post_id = request.args.get('id')
    if (post_id):
        #ind_post = Blog.query.get(post_id)
        single = Blog.query.get(post_id)
        #return render_template('ind_post.html', ind_post=ind_post)
        return render_template('single.html', single=single)
    else:
        #post_id = request.args.get('id')
        all_blog_posts = Blog.query.all()
        return render_template('blog.html', posts=all_blog_posts)
        #return render_template('blog.html', posts=posts)


# Empty field toggle
def empty_field(f):
    if f:
        return True
    else:
        return False
    

# THIS HANDLES THE REDIRECT (SUCCESS) AND ERROR MESSAGES (FAILURE)

@app.route('/newpost', methods=['POST', 'GET'])
def new_post():

    if request.method == 'POST':

        title_error = ""
        blog_entry_error = ""

        post_title = request.form['blog_title']
        post_entry = request.form['blog_post']
        post_new = Blog(post_title, post_entry)

        # if the title and post entry are not empty, the object will be added
    
        if empty_field(post_title) and empty_field(post_entry):
            db.session.add(post_new)
            db.session.commit()
            post_link = "/blog?id=" + str(post_new.id)
            return redirect(post_link)

        else:
            if not empty_field(post_title) and not empty_field(post_entry):
                #flash('Please enter text for blog title')
                title_error = "Please enter text for blog title"
                blog_entry_error = "Please enter text for blog entry"
                return render_template('new_post.html', blog_entry_error=blog_entry_error, title_error=title_error)
                #return redirect('/newpost')
            elif not empty_field(post_title):
                title_error = "Please enter text for blog title"
                #flash('Please enter text for blog title')
                return render_template('new_post.html', title_error=title_error, post_entry=post_entry)
                #return redirect('/newpost')
            elif not empty_field(post_entry):
                blog_entry_error = "Please enter text for blog entry"
                #flash('Please enter text for blog entry')
                return render_template('new_post.html', blog_entry_error=blog_entry_error, post_title=post_title)
                #return redirect('/newpost')

    # DISPLAYS NEW BLOG ENTRY FORM
    else:
        return render_template('new_post.html')
        

# only runs when the main.py file run directly
if __name__ == '__main__':
    app.run()