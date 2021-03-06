# coding: utf-8

"""
    Kernel API

    Access Kernel insights programmatically

    OpenAPI spec version: 0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TableRow(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'crop': 'str',
        'data': 'list[float]',
        'date': 'date',
        'geography': 'Geography'
    }

    attribute_map = {
        'crop': 'crop',
        'data': 'data',
        'date': 'date',
        'geography': 'geography'
    }

    def __init__(self, crop=None, data=None, date=None, geography=None):
        """
        TableRow - a model defined in Swagger
        """

        self._crop = None
        self._data = None
        self._date = None
        self._geography = None

        if crop is not None:
          self.crop = crop
        if data is not None:
          self.data = data
        if date is not None:
          self.date = date
        if geography is not None:
          self.geography = geography

    @property
    def crop(self):
        """
        Gets the crop of this TableRow.

        :return: The crop of this TableRow.
        :rtype: str
        """
        return self._crop

    @crop.setter
    def crop(self, crop):
        """
        Sets the crop of this TableRow.

        :param crop: The crop of this TableRow.
        :type: str
        """

        self._crop = crop

    @property
    def data(self):
        """
        Gets the data of this TableRow.

        :return: The data of this TableRow.
        :rtype: list[float]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this TableRow.

        :param data: The data of this TableRow.
        :type: list[float]
        """

        self._data = data

    @property
    def date(self):
        """
        Gets the date of this TableRow.

        :return: The date of this TableRow.
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this TableRow.

        :param date: The date of this TableRow.
        :type: date
        """

        self._date = date

    @property
    def geography(self):
        """
        Gets the geography of this TableRow.

        :return: The geography of this TableRow.
        :rtype: Geography
        """
        return self._geography

    @geography.setter
    def geography(self, geography):
        """
        Sets the geography of this TableRow.

        :param geography: The geography of this TableRow.
        :type: Geography
        """

        self._geography = geography

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, TableRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
