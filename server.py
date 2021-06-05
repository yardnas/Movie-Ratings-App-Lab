"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud 
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """Renders Homepage"""

    return render_template('homepage.html')


@app.route('/movies')
def view_movies():
    """Displays all movies"""

    all_movies = crud.get_movies()

    return render_template('all_movies.html', all_movies=all_movies)


@app.route('/movies/<movie_id>')
def display_movie(movie_id):
    """Display details abut the movie"""

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)


@app.route('/users')
def view_users():
    """Displays all users"""

    all_users = crud.get_users()

    return render_template('all_users.html', all_users=all_users)


@app.route('/users/<user_id>')
def display_user(user_id):
    """Display details abut the user"""

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)

@app.route('/users', methods=['POST'])
def create_user():
    """Create a user"""

    email = request.form.get('email')
    password = request.form.get('password')
    
    if crud.get_user_by_email(email):
        flash('You cannot create an account withh that email. Please try again.')
    else:
        crud.create_user(email, password)
        flash('You have successfully created an account. Welcome!')

    return redirect('/')


@app.route('/users', methods=['POST'])
def log_in():
    """Log in a user"""

    #TODO
    #Create another form on homepage for login
    #get email and password
    #query for user with that email
    #if user exists
    #get password, check passwords are = 
    #add username to session
    #add a flash
    #redirect to home

    # email = request.form.get('email')
    # password = request.form.get('password')
    
    # if crud.get_user_by_email(email):
    #     flash('You cannot create an account withh that email. Please try again.')
    # else:
    #     crud.create_user(email, password)
    #     flash('You have successfully created an account. Welcome!')

    # return redirect('/')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
