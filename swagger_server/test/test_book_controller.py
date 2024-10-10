# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.book import Book  # noqa: E501
from swagger_server.models.create_book_request import CreateBookRequest  # noqa: E501
from swagger_server.models.create_book_response import CreateBookResponse  # noqa: E501
from swagger_server.models.delete_book_response import DeleteBookResponse  # noqa: E501
from swagger_server.models.list_books_response import ListBooksResponse  # noqa: E501
from swagger_server.models.update_book_request import UpdateBookRequest  # noqa: E501
from swagger_server.models.update_book_response import UpdateBookResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBookController(BaseTestCase):
    """BookController integration test stubs"""

    def test_create_book(self):
        """Test case for creating a book."""
        book = CreateBookRequest()  # Assuming default values or set values as needed.
        response = self.client.open(
            '/v1/book',
            method='POST',
            data=json.dumps(book.to_dict()),  # Ensure we convert to dict for JSON serialization
            content_type='application/json'
        )
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))

    def test_delete_book(self):
        """Test case for deleting a book."""
        response = self.client.open(
            '/v1/book/{bookID}'.format(bookID='bookID_example'),
            method='DELETE',
            content_type='application/json'
        )
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))

    def test_get_book_by_id(self):
        """Test case for retrieving a book by ID."""
        response = self.client.open(
            '/v1/book/{bookID}'.format(bookID='bookID_example'),
            method='GET',
            content_type='application/json'
        )
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))

    def test_list_books(self):
        """Test case for listing all books."""
        response = self.client.open(
            '/v1/book',
            method='GET',
            content_type='application/json'
        )
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))

    def test_update_book(self):
        """Test case for updating a book."""
        book = UpdateBookRequest()  # Assuming default values or set values as needed.
        response = self.client.open(
            '/v1/book/{bookID}'.format(bookID='bookID_example'),
            method='PUT',
            data=json.dumps(book.to_dict()),  # Ensure we convert to dict for JSON serialization
            content_type='application/json'
        )
        self.assert200(response, 'Response body is: ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
