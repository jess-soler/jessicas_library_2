"""
    Name: app.py
    Author: Jessica Soler
    Date: 1/20/25
    Purpose: 
"""
# GUI Library
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# import the db_library module
import db_library



#----Class----------------------------------------------------------------------------------------------------#
class LibraryApp:
    def __init__(self, main_app_window):
        self.main_app_window = main_app_window
        self.main_app_window.title("Jessica's Library Database")
        self.main_app_window.geometry("1200x900")
        
        self.barcode = ""
        
        # create tables
        db_library.create_tables()
        
        # set up frames - database, input fields, and buttons
        self.create_frames()
        
        # set up buttons
        self.create_buttons()
        
        # set up input fields
        self.create_input_fields()
        
        # set up database display
        self.create_database_display()
        
        # run window
        self.main_app_window.mainloop()
      
      
      
#---GUI FUNCTIONS----------------------------------------------------------------------------------------------------#  
    def create_frames(self):
        """
            upper left frame = input fields
            bd=2 means border width is 2 pixels
            relief=tk.RAISED means the border is raised
        """
        self.input_frame = tk.Frame(self.main_app_window, bd=2, relief=tk.RAISED)
        
        
        """
            main_app_window is 1200 pixels wide
            the input_frame is in the upper left corner
            1200/2 = 600 with 100 pixels of padding on each side = 700
            frame width = 380 pixels
            main_app_window is 500 pixels tall
            the input_frame is in the upper left corner
            500/2 = 250 with 10 pixels of padding on each side = 240
        """
        self.input_frame.place(x=10, y=10, width=380, height=340)
        # title for the input frame
        tk.Label(self.input_frame, text="Book Details").pack()
        
        # upper right frame = buttons
        """
            upper right frame is 400 pixels wide
            but it needs to be placed 710 pixels from the left side
            the input_frame is 380 pixels wide
            the input_frame is 100 pixels from the left side
            410 + 380 + 10 = 800
        """
        self.button_frame = tk.Frame(self.main_app_window, bd=2, relief=tk.RAISED)
        self.button_frame.place(x=410, y=10, width=380, height=340)
        # title for the buttons frame
        tk.Label(self.button_frame, text="Book Database Functions").pack()
        
        # barcode frame to be put underneath the input frame
        self.barcode_frame = tk.Frame(self.main_app_window, bd=2, relief=tk.RAISED)
        self.barcode_frame.place(x=800, y=10, width=380, height=340)
        
        
        # bottom half frame = database display
        """
            database_display frame is the bottom half of the window
            the bottom half frame is 1200 pixels wide
            1200 - 20 = 1180 pixels wide with 10 padding on each side
            it is placed 550 pixels from the top with 10 padding on top
            500 - 10 = 490 pixels tall with 10 padding on top
        """
        self.database_display_frame = tk.Frame(self.main_app_window, bd=2, relief=tk.RAISED)
        self.database_display_frame.place(x=10, y=450, width=1180, height=340)
        # title for the database display frame
        tk.Label(self.database_display_frame, text="Scanner").pack()
        

        
             
    def create_buttons(self):
        # add, edit, delete, save, clear input fields, close buttons
        
        # add book button
        # used format from AI code
        self.add_book_button = tk.Button(self.button_frame, text="Add Book", command=self.call_add_book)
        self.add_book_button.pack(side="top", fill="x", padx=5, pady=7)
        
        # edit book button
        # used format from AI code
        self.edit_book_button = tk.Button(self.button_frame, text="Edit Book", command=self.call_edit_book)
        self.edit_book_button.pack(side="top", fill="x", padx=5, pady=7)
        
        # delete book button
        # used format from AI code
        self.delete_book_button = tk.Button(self.button_frame, text="Delete Book", command=self.call_delete_book)
        self.delete_book_button.pack(side="top", fill="x", padx=5, pady=7)
        
        # save button
        # used format from AI code
        self.save_button = tk.Button(self.button_frame, text="Save", command=self.call_save_book)
        self.save_button.pack(side="top", fill="x", padx=5, pady=7)
        
        # clear input fields button
        # used format from AI code
        self.clear_input_fields_button = tk.Button(self.button_frame, text="Clear Input Fields", command=self.clear_input_fields)
        self.clear_input_fields_button.pack(side="top", fill="x", padx=5, pady=7)
        
        # close app button
        # used format from AI code
        self.close_app_button = tk.Button(self.button_frame, text="Close App", command=self.close_app)
        self.close_app_button.pack(side="top", fill="x", padx=5, pady=7)
        
        # clear database button
        # used format from AI code
        # self.clear_database_button = tk.Button(self.button_frame, text="Clear Database", command=self.call_clear_database)
        # self.clear_database_button.pack(side="top", fill="x", padx=5, pady=0)
        
        # scan barcode button
        self.scan_barcode_button = tk.Button(self.barcode_frame, text="Scan Barcode", command=self.call_scan_barcode)
        self.scan_barcode_button.pack(side="top", fill="x", padx=5, pady=7)
        
        # search ISBN button
        self.search_isbn_button = tk.Button(self.barcode_frame, text="Search ISBN", command=self.call_format_isbn)
        self.search_isbn_button.pack(side="top", fill="x", padx=5, pady=7)
        
    def create_input_fields(self):
        # title, author, genre, rating, pub_date
        # AI Code, edited
        
        # ISBN input field
        tk.Label(self.input_frame, text="ISBN:").pack(anchor="w")
        self.isbn_entry = tk.Entry(self.input_frame)
        self.isbn_entry.pack(fill="x", padx=5, pady=2)
        
        # Title input field
        tk.Label(self.input_frame, text="Title:").pack(anchor="w")
        self.title_entry = tk.Entry(self.input_frame)
        self.title_entry.pack(fill="x", padx=5, pady=2)

        # Author input field
        tk.Label(self.input_frame, text="Author:").pack(anchor="w")
        self.author_entry = tk.Entry(self.input_frame)
        self.author_entry.pack(fill="x", padx=5, pady=2)

        # Genre input field
        tk.Label(self.input_frame, text="Genre:").pack(anchor="w")
        self.genre_entry = tk.Entry(self.input_frame)
        self.genre_entry.pack(fill="x", padx=5, pady=2)

        # Rating input field
        tk.Label(self.input_frame, text="Rating (1-5):").pack(anchor="w")
        self.rating_entry = tk.Entry(self.input_frame)
        self.rating_entry.pack(fill="x", padx=5, pady=2)

        # Publication Date input field
        tk.Label(self.input_frame, text="Publication Date (YYYY):").pack(anchor="w")
        self.pub_date_entry = tk.Entry(self.input_frame)
        self.pub_date_entry.pack(fill="x", padx=5, pady=2)
    
    
    def clear_input_fields(self):
        # AI Code
        self.isbn_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        self.rating_entry.delete(0, tk.END)
        self.pub_date_entry.delete(0, tk.END)
     
         
    def create_database_display(self):
        # create a treeview to display the database
        # AI Code, edited
        self.tree = ttk.Treeview(self.database_display_frame, columns=("ID", "ISBN", "Title", "Author", "Genre", "Rating", "Publication Date"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("ISBN", text="ISBN")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Author", text="Author")
        self.tree.heading("Genre", text="Genre")
        self.tree.heading("Rating", text="Rating")
        self.tree.heading("Publication Date", text="Publication Date")
        self.tree.pack(fill="both", expand=True)        
        
        # add a scrollbar
        scrollbar = ttk.Scrollbar(self.database_display_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

        self.update_treeview()


    def update_treeview(self):
        # AI Code
        
        # clear the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # fetch updated records from the database
        books = db_library.fetch_books()
        
        # insert the updated records into the treeview
        for book in books:
            self.tree.insert("", "end", values=book)
        
        
        
#---WRAPPER FUNCTIONS----------------------------------------------------------------------------------------------------#
# Call to: db_library.py
# Add, Edit, Save, Delete, Close

    def get_entry(self):
        # .get() function to get the text from the entry field
        isbn = self.isbn_entry.get()
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        rating = self.rating_entry.get()
        pub_date = self.pub_date_entry.get()
        
        return isbn, title, author, genre, rating, pub_date


    def call_add_book(self):
        
        # get the book details from the input fields
        isbn, title, author, genre, rating, pub_date = self.get_entry()

        # call database function to add a book
        db_library.add_book(isbn, title, author, genre, rating, pub_date)
        
        # update the treeview after adding a book
        self.update_treeview()
        
        # clear fields after adding a book
        self.clear_input_fields()
        
        
    def call_edit_book(self):
        # select item from the treeview
        selected_item = self.tree.selection()
        
        if not selected_item:
            messagebox.showwarning("Edit Book", "Please select a book from the database.")
            return
        
        # save the tuple as book_details
        book_details = self.tree.item(selected_item)["values"]
   
# indexes?!?!     
# AI Code
# populate input fields with current details
        self.isbn_entry.insert(0, book_details[1])
        self.title_entry.insert(0, book_details[2])
        self.author_entry.insert(0, book_details[3])
        self.genre_entry.insert(0, book_details[4])
        self.rating_entry.insert(0, book_details[5])
        self.pub_date_entry.insert(0, book_details[6])
        
        
    def call_delete_book(self):
        selected_item = self.tree.selection()
        
        if not selected_item:
            messagebox.showwarning("Delete Book", "Please select a book from the database.")
            return
        
        book_id = self.tree.item(selected_item)["values"][0]
        db_library.delete_book(book_id)
        self.update_treeview()
        
        
    def call_save_book(self):
        
        # .get() the text from the entry field
        bk_id = self.tree.item(self.tree.selection())["values"][0]
        bk_isbn = self.isbn_entry.get()
        bk_title = self.title_entry.get()
        bk_author = self.author_entry.get()
        bk_genre = self.genre_entry.get()
        bk_rating = self.rating_entry.get()
        bk_pub_date = self.pub_date_entry.get()  
        db_library.save_book(bk_id, bk_isbn, bk_title, bk_author, bk_genre, bk_rating, bk_pub_date)
        
        self.update_treeview()
        self.clear_input_fields()
        
        
    def close_app(self):
        self.main_app_window.quit()
    
    # def call_clear_database(self):
    #     db_library.clear_database()
    #     self.update_treeview()
    
    def call_scan_barcode(self):
        """ The call_scan_barcode method sets the focus to the isbn_entry field
        when the "scan barcode" button is clicked.
        The isbn_entry field is bound to the <return> event, which triggers the capture_barcode method
        the capture_barcode method caputres the barcode input from the isbn_entry field and processes it"""
        # set focus to the isbn_entry field
        self.isbn_entry.focus()
        
    def capture_barcode(self, event):
        """ The capture_barcode method captures the barcode input from the isbn_entry field and processes it"""
        self.isbn = self.isbn_entry.get()
        # add barcode to the input field
        self.isbn_entry.delete(0, tk.END)
        self.isbn_entry.insert(0, self.isbn)
        self.get_bibliography(self.isbn)
        

        
        

# initialize tkinter and run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    
#MOVE DATABASE INITIALIZATION HERE???
