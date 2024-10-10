# coding: utf-8

from __future__ import absolute_import
from typing import Dict

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DeleteBookResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, status: str = None, message: str = None):  # noqa: E501
        """DeleteBookResponse - a model defined in Swagger

        :param status: The status of this DeleteBookResponse.
        :type status: str
        :param message: The message of this DeleteBookResponse.
        :type message: str
        """
        self.swagger_types = {
            'status': str,
            'message': str
        }

        self.attribute_map = {
            'status': 'status',
            'message': 'message'
        }

        self._status = status
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'DeleteBookResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DeleteBookResponse of this DeleteBookResponse.
        :rtype: DeleteBookResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status(self) -> str:
        """Gets the status of this DeleteBookResponse.

        :return: The status of this DeleteBookResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this DeleteBookResponse.

        :param status: The status of this DeleteBookResponse.
        :type status: str
        """
        self._status = status

    @property
    def message(self) -> str:
        """Gets the message of this DeleteBookResponse.

        :return: The message of this DeleteBookResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this DeleteBookResponse.

        :param message: The message of this DeleteBookResponse.
        :type message: str
        """
        self._message = message

