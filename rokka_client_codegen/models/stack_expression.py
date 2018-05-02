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

from rokka_client_codegen.models.stack_expression_overrides import StackExpressionOverrides  # noqa: F401,E501


class StackExpression(object):
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
        'expression': 'str',
        'overrides': 'StackExpressionOverrides'
    }

    attribute_map = {
        'expression': 'expression',
        'overrides': 'overrides'
    }

    def __init__(self, expression=None, overrides=None):  # noqa: E501
        """StackExpression - a model defined in Swagger"""  # noqa: E501

        self._expression = None
        self._overrides = None
        self.discriminator = None

        self.expression = expression
        self.overrides = overrides

    @property
    def expression(self):
        """Gets the expression of this StackExpression.  # noqa: E501


        :return: The expression of this StackExpression.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this StackExpression.


        :param expression: The expression of this StackExpression.  # noqa: E501
        :type: str
        """
        if expression is None:
            raise ValueError("Invalid value for `expression`, must not be `None`")  # noqa: E501

        self._expression = expression

    @property
    def overrides(self):
        """Gets the overrides of this StackExpression.  # noqa: E501


        :return: The overrides of this StackExpression.  # noqa: E501
        :rtype: StackExpressionOverrides
        """
        return self._overrides

    @overrides.setter
    def overrides(self, overrides):
        """Sets the overrides of this StackExpression.


        :param overrides: The overrides of this StackExpression.  # noqa: E501
        :type: StackExpressionOverrides
        """
        if overrides is None:
            raise ValueError("Invalid value for `overrides`, must not be `None`")  # noqa: E501

        self._overrides = overrides

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
        if not isinstance(other, StackExpression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other