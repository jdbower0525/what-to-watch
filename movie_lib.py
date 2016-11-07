import csv

class User:

    def __init__(self, **kwargs):
        self.user_id = kwargs["user_id"]
        self.age = kwargs["age"]
        self.gender = kwargs["gender"]
        self.job = kwargs["job"]
        self.zip_code = kwargs["zip_code"]

    def __repr__(self):
        return "User ID: " + self.user_id + " age: " + self.age


class Movie:

    def __init__(self, **kwargs):
        self.title = kwargs['title']
        self.movie_id = kwargs["movie_id"]

    def get_name(self, movie_id):
        return self.title

    def __repr__(self):
        return self.title[:-7]


class Rating:

    def __init__(self, **kwargs):
        self.item_id = kwargs["item_id"]
        self.rating = kwargs["rating"]
        self.user_id = kwargs["user_id"]

    def __repr__(self):
        return self.rating + " " + self.user_id + " " + self.item_id


def import_data_item():
    with open("u.data.csv", encoding= 'latin_1') as data_file:
        data_reader = csv.DictReader(data_file, fieldnames= ['user_id', 'item_id', 'rating', 'timestamp'],  delimiter='\t')
        item_rating_dict = {}
        for row in data_reader:
            item_rating_dict.setdefault(row["item_id"], []).append(int(row['rating']))
        return item_rating_dict


def import_data_user():
    with open("u.data.csv", encoding= 'latin_1') as data_file:
        data_reader = csv.DictReader(data_file, fieldnames= ['user_id', 'item_id', 'rating', 'timestamp'],  delimiter='\t')
        user_rating_dict = {}
        for row in data_reader:
            user_rating_dict.setdefault(row["user_id"], []).append(row['item_id'])
        return user_rating_dict


def import_user_data():
    with open("u.user.csv",  encoding= 'latin_1') as f:
        user_reader = csv.DictReader(f, delimiter= "|")
        user_dict = {}
        for row in user_reader:
            user_dict[row['user_id']] = User(**row)
        return user_dict


def import_movie_data():
    with open("u.item.csv", encoding= 'latin_1') as movie_file:
        movie_reader = csv.DictReader(movie_file, delimiter= "|")
        movie_dict = {}
        for row in movie_reader:
            movie_dict[row["movie_id"]] = Movie(**row)
        return movie_dict

def average_ranks():
    with open('u.data.csv') as f:
        fieldnames = ['user_id', 'item_id', 'rating', 'timestamp']
        average_reader = csv.DictReader(f, fieldnames = fieldnames, delimiter = '\t')
        dictionary_ranked_movies = {}
        dictionary_ranked_top = {}
        i = 0
        for row in average_reader:
            dictionary_ranked_movies.setdefault(row['item_id'], []).append(Rating(**row))
        for k in dictionary_ranked_movies:
            sum_ratings_all = 0
            i = 0
            for item in dictionary_ranked_movies[k]:
                sum_ratings_all += (int(dictionary_ranked_movies[k][i].rating))
                i += 1
            if i >= 300:
                (dictionary_ranked_top[k]) = (sum_ratings_all/i)
        return(sorted(dictionary_ranked_top.items(), key = lambda x: x[1], reverse = True))

def read_files():
    import_movie_data()
    import_user_data()
    import_data_user()
    import_data_item()
    average_ranks()
