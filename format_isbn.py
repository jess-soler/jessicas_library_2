# format_isbn.py
# jessica soler
# class to format isbn numbers using isbnlib

import isbnlib

class FormatISBN:
    def __init__(self, isbn):
        self.isbn = isbn
        
    def isbn_api(self):
        """return the isbn without dashes"""
        
        try:
            if isbnlib.is_isbn13(self.isbn):
                return isbnlib.canonical(self.isbn)
            elif isbnlib.is_isbn10(self.isbn):
                return isbnlib.canonical(isbnlib.to_isbn13(self.isbn))
            else:
                raise ValueError("Invalid ISBN")
        except Exception as e:
            return str(e)

    
    def isbn_display(self):
        """return the isbn with dashes for display"""
        
        try:
            if isbnlib.is_isbn13(self.isbn) or isbnlib.is_isbn10(self.isbn):
                return isbnlib.mask(self.isbn)
            else:
                raise ValueError("Invalid ISBN")
        except Exception as e:
            return str(e)
        
        
def main():
    isbn = FormatISBN('978-3-16-148410-0')
    print(isbn.isbn_api())
    print(isbn.isbn_display())
    
    ten_digit_isbn = FormatISBN('0-439-02348-3')
    print(ten_digit_isbn.isbn_api())
    print(ten_digit_isbn.isbn_display())
    
if __name__ == '__main__':
    main()