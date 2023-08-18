from bs4 import BeautifulSoup
import os

import pandas as pd

def nameCleaner(name):
    return name[0:name.index("-Notebook")]

def chooseBookFile(books):
    # List out all the books
    for i, book in enumerate(books):
        print(f"{i+1}. {book}")
    # Return the corresponding book
    return books[int(input("Choose your book: "))-1]

def getBookAndNotes():
    # Gets list of books
    books = os.listdir("htmls")
    choice = chooseBookFile(books)

    # Opens book you chose
    with open(f"htmls/{choice}") as book:
        # Reads every line looking for noteText 
        soup = BeautifulSoup(book.read(), 'html.parser')
        notes = soup.findAll(class_="noteText")
        
        # Only retrieves the note, not the Heading
        notes = stripNotes(notes)

    return nameCleaner(choice), notes

def stripNotes(notes):
    for note in range(len(notes)):
        notes[note] = notes[note].get_text().strip().split("Highlight (")[0]

    return notes

def addToExcel(book, notes):
    # book = book.replace(" ", "-")
    books = pd.DataFrame({book:notes})
    books.to_excel(f"csvs/{book}.xlsx")

def main():
    book, notes = getBookAndNotes()
    addToExcel(book, notes)


if __name__ == "__main__":
    main()
