from movie_recommendation import *
import nosetests
import csv
import operator



user_data = ['125','19','F','writer','27606']
other_user_data = ['126','31','M','programmer','28562']

movie_data = ['11','Seven (Se7en) (1995)','01-Jan-1995','','http://us.imdb.com/M/title-exact?Se7en%20(1995)',
'0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','1','0','0']

rating_data = ['125','11','4','880324214']
other_rating_data = ['126','11','3','880324214']

user = User(user_data)
other_user = User(other_user_data)

movie = Movie(movie_data)

rating = Rating(rating_data)
other_rating = Rating(other_rating_data)

ratings = [rating, other_rating]
movies = [movie]
users = [user, other_user]


def test_create_user_with_attributes():
    assert user.id == '125'
    assert user.age == '19'
    assert user.gender == 'F'


def test_create_movie_with_attributes():
    assert movie.id == '11'
    assert movie.title == 'Seven (Se7en)'


def test_create_rating_with_attributes():
    assert rating.user_id == '125'
    assert rating.item_id == '51'
    assert rating.rating == '5'
