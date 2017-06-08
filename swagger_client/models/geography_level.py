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


class GeographyLevel(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, country_iso=None, geo_level=None, geo_level_name=None, geo_level_description=None):
        """
        GeographyLevel - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'country_iso': 'str',
            'geo_level': 'str',
            'geo_level_name': 'str',
            'geo_level_description': 'str'
        }

        self.attribute_map = {
            'country_iso': 'country_iso',
            'geo_level': 'geo_level',
            'geo_level_name': 'geo_level_name',
            'geo_level_description': 'geo_level_description'
        }

        self._country_iso = country_iso
        self._geo_level = geo_level
        self._geo_level_name = geo_level_name
        self._geo_level_description = geo_level_description

    @property
    def country_iso(self):
        """
        Gets the country_iso of this GeographyLevel.
        3-letter country code

        :return: The country_iso of this GeographyLevel.
        :rtype: str
        """
        return self._country_iso

    @country_iso.setter
    def country_iso(self, country_iso):
        """
        Sets the country_iso of this GeographyLevel.
        3-letter country code

        :param country_iso: The country_iso of this GeographyLevel.
        :type: str
        """

        self._country_iso = country_iso

    @property
    def geo_level(self):
        """
        Gets the geo_level of this GeographyLevel.
        Geographic level of granularity

        :return: The geo_level of this GeographyLevel.
        :rtype: str
        """
        return self._geo_level

    @geo_level.setter
    def geo_level(self, geo_level):
        """
        Sets the geo_level of this GeographyLevel.
        Geographic level of granularity

        :param geo_level: The geo_level of this GeographyLevel.
        :type: str
        """

        self._geo_level = geo_level

    @property
    def geo_level_name(self):
        """
        Gets the geo_level_name of this GeographyLevel.
        Country-specific name of geography level

        :return: The geo_level_name of this GeographyLevel.
        :rtype: str
        """
        return self._geo_level_name

    @geo_level_name.setter
    def geo_level_name(self, geo_level_name):
        """
        Sets the geo_level_name of this GeographyLevel.
        Country-specific name of geography level

        :param geo_level_name: The geo_level_name of this GeographyLevel.
        :type: str
        """

        self._geo_level_name = geo_level_name

    @property
    def geo_level_description(self):
        """
        Gets the geo_level_description of this GeographyLevel.
        Description of geography level

        :return: The geo_level_description of this GeographyLevel.
        :rtype: str
        """
        return self._geo_level_description

    @geo_level_description.setter
    def geo_level_description(self, geo_level_description):
        """
        Sets the geo_level_description of this GeographyLevel.
        Description of geography level

        :param geo_level_description: The geo_level_description of this GeographyLevel.
        :type: str
        """

        self._geo_level_description = geo_level_description

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
        if not isinstance(other, GeographyLevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
