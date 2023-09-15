"""1

def file_status(file_path):
    try:
        with open(file_path, 'r') as file:
            is_read_only = file.readable() and not file.writable()

            is_closed = file.closed

            file_mode = file.mode

            file_name = file.name

        print(f"File Name: {file_name}")
        print(f"Read-Only: {is_read_only}")
        print(f"Closed: {is_closed}")
        print(f"File Mode: {file_mode}")

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = '/home/aman/Desktop/Concerns.txt'
file_status(file_path)
"""

"""2
user_input = input("Har Pal Har Lamha Main Kaise Sehta Hu : ")

try:
    with open('myfile.txt', 'w') as file:
        file.write(user_input)
    print("Text has been written to 'myfile.txt' successfully.")
except Exception as e:
    print(f"An error occurred: {e}")"""


"""3
try:
    with open('myfile.txt', 'r') as file:
        file_content = file.read()
        print("Content of 'myfile.txt':")
        print(file_content)
except FileNotFoundError:
    print("'myfile.txt' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
"""

"""4
city_names = [
    "New York",
    "Los Angeles",
    "Chicago",
    "San Francisco",
    "Miami",
    "Houston",
    "Boston",
]

try:
    with open('cities.txt', 'w') as file:
        for city in city_names:
            file.write(city + '\n')
    print("City names have been written to 'cities.txt' successfully.")
except Exception as e:
    print(f"An error occurred: {e}")"""

"""5
city_names = [
    "Dallas",
    "Philadelphia",
    "Seattle",
    "Denver",
    "Phoenix",
]

try:
    with open('cities.txt', 'a') as file:
        for city in city_names:
            file.write(city + '\n')
    print("City names have been appended to 'cities.txt' successfully.")
except Exception as e:
    print(f"An error occurred: {e}")"""

"""6
def search_city_in_file(city_name, file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

            cities = [line.strip() for line in lines]

            if city_name in cities:
                print(f"{city_name} is found in 'cities.txt'.")
            else:
                print(f"{city_name} is not found in 'cities.txt'.")

    except FileNotFoundError:
        print("File 'cities.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

city_to_search = input("Enter the city name you want to search for: ")

search_city_in_file(city_to_search, 'cities.txt')"""

"""7
import keyword

def count_keywords(file_name):
    try:
        with open(file_name, 'r') as file:
            source_code = file.read()

            words = source_code.split()

            keyword_count = 0

            for word in words:
                if keyword.iskeyword(word):
                    keyword_count += 1

        print(f"Number of Python keywords in '{file_name}': {keyword_count}")

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = input("Enter the name of the Python source file: ")

count_keywords(file_name)"""

"""8
import shutil

def copy_file(source_file, destination_file):
    try:
        shutil.copyfile(source_file, destination_file)
        print(f"File '{source_file}' has been copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"Source file '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file = input("Enter the path of the source file: ")
destination_file = input("Enter the path of the destination file: ")

copy_file(source_file, destination_file)
"""

"""9
import pickle

def store_book_data(book_data, file_name):
    try:
        with open(file_name, 'wb') as file:
            pickle.dump(book_data, file)
        print("Book data has been successfully stored in the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

book_data = {
    "Book1": 19.99,
    "Book2": 24.95,
    "Book3": 14.50,
}

file_name = "bookfile.pickle"

store_book_data(book_data, file_name)
"""

"""10
import pickle

def extract_book_data(file_name):
    try:
        with open(file_name, 'rb') as file:
            book_data = pickle.load(file)
            return book_data
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = "bookfile.pickle"
extracted_data = extract_book_data(file_name)

if extracted_data:
    print("Extracted Book Data:")
    for book, price in extracted_data.items():
        print(f"Book: {book}, Price: {price}")
"""