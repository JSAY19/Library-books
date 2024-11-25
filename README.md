# Library Management System with GUI

## Description
This is a graphical application for managing a library system. It allows users to perform operations such as adding, deleting, searching for books, viewing all books, and updating their statuses. The interface is designed in a clean, modern, matte gray style with intuitive controls for ease of use.

## Features
1. **Add Books**: Users can add new books by entering the title, author, and year of publication.
2. **Delete Books**: Books can be removed from the library using their unique ID.
3. **Search Books**: Search for books by title or ID.
4. **View All Books**: Displays a list of all books in the library with their details:
   - ID
   - Title
   - Author
   - Year of Publication
   - Status (Available/Issued)
5. **Update Book Status**: Change the status of a book to "Available" or "Issued."
6. **Persistent Data**: The library data is stored in a JSON file (`library.json`), ensuring persistence across sessions.
7. **Modern Interface**: The application features a visually appealing gray matte GUI with styled buttons and tables.

## Requirements
- Python 3.10 or later
- Standard Python library (no external dependencies)

## Installation
1. Clone the repository or download the code.
2. Ensure you have Python installed on your machine.
3. Run the program using the command:
   ```bash
   python library_management_gui.py
   ```

## How to Use
1. Launch the program.
2. Use the buttons provided to perform desired operations:
   - **Add Book**: Enter book details and click the "Add Book" button.
   - **Delete Book**: Enter the ID of the book and click "Delete Book."
   - **Search Book**: Enter the title or ID in the search field and click "Search."
   - **View All Books**: Click the "View All Books" button.
   - **Update Status**: Select a book, choose a new status, and click "Update Status."
3. The book data will automatically be saved to `library.json`.

## File Structure
- `library_management_gui.py`: The main Python script for the application.
- `library.json`: Stores library data in JSON format. This file is created automatically after the first run.

## Future Enhancements
- Add filters for searching books by author or year.
- Enable sorting books by different fields.
- Enhance styling with custom themes.

## Screenshots
*Add a screenshot of the GUI here to demonstrate its appearance.*

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

---
Enjoy managing your library with this user-friendly system!
