from fastapi import FastAPI, HTTPException, Body
from books import BOOKS
app = FastAPI()

@app.get('/api/v1/books')
async def get_books():
    return {'Books':BOOKS}

@app.get('/api/v1/books/{book_name}')
async def get_books_by_name(book_name:str):
    for book in BOOKS:
        if book['title'].casefold() == book_name.casefold():
            return book
    raise HTTPException(404,"Book not found")

@app.get('/api/v1/books/')
async def get_books_by_category(category:str):
    books =[]
    for book in BOOKS:
        if book['category'].casefold() == category.casefold():
             books.append(book)
    if books == []:
      raise HTTPException(404,"Book not found")
    return books

@app.get('/api/v1/books/{book_author}/')
async def get_books_by_author_and_category(book_author:str,category:str):
    books =[]
    for book in BOOKS:
        if (book['category'].casefold() == category.casefold()) and (book['author'].casefold()==book_author.casefold()):
             books.append(book)
    if books == []:
      raise HTTPException(404,"Book not found")
    return books

@app.post('/api/v1/books')
async def create_book(book=Body()):
    BOOKS.append(book)
    return await get_books_by_name(book['title'])

@app.delete('/api/v1/books/{book_name}')
async def delete_book(book_name:str):
    for i in range(len(BOOKS)):
        if BOOKS[i]['title'].casefold() == book_name.casefold():
            del BOOKS[i]
            break
    return "Book Deleted Sucessfully"

@app.put('/api/v1/books')
async def update_book(book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i]['title'].casefold() == book['title'].casefold():
            BOOKS[i] = book
    return await get_books_by_name(book['title'])
