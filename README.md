# jessicas_library_2
added functionality to my library database project

# TODO:
### Barcode Scanning for Book Entry
- use a barcode scanner to scan a book's barcode (ISBN)
- Automatically decode the barcode to retrieve the ISBN number
- Fetch book details (title, author, publisher, publication date, rating) using the ISBN through an external API
- Save the retrieved book details to the library database

### SQLite database
Store book information in a relational database with fields for:
- Title
- Author(s)
- Publisher
- Publication Date
- Description
- Book Cover Image
- Rating
  
### Data Analytics
Perform analytics on the library database to generate insights, such as:
- Most common genres or categories
- Popular authors or publishers
- Trends based on book types or publication years
- Book recommendations (API?)
- NumPy, MatPlotLib, Pandas, SciPy, or Seaborn
- Get Book Recommendations 

### User Interface
Develop a GUI or command-line interface for users to:
- Add books via barcode scanning.
- View book details
- Allow manual entry for missing book details
- Search or filter books by various attributes (title, author, etc.).
- Display analytics results


### Future Updates
- Portability: Package the project for cross-platform use with an intuitive setup.

### Goal
By the end of the project, I aim to have a fully functional library management tool that combines automation (barcode scanning and API integration), data storage, analytics, and user-friendly interfaces. 

### DOCUMENTATION NEEDED TO DO
- update documentation (ERD and others from Final project last term to represent the new project)
- create tables
- new wireframe!!!!!

### CLASS ORGANIZATION TODO
- turn db_book and db_author into classes
- adjust functions to work with classes
- Make sure GUI works with new classes

### APIS FOR BOOK REVTRIEVAL/RECOMMENDATIONS TODO
- Open Library API
- Amazon???
- Google???
- other???  

### OTHER TODO 
- order barcode scanner
- Begin Implementing barcode
- Research libraries for data analytics
- Research API and JSON file handling
- Research 5 stars/book cover imaging into tkinter treeview
- 
  
### TESTING TODO
- GUI and Database testing
- Error handling for missing ISBN records


 










































This README provides a detailed overview of the program's features, usage, and setup instructions.


# Library App

A Python-based library application that uses a barcode scanner to capture ISBN numbers.  The application queries the Open Library API to fetch book details based on the ISBN number and saves them in an SQLite database. The database will be managed with a Tkinter GUI.

Using (libraries) pyzbar to decode the one-dimensional barcode and QR code. 

### Hardware Used
- ScanAvenger SA8900
- https://www.amazon.com/gp/product/B07WG1ZKZR/ref=ox_sc_act_image_14?smid=A1SP5E24FDDAMS&psc=1

- 
## Features

- Real-time barcode scanning using SA8900 barcode scanner
- ISBN validation using the isbnlib library **********
- Open Library API integration for fetching book details ******************
- SQLite database storage for book records
- Tkinter GUI for managing book records
- Personal rating system (displays star ratings) *****************
- Data analytics ********************
      - most popular genre
      - amounts of books per genre
      - list of 5 star books
      - list of 1 star books
      - least owned genre
      - most owned genre
- Book recommendations based on stored data ************


## Prerequisites

Before using the MyLibraryApp, ensure you have the following dependencies installed:

- Python 3.x
- OpenCV (`cv2`)
- `pyzbar` library
- pillow library
- `isbnlib` library?????????????
- SQLite3
- tkinter
- matplotlib
- requests (for API use)

You can install these dependencies using the following command: 

- pip install opencv-contrib-python
- pip install pyzbar
- pip install pillow
- pip install tk
- pip install matplotlib
- pip install requests





## Usage

Clone the repository to your local machine:
list the MAIN_APP_NAME to run
other general directions to use the app

- Scan an ISBN barcode → Scanner types the number into the isbn_entry field.
- Scanner sends "Enter" key → on_barcode_scanned function is triggered.
- Fetch book details from Open Library API using ISBN.
- Store book details in an SQLite database.
- Show confirmation message when added successfully.

## Configuration

The program contains a few configuration options:

????
- Captured barcode frames are saved in a 'captures' directory. You can change this directory's name or location by modifying the save_capture function.

## Additional Notes

DISCUSS THE DIFFERENT MODULES HERE!!!!!!!!!!
The BarcodeScanner class provides methods for creating the database table, checking for existing ISBNs, storing ISBNs, and more.
The is_valid_isbn method validates ISBNs using the isbnlib library, checking both ISBN-10 and ISBN-13 formats.
The capture_barcode method continuously captures frames, detects barcodes, and stores ISBNs until you exit the program.

## Contribution

Contributions to this project are welcome! If you encounter any issues, have ideas for improvements, or want to add new features, feel free to submit a pull request or open an issue.

## License

This barcode scanner is open-source and licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

This program utilizes the OpenCV library for computer vision tasks. Credits to the OpenCV community for their contributions.

The development of this application benefited from the assistance of language models, including GPT-3.5 and GPT-4, provided by OpenAI. The author acknowledges the valuable contributions made by these language models in generating design ideas and providing insights during the development process.






