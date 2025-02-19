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
                
            # # print the data using the dictionary created from the API JSON data
            # print(f"\n{self.data.get('title')}")
            # print(f"by {self.data.get('authors')}")
            # print(f"Published: {self.data.get('publish_date')}")
            
            return self.data
        
        else:
            print("API Not Available")
            print(f"Error: {response.status_code}")
            return None                
            
            
    def get_title(self):
        return self.data.get('title')
    
    def get_authors(self):
        return self.data.get('authors')
    
    def get_publish_date(self):
        return self.data.get('publish_date')
    
    # def get_publishers(self):
    #     return self.data.get('publishers')
    
    # def get_number_of_pages(self):
    #     return self.data.get('number_of_pages')
    
    # def get_subjects(self):
    #     return self.data.get('subjects')
    
    # def get_isbn_10(self):
    #     return self.data.get('isbn_10')
    
    # def get_isbn_13(self):
    #     return self.data.get('isbn_13')
    
    # def get_cover(self):
    #     return self.data.get('cover')
    
    # def get_languages(self):
    #     return self.data.get('languages')
    
    # def get_weight(self):
    #     return self.data.get('weight')
    
    # def get_physical_dimensions(self):
    #     return self.data.get('physical_dimensions')
    
    # def get_physical_format(self):
    #     return self.data.get('physical_format')
    
    # def get_publish_places(self):
    #     return self.data.get('publish_places')
    