import csv


def import_user_data():
    with open("test_user_data.csv") as f:
        user_data_reader = csv.DictReader(f, delimiter = '|')
        return user_data_reader

def import_item_data():
    with open("test_item_data.csv", encoding='latin_1') as f:
        item_data_reader = csv.DictReader(f, delimiter = '|')
        for row in item_data_reader:
            print(row)
        return item_data_reader

def import_data_data():
    with open("test_data_data.csv", encoding='latin_1') as f:
        fieldnames = ['User', 'Movie', 'Rating', 'Time_Stamp']
        data_data_reader = csv.DictReader(f, fieldnames=fieldnames, delimiter = '\t')
        for row in data_data_reader:
            print(row)
        return data_data_reader


class Movie:
    def __init__(self, title, movie_id):
        self.title = title
        self.movie_id = movie_id


class User:
    def __init__(self, user_id, rating):
        self.user_id = user_id
        self.rating = rating


class Rating:
    def __init__(self, **kwargs):
        pass
        #self.Movie = kwargs['Movie']
        #self.Rating = kwargs['Rating']

    def rating_search(self):
        pass


dict1 = {}
my_dict = import_user_data()
for row in my_dict:
    dict1.append(row)
print(dict1)
# for row in item_data_reader:
#     print(row)
# rating = Rating()
# rating.rating_search()



# import_user_data()
# import_data_data()
# import_item_data()

#def main():
#    print(User.import_user_data())
