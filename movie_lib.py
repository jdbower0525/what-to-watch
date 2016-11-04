import csv
import re
import math

def import_user_data():
    with open("test_user_data.csv") as f:
        fieldnames = ['User', 'Age', 'Gender', 'Occupation', 'ZipCode']
        user_data_reader = csv.DictReader(f, fieldnames = fieldnames, delimiter = '|')
        user_list = {}
        for row in user_data_reader:
            user_list[row['User']] = User(**row)
        print(user_list)


def import_item_data():
    with open("test_item_data.csv", encoding='latin_1') as f:
        item_data_reader = csv.DictReader(f, delimiter = '|')
        movie_list = {}
        for row in item_data_reader:
            movie_list[row["Movie_id"]] = Movie(**row)
        print(movie_list)


def import_data_data():
    with open("test_data_data.csv", encoding='latin_1') as f:
        fieldnames = ['User', 'Movie', 'Rating', 'Time_Stamp']
        data_data_reader = csv.DictReader(f, fieldnames = fieldnames, delimiter = '\t')
        rating_dict = {}
        for row in data_data_reader:
            rating_dict.setdefault(row['User'], []).append(Rating(**row))
        print(rating_dict)



class Movie:
    def __init__(self, **kwargs):
        self.movie_id = kwargs['Movie_id']
        self.title = kwargs['Title']
    def __repr__(self):
        return "\nMovie ID = {} Movie Title = {}".format(self.movie_id, self.title)

class User:
    def __init__(self, **kwargs):
        self.user_id = kwargs["User"]
        self.age = kwargs["Age"]
        self.gender = kwargs["Gender"]
        self.occupation = kwargs["Occupation"]
        self.zipcode = kwargs["ZipCode"]

    def __repr__(self):
        return "\nUser = {} User's Age = {} User's Gender = {} User's Occupation = {} User's ZipCode = {}".format(self.user_id, self.age, self.gender, self.occupation, self.zipcode)

class Rating:
    def __init__(self, **kwargs):
        self.user_id = kwargs['User']
        self.movie_id = kwargs['Movie']
        self.rating = kwargs['Rating']
        self.time_stamp = kwargs["Time_Stamp"]

    def __add__(self, other):
        if self.movie_id == other.movie_id:
            return Rating(self.movie_id, self.rating + other.rating)

    def avg_rating_by_movie_id(self):
        rating_dict = import_data_data()
        for item in rating_dict:
            if type(rating_dict['movie_id']) == type([]):
                return sum('Rating')



    def __repr__(self):
        return "\nUser = {} Movie = {} Rating = {} Time_Stamp = {}".format(self.user_id, self.movie_id, self.rating, self.time_stamp)

# import_user_data()
# import_data_data()
# import_item_data()
# a = Rating('1')
# print(a.avg_rating_by_movie_id())
