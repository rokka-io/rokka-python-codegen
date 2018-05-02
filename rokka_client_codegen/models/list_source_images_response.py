# coding: utf-8

"""
    rokka.io

    digital image processing done right. [Documentation](https://rokka.io/documentation). [Changelog](https://api.rokka.io/changelog.md).  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from rokka_client_codegen.models.source_image import SourceImage  # noqa: F401,E501


class ListSourceImagesResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'total': 'int',
        'items': 'list[SourceImage]',
        'cursor': 'str',
        'links': 'object'
    }

    attribute_map = {
        'total': 'total',
        'items': 'items',
        'cursor': 'cursor',
        'links': 'links'
    }

    def __init__(self, total=None, items=None, cursor=None, links=None):  # noqa: E501
        """ListSourceImagesResponse - a model defined in Swagger"""  # noqa: E501

        self._total = None
        self._items = None
        self._cursor = None
        self._links = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if items is not None:
            self.items = items
        if cursor is not None:
            self.cursor = cursor
        if links is not None:
            self.links = links

    @property
    def total(self):
        """Gets the total of this ListSourceImagesResponse.  # noqa: E501


        :return: The total of this ListSourceImagesResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListSourceImagesResponse.


        :param total: The total of this ListSourceImagesResponse.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def items(self):
        """Gets the items of this ListSourceImagesResponse.  # noqa: E501


        :return: The items of this ListSourceImagesResponse.  # noqa: E501
        :rtype: list[SourceImage]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ListSourceImagesResponse.


        :param items: The items of this ListSourceImagesResponse.  # noqa: E501
        :type: list[SourceImage]
        """

        self._items = items

    @property
    def cursor(self):
        """Gets the cursor of this ListSourceImagesResponse.  # noqa: E501


        :return: The cursor of this ListSourceImagesResponse.  # noqa: E501
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """Sets the cursor of this ListSourceImagesResponse.


        :param cursor: The cursor of this ListSourceImagesResponse.  # noqa: E501
        :type: str
        """

        self._cursor = cursor

    @property
    def links(self):
        """Gets the links of this ListSourceImagesResponse.  # noqa: E501


        :return: The links of this ListSourceImagesResponse.  # noqa: E501
        :rtype: object
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ListSourceImagesResponse.


        :param links: The links of this ListSourceImagesResponse.  # noqa: E501
        :type: object
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSourceImagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
