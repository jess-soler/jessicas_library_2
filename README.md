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
- Rating
  
### Data Analytics
Perform analytics on the library database to generate insights, such as:
- Most common genres or categories
- Popular authors or publishers
- Trends based on book types or publication years
- Book recommendations (API?)

### User Interface
Develop a GUI or command-line interface for users to:
- Add books via barcode scanning.
- View book details
- Search or filter books by various attributes (title, author, etc.).
- Display analytics results.

### Future Updates
- Portability: Package the project for cross-platform use with an intuitive setup.

### Goal
By the end of the project, I aim to have a fully functional library management tool that combines automation (barcode scanning and API integration), data storage, analytics, and user-friendly interfaces. 

### Week 2
- update code into new repository
- update documentation (ERD and others from Final project last term to represent the new project)
- create tables
- new wireframe!!!!!

### Week 3
- turn db_book and db_author into classes
- adjust functions to work with classes
- Make sure GUI works with new classes
- order barcode scanner
- resarch APIs for book information
- research APIs for book recommendations
- research pyzbar and opencv

### Week 4
- GUI and Database testing
- Begin Implementing barcode
  
### Week 5
- Barcode GUI
### Week 6
- Barcode API
### Week 7
- Barcode
  
### Week 8
- Data analytics tools
### Week 9
- Data analytics
### Week 10
- Data analytics
### Week 11
- Data analytics 

### Week 12
- 
### Week 13
- testing and debugging
### Week 14
- testing and debugging
### Week 15
- present

### Week 16











































This README provides a detailed overview of the program's features, usage, and setup instructions.







### Hardware Used
- ScanAvenger SA8900
- https://www.amazon.com/gp/product/B07WG1ZKZR/ref=ox_sc_act_image_14?smid=A1SP5E24FDDAMS&psc=1


# Library App

A Python ISBN barcode scanner that uses a barcode scanner (Scan Avenger SA8900) and stores the ISBN numbers in an SQLite database. I will use an API (name of API) to look up the book details using the ISBN number as save the information into a database using SQLite.  The application uses tkinter for a GUI


## Features

- Real-time barcode scanning using a barcode scanner
- Detection and storage of valid ISBN barcodes in an SQLite database
- Confirmation messages for successful barcode detection and storage
- Captured barcode frames saved as images in a 'captures' directory
- Validation of ISBN using the `isbnlib` library???????

- API to gather book details
- Store details in SQLite database
- Room for personal book reviews

- data analytics
- API to make book recommendations??

## Prerequisites

Before using the MyLibraryApp, ensure you have the following dependencies installed:

- Python 3.x
- OpenCV (`cv2`)
- `pyzbar` library
- pillow library
- `isbnlib` library?????????????
- SQLite3
- tkinter

You can install these dependencies using the following command: 

-pip install opencv-contrib-python
-pip install pyzbar
-pip install pillow
-pip install tk





## Usage

Clone the repository to your local machine:
list the main library app to run
other general directions to use the app

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






