# format_isbn.py
# jessica soler
# class to format isbn numbers using isbnlib

import isbnlib

class FormatISBN:
    def __init__(self, isbn):
        self.isbn = isbn
        
    def isbn_api(self):
        # return the isbn without dashes
        return isbnlib.canonical(self.isbn)
    
    def isbn_display(self):
        # return the isbn with dashes for display
        return isbnlib.mask(self.isbn)
    
def main():
    isbn = FormatISBN('978-3-16-148410-0')
    print(isbn.isbn_api())
    print(isbn.isbn_display())
    
if __name__ == '__main__':
    main()