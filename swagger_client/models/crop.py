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


class Crop(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, crop_uid=None, crop_display_name=None, crop_type_code=None, crop_type_display_name=None, country_iso=None, start_date=None, end_date=None, active=None):
        """
        Crop - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'crop_uid': 'int',
            'crop_display_name': 'str',
            'crop_type_code': 'str',
            'crop_type_display_name': 'str',
            'country_iso': 'str',
            'start_date': 'str',
            'end_date': 'str',
            'active': 'bool'
        }

        self.attribute_map = {
            'crop_uid': 'crop_uid',
            'crop_display_name': 'crop_display_name',
            'crop_type_code': 'crop_type_code',
            'crop_type_display_name': 'crop_type_display_name',
            'country_iso': 'country_iso',
            'start_date': 'start_date',
            'end_date': 'end_date',
            'active': 'active'
        }

        self._crop_uid = crop_uid
        self._crop_display_name = crop_display_name
        self._crop_type_code = crop_type_code
        self._crop_type_display_name = crop_type_display_name
        self._country_iso = country_iso
        self._start_date = start_date
        self._end_date = end_date
        self._active = active

    @property
    def crop_uid(self):
        """
        Gets the crop_uid of this Crop.
        Unique identifier for a given crop

        :return: The crop_uid of this Crop.
        :rtype: int
        """
        return self._crop_uid

    @crop_uid.setter
    def crop_uid(self, crop_uid):
        """
        Sets the crop_uid of this Crop.
        Unique identifier for a given crop

        :param crop_uid: The crop_uid of this Crop.
        :type: int
        """

        self._crop_uid = crop_uid

    @property
    def crop_display_name(self):
        """
        Gets the crop_display_name of this Crop.
        Crop display name

        :return: The crop_display_name of this Crop.
        :rtype: str
        """
        return self._crop_display_name

    @crop_display_name.setter
    def crop_display_name(self, crop_display_name):
        """
        Sets the crop_display_name of this Crop.
        Crop display name

        :param crop_display_name: The crop_display_name of this Crop.
        :type: str
        """

        self._crop_display_name = crop_display_name

    @property
    def crop_type_code(self):
        """
        Gets the crop_type_code of this Crop.
        3-letter crop code

        :return: The crop_type_code of this Crop.
        :rtype: str
        """
        return self._crop_type_code

    @crop_type_code.setter
    def crop_type_code(self, crop_type_code):
        """
        Sets the crop_type_code of this Crop.
        3-letter crop code

        :param crop_type_code: The crop_type_code of this Crop.
        :type: str
        """

        self._crop_type_code = crop_type_code

    @property
    def crop_type_display_name(self):
        """
        Gets the crop_type_display_name of this Crop.
        Display name for a given crop type

        :return: The crop_type_display_name of this Crop.
        :rtype: str
        """
        return self._crop_type_display_name

    @crop_type_display_name.setter
    def crop_type_display_name(self, crop_type_display_name):
        """
        Sets the crop_type_display_name of this Crop.
        Display name for a given crop type

        :param crop_type_display_name: The crop_type_display_name of this Crop.
        :type: str
        """

        self._crop_type_display_name = crop_type_display_name

    @property
    def country_iso(self):
        """
        Gets the country_iso of this Crop.
        3-letter country code

        :return: The country_iso of this Crop.
        :rtype: str
        """
        return self._country_iso

    @country_iso.setter
    def country_iso(self, country_iso):
        """
        Sets the country_iso of this Crop.
        3-letter country code

        :param country_iso: The country_iso of this Crop.
        :type: str
        """

        self._country_iso = country_iso

    @property
    def start_date(self):
        """
        Gets the start_date of this Crop.
        Start date for TellusLabs crop yield coverage

        :return: The start_date of this Crop.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this Crop.
        Start date for TellusLabs crop yield coverage

        :param start_date: The start_date of this Crop.
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this Crop.
        End date for TellusLabs crop yield coverage

        :return: The end_date of this Crop.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this Crop.
        End date for TellusLabs crop yield coverage

        :param end_date: The end_date of this Crop.
        :type: str
        """

        self._end_date = end_date

    @property
    def active(self):
        """
        Gets the active of this Crop.
        In growing season

        :return: The active of this Crop.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this Crop.
        In growing season

        :param active: The active of this Crop.
        :type: bool
        """

        self._active = active

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
        if not isinstance(other, Crop):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
