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


class Error(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, code=None, message=None, fields=None):
        """
        Error - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'code': 'int',
            'message': 'str',
            'fields': 'str'
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message',
            'fields': 'fields'
        }

        self._code = code
        self._message = message
        self._fields = fields

    @property
    def code(self):
        """
        Gets the code of this Error.

        :return: The code of this Error.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Error.

        :param code: The code of this Error.
        :type: int
        """

        self._code = code

    @property
    def message(self):
        """
        Gets the message of this Error.

        :return: The message of this Error.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this Error.

        :param message: The message of this Error.
        :type: str
        """

        self._message = message

    @property
    def fields(self):
        """
        Gets the fields of this Error.

        :return: The fields of this Error.
        :rtype: str
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this Error.

        :param fields: The fields of this Error.
        :type: str
        """

        self._fields = fields

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
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
