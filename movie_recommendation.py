import csv
import sys
from movie_lib import *

movie_ratings = import_data_item()
user_dict = import_data_user()
top_avg_list = average_ranks()
movie_dict = import_movie_data()

def get_movie_id():
    movie_id = input("What movie (by movie ID) would you like to choose? ")
    return movie_id

def get_user_id():
    user_id = input("What user (by ID) would you like to choose? ")
    return user_id

def get_all_ratings_for_movie(user_input):
    return movie_ratings[user_input]


def name_of_movie_by_id(user_input):
    return movie_dict[user_input]

def average_movie_rating(user_input):
    movie_dict = import_data_item()
    rating_list = movie_dict[user_input]
    average_rating = sum(rating_list) / len(rating_list)
    return average_rating

def get_all_ratings_for_user(user_input):
    user_dict = import_data_user()
    user_ratings = user_dict[user_input]
    return user_ratings

def see_top_ten_by_avg():
    top_avg_movies = []
    i = 0
    for item in top_avg_list:
        top_avg_movies.append((movie_dict[item[0]].get_name(item[0]), top_avg_list[i][1]))
        print(top_avg_movies[i])
        i += 1
    return top_avg_movies

def main_menu():
    while True:
        user_input = input("""Select an option (1-5):
        1 - Search for a movie (by movie ID)
        2 - Search for the ratings of a movie (by movie ID)
        3 - Look at the average rating of a movie (by movie ID)
        4 - Look at all movies rated by a user (by user ID)
        5 - Look at the top 10 rated movies
        6 - Exit
        >>> """)

        if user_input == '1':
            print(name_of_movie_by_id(get_movie_id()))
            continue
        if user_input == '2':
            print(get_all_ratings_for_movie(get_movie_id()))
            continue
        elif user_input == '3':
            print(average_movie_rating(get_movie_id()))
            continue
        elif user_input == '4':
            print(get_all_ratings_for_user(get_user_id()))
            continue
        elif user_input == '5':
            see_top_ten_by_avg()
        else:
            exit()

def main():
    read_files()
    main_menu()

main()
if __name__ == '__main__':
    main()
