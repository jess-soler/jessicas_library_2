import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# import the db_library module
import db_library

class LibraryApp:
    def __init__(self, main_app_window):
        self.main_app_window = main_app_window
        self.main_app_window.title("Jessica's Library Database")
        self.main_app_window.geometry("1200x500")
        
        # Ensure tables are created
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
      
    def create_frames(self):
        self.input_frame = tk.Frame(self.main_app_window, bd=2, relief=tk.RAISED)
        self.input_frame.place(x=100, y=10, width=380, height=240)
        
        self.button_frame = tk.Frame(self.main_app_window, bd=2, relief=tk.RAISED)
        self.button_frame.place(x=710, y=10, width=380, height=240)
        
        self.database_display_frame = tk.Frame(self.main_app_window, bd=2, relief=tk.RAISED)
        self.database_display_frame.place(x=10, y=250, width=1180, height=240)
        
    def create_buttons(self):
        self.add_book_button = tk.Button(self.button_frame, text="Add Book", command=self.call_add_book)
        self.add_book_button.pack(side="top", fill="x", padx=5, pady=7)
        
        self.edit_book_button = tk.Button(self.button_frame, text="Edit Book", command=self.call_edit_book)
        self.edit_book_button.pack(side="top", fill="x", padx=5, pady=7)
        
        self.delete_book_button = tk.Button(self.button_frame, text="Delete Book", command=self.call_delete_book)
        self.delete_book_button.pack(side="top", fill="x", padx=5, pady=7)
        
        self.save_button = tk.Button(self.button_frame, text="Save", command=self.call_save_book)
        self.save_button.pack(side="top", fill="x", padx=5, pady=7)
        
        self.clear_input_fields_button = tk.Button(self.button_frame, text="Clear Input Fields", command=self.clear_input_fields)
        self.clear_input_fields_button.pack(side="top", fill="x", padx=5, pady=7)
        
        self.close_app_button = tk.Button(self.button_frame, text="Close App", command=self.close_app)
        self.close_app_button.pack(side="top", fill="x", padx=5, pady=7)
        
    def create_input_fields(self):
        notebook = ttk.Notebook(self.input_frame)
        notebook.pack(fill="both", expand=True)
        
        book_tab = ttk.Frame(notebook)
        author_tab = ttk.Frame(notebook)
        
        notebook.add(book_tab, text="Book Details")
        notebook.add(author_tab, text="Author Details")
        
        # Book Details
        tk.Label(book_tab, text="ISBN:").pack(anchor="w")
        self.isbn_entry = tk.Entry(book_tab)
        self.isbn_entry.pack(fill="x", padx=5, pady=2)
        
        tk.Label(book_tab, text="Title:").pack(anchor="w")
        self.title_entry = tk.Entry(book_tab)
        self.title_entry.pack(fill="x", padx=5, pady=2)
        
        tk.Label(book_tab, text="Genre:").pack(anchor="w")
        self.genre_entry = tk.Entry(book_tab)
        self.genre_entry.pack(fill="x", padx=5, pady=2)
        
        tk.Label(book_tab, text="Rating (1-5):").pack(anchor="w")
        self.rating_entry = tk.Entry(book_tab)
        self.rating_entry.pack(fill="x", padx=5, pady=2)
        
        tk.Label(book_tab, text="Publication Date (YYYY):").pack(anchor="w")
        self.pub_date_entry = tk.Entry(book_tab)
        self.pub_date_entry.pack(fill="x", padx=5, pady=2)
        
        tk.Label(book_tab, text="Description:").pack(anchor="w")
        self.description_entry = tk.Entry(book_tab)
        self.description_entry.pack(fill="x", padx=5, pady=2)
        
        tk.Label(book_tab, text="Cover:").pack(anchor="w")
        self.cover_entry = tk.Entry(book_tab)
        self.cover_entry.pack(fill="x", padx=5, pady=2)
        
        # Author Details
        tk.Label(author_tab, text="Author:").pack(anchor="w")
        self.author_entry = tk.Entry(author_tab)
        self.author_entry.pack(fill="x", padx=5, pady=2)
        
    def clear_input_fields(self):
        self.isbn_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        self.rating_entry.delete(0, tk.END)
        self.pub_date_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.cover_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
     
    def create_database_display(self):
        self.database_tree = ttk.Treeview(self.database_display_frame, columns=("ID", "ISBN", "Title", "Genre", "Rating", "Publication Date", "Description", "Cover", "Author"), show="headings")
        self.database_tree.heading("ID", text="ID")
        self.database_tree.heading("ISBN", text="ISBN")
        self.database_tree.heading("Title", text="Title")
        self.database_tree.heading("Genre", text="Genre")
        self.database_tree.heading("Rating", text="Rating")
        self.database_tree.heading("Publication Date", text="Publication Date")
        self.database_tree.heading("Description", text="Description")
        self.database_tree.heading("Cover", text="Cover")
        self.database_tree.heading("Author", text="Author")
        self.database_tree.pack(fill="both", expand=True)        
        
        scrollbar = ttk.Scrollbar(self.database_display_frame, orient="vertical", command=self.database_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.database_tree.configure(yscrollcommand=scrollbar.set)
        
        self.database_tree.pack(padx=10, pady=10, fill="both", expand=True)
        self.update_database_display()
        
    def update_database_display(self):
        for item in self.database_tree.get_children():
            self.database_tree.delete(item)
            
        books = db_library.fetch_books()
        
        for record in books:
            self.database_tree.insert("", "end", text=record[0], values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]))
        
    def get_entry(self):
        isbn = self.isbn_entry.get()
        title = self.title_entry.get()
        genre = self.genre_entry.get()
        rating = self.rating_entry.get()
        pub_date = self.pub_date_entry.get()
        description = self.description_entry.get()
        cover = self.cover_entry.get()
        author = self.author_entry.get()
        
        return isbn, title, genre, rating, pub_date, description, cover, author
        
    def call_add_book(self):
        isbn, title, genre, rating, pub_date, description, cover, author = self.get_entry()
        db_library.add_book(isbn, title, genre, rating, pub_date, description, cover, author)
        self.update_database_display()
        self.clear_input_fields()
        
    def call_edit_book(self):
        selected_item = self.database_tree.selection()
        
        if not selected_item:
            messagebox.showwarning("Edit Book", "Please select a book from the database.")
            return
        
        book_details = self.database_tree.item(selected_item)["values"]
        
        self.isbn_entry.insert(0, book_details[1])
        self.title_entry.insert(0, book_details[2])
        self.genre_entry.insert(0, book_details[3])
        self.rating_entry.insert(0, book_details[4])
        self.pub_date_entry.insert(0, book_details[5])
        self.description_entry.insert(0, book_details[6])
        self.cover_entry.insert(0, book_details[7])
        self.author_entry.insert(0, book_details[8])
        
    def call_delete_book(self):
        selected_item = self.database_tree.selection()
        
        if not selected_item:
            messagebox.showwarning("Delete Book", "Please select a book from the database.")
            return
        
        book_id = self.database_tree.item(selected_item)["text"]
        db_library.delete_book(book_id)
        self.update_database_display()
        
    def call_save_book(self):
        bk_id = self.database_tree.item(self.database_tree.selection())["text"]
        isbn, title, genre, rating, pub_date, description, cover, author = self.get_entry()
        db_library.save_book(bk_id, isbn, title, genre, rating, pub_date, description, cover, author)
        self.update_database_display()
        self.clear_input_fields()
        
    def close_app(self):
        self.main_app_window.quit()
    
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)