import json
import tkinter as tk
from tkinter import ttk, messagebox

class LibraryManagementSystem:
    def __init__(self, root, data_file="library.json"):
        self.data_file = data_file
        self.books = self.load_books()
        self.root = root
        self.root.title("Library books by Danya Superechenko")
        self.root.configure(bg="#2e2e2e")

        self.create_widgets()

    def load_books(self):
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self):
        with open(self.data_file, "w") as file:
            json.dump(self.books, file, indent=4)

    def generate_id(self):
        return max((book["id"] for book in self.books), default=0) + 1

    def add_book(self):
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        year = self.year_entry.get().strip()

        if not title or not author or not year.isdigit():
            messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля корректно.")
            return

        book = {
            "id": self.generate_id(),
            "title": title,
            "author": author,
            "year": int(year),
            "status": "в наличии"
        }
        self.books.append(book)
        self.save_books()
        self.update_table()

    def delete_book(self):
        try:
            selected_item = self.table.selection()[0]
            book_id = int(self.table.item(selected_item)['values'][0])
            self.books = [book for book in self.books if book["id"] != book_id]
            self.save_books()
            self.update_table()
            messagebox.showinfo("Успех", f"Книга с ID: {book_id} успешно удалена.")
        except IndexError:
            messagebox.showerror("Ошибка", "Пожалуйста, выберите книгу для удаления.")

    def search_books(self):
        query = self.search_entry.get().strip().lower()
        if not query:
            messagebox.showerror("Ошибка", "Введите название книги или ID для поиска.")
            return

        if query.isdigit():
            results = [book for book in self.books if book["id"] == int(query)]
        else:
            results = [book for book in self.books if query in book["title"].lower()]

        if results:
            self.update_table(results)
        else:
            messagebox.showinfo("Результат поиска", "Книги не найдены.")

    def update_table(self, books=None):
        for row in self.table.get_children():
            self.table.delete(row)

        if books is None:
            books = self.books

        for book in books:
            self.table.insert("", "end", values=(book["id"], book["title"], book["author"], book["year"], book["status"]))

    def change_status(self):
        try:
            selected_item = self.table.selection()[0]
            book_id = int(self.table.item(selected_item)['values'][0])
            new_status = self.status_combobox.get()

            if new_status not in ["в наличии", "выдана"]:
                messagebox.showerror("Ошибка", "Некорректный статус.")
                return

            for book in self.books:
                if book["id"] == book_id:
                    book["status"] = new_status
                    break

            self.save_books()
            self.update_table()
        except IndexError:
            messagebox.showerror("Ошибка", "Пожалуйста, выберите книгу для изменения статуса.")

    def create_widgets(self):
        # Добавление книги
        form_frame = tk.Frame(self.root, bg="#2e2e2e")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Название:", bg="#2e2e2e", fg="white").grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = tk.Entry(form_frame)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Автор:", bg="#2e2e2e", fg="white").grid(row=1, column=0, padx=5, pady=5)
        self.author_entry = tk.Entry(form_frame)
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Год:", bg="#2e2e2e", fg="white").grid(row=2, column=0, padx=5, pady=5)
        self.year_entry = tk.Entry(form_frame)
        self.year_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(form_frame, text="Добавить книгу", command=self.add_book, bg="#39352a", fg="white").grid(row=3, column=0, columnspan=2, pady=10)

        # Поиск книги
        search_frame = tk.Frame(self.root, bg="#2e2e2e")
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="Поиск (Название или ID):", bg="#2e2e2e", fg="white").grid(row=0, column=0, padx=5, pady=5)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(search_frame, text="Найти", command=self.search_books, bg="#2196f3", fg="white").grid(row=0, column=2, padx=5, pady=5)

        # Таблица книг
        self.table = ttk.Treeview(self.root, columns=("ID", "Название", "Автор", "Год", "Статус"), show="headings")
        self.table.heading("ID", text="ID")
        self.table.heading("Название", text="Название")
        self.table.heading("Автор", text="Автор")
        self.table.heading("Год", text="Год")
        self.table.heading("Статус", text="Статус")
        self.table.pack(pady=10, fill=tk.BOTH, expand=True)

        # Изменение статуса
        status_frame = tk.Frame(self.root, bg="#2e2e2e")
        status_frame.pack(pady=10)

        tk.Label(status_frame, text="Изменить статус:", bg="#2e2e2e", fg="white").grid(row=0, column=0, padx=5, pady=5)
        self.status_combobox = ttk.Combobox(status_frame, values=["в наличии", "выдана"], state="readonly")
        self.status_combobox.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(status_frame, text="Обновить статус", command=self.change_status, bg="#ff9800", fg="white").grid(row=0, column=2, padx=5, pady=5)

        # Удаление книги
        tk.Button(self.root, text="Удалить книгу", command=self.delete_book, bg="#f44336", fg="white").pack(pady=10)

        self.update_table()

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()
