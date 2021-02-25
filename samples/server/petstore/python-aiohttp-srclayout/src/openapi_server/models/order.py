# coding: utf-8

from datetime import date, datetime

from typing import List, List, Type

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Order(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, pet_id: int=None, quantity: int=None, ship_date: datetime=None, status: str=None, complete: bool=False):
        """Order - a model defined in OpenAPI

        :param id: The id of this Order.
        :param pet_id: The pet_id of this Order.
        :param quantity: The quantity of this Order.
        :param ship_date: The ship_date of this Order.
        :param status: The status of this Order.
        :param complete: The complete of this Order.
        """
        self.openapi_types = {
            'id': int,
            'pet_id': int,
            'quantity': int,
            'ship_date': datetime,
            'status': str,
            'complete': bool
        }

        self.attribute_map = {
            'id': 'id',
            'pet_id': 'petId',
            'quantity': 'quantity',
            'ship_date': 'shipDate',
            'status': 'status',
            'complete': 'complete'
        }

        self._id = id
        self._pet_id = pet_id
        self._quantity = quantity
        self._ship_date = ship_date
        self._status = status
        self._complete = complete

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Order':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Order of this Order.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Order.


        :return: The id of this Order.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Order.


        :param id: The id of this Order.
        :type id: int
        """

        self._id = id

    @property
    def pet_id(self):
        """Gets the pet_id of this Order.


        :return: The pet_id of this Order.
        :rtype: int
        """
        return self._pet_id

    @pet_id.setter
    def pet_id(self, pet_id):
        """Sets the pet_id of this Order.


        :param pet_id: The pet_id of this Order.
        :type pet_id: int
        """

        self._pet_id = pet_id

    @property
    def quantity(self):
        """Gets the quantity of this Order.


        :return: The quantity of this Order.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Order.


        :param quantity: The quantity of this Order.
        :type quantity: int
        """

        self._quantity = quantity

    @property
    def ship_date(self):
        """Gets the ship_date of this Order.


        :return: The ship_date of this Order.
        :rtype: datetime
        """
        return self._ship_date

    @ship_date.setter
    def ship_date(self, ship_date):
        """Sets the ship_date of this Order.


        :param ship_date: The ship_date of this Order.
        :type ship_date: datetime
        """

        self._ship_date = ship_date

    @property
    def status(self):
        """Gets the status of this Order.

        Order Status

        :return: The status of this Order.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Order.

        Order Status

        :param status: The status of this Order.
        :type status: str
        """
        allowed_values = ["placed", "approved", "delivered"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def complete(self):
        """Gets the complete of this Order.


        :return: The complete of this Order.
        :rtype: bool
        """
        return self._complete

    @complete.setter
    def complete(self, complete):
        """Sets the complete of this Order.


        :param complete: The complete of this Order.
        :type complete: bool
        """

        self._complete = complete
