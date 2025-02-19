# import requests for api use
import requests
# import json for json data handling
import json


"""
    Bibliography class
    Take ISBN from user input in app.py
    Use Open Books API to get book information
"""
    
class Bibliography():
    def __init__(self, isbn):
        self.isbn = isbn
        
        # set this to False to only display the data
        self.IS_DEBUGGING = True
        
        # Open Library API URL        
        self.URL = f"https://openlibrary.org/isbn/{self.isbn}.json"
        
        
        
        self.book_info = self.get_book_info()
        self.book_info = self.book_info[0]
        self.title = self.book_info['volumeInfo']['title']
        self.author = self.book_info['volumeInfo']['authors'][0]
        self.genre = self.book_info['volumeInfo']['categories'][0]
        self.rating = self.book_info['volumeInfo']['averageRating']
        self.pub_date = self.book_info['volumeInfo']['publishedDate']
        self.description = self.book_info['volumeInfo']['description']
        self.cover = self.book_info['volumeInfo']['imageLinks']['thumbnail']
        self.auth_id = self.get_author_id()
        
    def get_book_info(self):
        # use the requests.get() function
        # with the parameter of the self.URL
        response = requests.get(self.URL)
        
        # if the status_code is 200, successful connection and data
        if (response.status_code == 200):
            
            # convert the JSON data into a Python dictionary with key value pairs
            self.data = response.json()
            
            # used to debug process
            if (self.IS_DEBUGGING == True):
                
                # display the status code
                print(f"\nStatus Code: {response.status_code}")
                
                # display the raw JSON data from the API
                print("\nData from API:")
                print(response.text)
                
                # display the Python dictionary
                print("\nData as Python Dictionary:")
                print(self.data)
                
            