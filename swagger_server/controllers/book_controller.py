import connexion
import six
from swagger_server.models.book import Book  # noqa: E501
from swagger_server.models.create_book_request import CreateBookRequest  # noqa: E501
from swagger_server.models.create_book_response import CreateBookResponse  # noqa: E501
from swagger_server.models.delete_book_response import DeleteBookResponse  # noqa: E501
from swagger_server.models.list_books_response import ListBooksResponse  # noqa: E501
from swagger_server.models.update_book_request import UpdateBookRequest  # noqa: E501
from swagger_server.models.update_book_response import UpdateBookResponse  # noqa: E501
from swagger_server import util

# In-memory storage for books
books = {}
book_counter = 1  # Simple counter to simulate book IDs

def create_book(book):  # noqa: E501
    """create_book

    :param book: 
    :type book: dict | bytes

    :rtype: CreateBookResponse
    """
    global book_counter
    if connexion.request.is_json:
        book_request = CreateBookRequest.from_dict(connexion.request.get_json())  # noqa: E501
        
        # Create a new book and assign an ID
        new_book = Book(
            id=book_counter,
            title=book_request.title,
            author=book_request.author,
            description=book_request.description
        )
        books[book_counter] = new_book
        book_counter += 1
        
        return CreateBookResponse(message="Book created successfully", book=new_book), 201  # 201 Created

def delete_book(bookID):  # noqa: E501
    """delete_book

    :param bookID: 
    :type bookID: str

    :rtype: DeleteBookResponse
    """
    book_id = int(bookID)
    if book_id in books:
        del books[book_id]
        return DeleteBookResponse(message="Book deleted successfully"), 200  # 200 OK
    else:
        return DeleteBookResponse(message="Book not found"), 404  # 404 Not Found

def get_book_by_id(bookID):  # noqa: E501
    """get_book_by_id

    :param bookID: 
    :type bookID: str

    :rtype: Book
    """
    book_id = int(bookID)
    book = books.get(book_id)
    if book:
        return book, 200  # 200 OK
    else:
        return 'Book not found', 404  # 404 Not Found

def list_books():  # noqa: E501
    """list_books

    :rtype: ListBooksResponse
    """
    return ListBooksResponse(books=list(books.values())), 200  # 200 OK

def update_book(bookID, book):  # noqa: E501
    """update_book

    :param bookID: 
    :type bookID: str
    :param book: 
    :type book: dict | bytes

    :rtype: UpdateBookResponse
    """
    if connexion.request.is_json:
        book_request = UpdateBookRequest.from_dict(connexion.request.get_json())  # noqa: E501
        
        book_id = int(bookID)
        if book_id in books:
            # Update the existing book details
            existing_book = books[book_id]
            existing_book.title = book_request.title
            existing_book.author = book_request.author
            existing_book.description = book_request.description
            
            return UpdateBookResponse(message="Book updated successfully", book=existing_book), 200  # 200 OK
        else:
            return UpdateBookResponse(message="Book not found"), 404  # 404 Not Found

