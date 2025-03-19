# format_isbn.py
# jessica soler
# class to format isbn numbers using isbnlib

import isbnlib

class FormatISBN:
    def __init__(self, isbn):
        self.isbn = isbn
        
    def isbn_valid(self):
        """verifies isbn is valid and returns boolean"""
        
        try:
            # check if the ISBN is valid 13 digit or 10 digit
            if isbnlib.is_isbn13(self.isbn) or isbnlib.is_isbn10(self.isbn):
                return True
            else:
                return False
        except Exception as e:
            return str(e)
        
    def isbn_api(self):
        """return the isbn without dashes"""
        
        try:
            # check if the ISBN is valid 13 digit or 10 digit
            # canonical means to remove dashes and spaces
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
            # check if the ISBN is valid 13 digit or 10 digit
            # mask means to add dashes
            if isbnlib.is_isbn13(self.isbn) or isbnlib.is_isbn10(self.isbn):
                return isbnlib.mask(self.isbn)
            else:
                raise ValueError("Invalid ISBN")
        except Exception as e:
            return str(e)
        
        
def main():
    """test the FormatISBN class"""
    
    # 13 digit ISBN
    isbn = FormatISBN('978-3-16-148410-0')
    print(isbn.isbn_api())
    print(isbn.isbn_display())
    
    # 10 digit ISBN
    ten_digit_isbn = FormatISBN('0-439-02348-3')
    print(ten_digit_isbn.isbn_api())
    print(ten_digit_isbn.isbn_display())
    
    # invalid ISBN
    invalid_isbn = FormatISBN('1234567890')
    print(invalid_isbn.isbn_api())
    print(invalid_isbn.isbn_display())
    
if __name__ == '__main__':
    main()