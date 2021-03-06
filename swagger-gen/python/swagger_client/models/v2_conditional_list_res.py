# coding: utf-8

"""
    Bybit API

    ## REST API for the Bybit Exchange. Base URI: [https://api.bybit.com]    # noqa: E501

    OpenAPI spec version: 0.2.10
    Contact: support@bybit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V2ConditionalListRes(object):
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
        'user_id': 'float',
        'stop_order_status': 'str',
        'symbol': 'str',
        'side': 'str',
        'order_type': 'str',
        'price': 'str',
        'qty': 'str',
        'time_in_force': 'str',
        'stop_order_type': 'str',
        'trigger_by': 'str',
        'base_price': 'str',
        'order_link_id': 'str',
        'stop_px': 'str',
        'stop_order_id': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'stop_order_status': 'stop_order_status',
        'symbol': 'symbol',
        'side': 'side',
        'order_type': 'order_type',
        'price': 'price',
        'qty': 'qty',
        'time_in_force': 'time_in_force',
        'stop_order_type': 'stop_order_type',
        'trigger_by': 'trigger_by',
        'base_price': 'base_price',
        'order_link_id': 'order_link_id',
        'stop_px': 'stop_px',
        'stop_order_id': 'stop_order_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, user_id=None, stop_order_status=None, symbol=None, side=None, order_type=None, price=None, qty=None, time_in_force=None, stop_order_type=None, trigger_by=None, base_price=None, order_link_id=None, stop_px=None, stop_order_id=None, created_at=None, updated_at=None):  # noqa: E501
        """V2ConditionalListRes - a model defined in Swagger"""  # noqa: E501

        self._user_id = None
        self._stop_order_status = None
        self._symbol = None
        self._side = None
        self._order_type = None
        self._price = None
        self._qty = None
        self._time_in_force = None
        self._stop_order_type = None
        self._trigger_by = None
        self._base_price = None
        self._order_link_id = None
        self._stop_px = None
        self._stop_order_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if stop_order_status is not None:
            self.stop_order_status = stop_order_status
        if symbol is not None:
            self.symbol = symbol
        if side is not None:
            self.side = side
        if order_type is not None:
            self.order_type = order_type
        if price is not None:
            self.price = price
        if qty is not None:
            self.qty = qty
        if time_in_force is not None:
            self.time_in_force = time_in_force
        if stop_order_type is not None:
            self.stop_order_type = stop_order_type
        if trigger_by is not None:
            self.trigger_by = trigger_by
        if base_price is not None:
            self.base_price = base_price
        if order_link_id is not None:
            self.order_link_id = order_link_id
        if stop_px is not None:
            self.stop_px = stop_px
        if stop_order_id is not None:
            self.stop_order_id = stop_order_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def user_id(self):
        """Gets the user_id of this V2ConditionalListRes.  # noqa: E501


        :return: The user_id of this V2ConditionalListRes.  # noqa: E501
        :rtype: float
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this V2ConditionalListRes.


        :param user_id: The user_id of this V2ConditionalListRes.  # noqa: E501
        :type: float
        """

        self._user_id = user_id

    @property
    def stop_order_status(self):
        """Gets the stop_order_status of this V2ConditionalListRes.  # noqa: E501


        :return: The stop_order_status of this V2ConditionalListRes.  # noqa: E501
        :rtype: str
        """
        return self._stop_order_status

    @stop_order_status.setter
    def stop_order_status(self, stop_order_status):
        """Sets the stop_order_status of this V2ConditionalListRes.


        :param stop_order_status: The stop_order_status of this V2ConditionalListRes.  # noqa: E501
        :type: str
        """

        self._stop_order_status = stop_order_status

    @property
    def symbol(self):
        """Gets the symbol of this V2ConditionalListRes.  # noqa: E501


        :return: The symbol of this V2ConditionalListRes.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this V2ConditionalListRes.


        :param symbol: The symbol of this V2ConditionalListRes.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def side(self):
        """Gets the side of this V2ConditionalListRes.  # noqa: E501


        :return: The side of this V2ConditionalListRes.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this V2ConditionalListRes.


        :param side: The side of this V2ConditionalListRes.  # noqa: E501
        :type: str
        """

        self._side = side

    @property
    def order_type(self):
        """Gets the order_type of this V2ConditionalListRes.  # noqa: E501


        :return: The order_type of this V2ConditionalListRes.  # noqa: E501
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this V2ConditionalListRes.


        :param order_type: The order_type of this V2ConditionalListRes.  # noqa: E501
        :type: str
        """

        self._order_type = order_type

    @property
    def price(self):
        """Gets the price of this V2ConditionalListRes.  # noqa: E501


        :return: The price of this V2ConditionalListRes.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this V2ConditionalListRes.


        :param price: The price of this V2ConditionalListRes.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def qty(self):
        """Gets the qty of this V2ConditionalListRes.  # noqa: E501


        :return: The qty of this V2ConditionalListRes.  # noqa: E501
        :rtype: str
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """Sets the qty of this V2ConditionalListRes.


        :param qty: The qty of this V2ConditionalListRes.  # noqa: E501
        :type: str
        """

        self._qty = qty

    @property
    def time_in_force(self):
        """Gets the time_in_force of this V2ConditionalListRes.  # noqa: E501


        :return: The time_in_force of this V2ConditionalListRes.  # noqa: E501
        :rtype: str
        """
        return self._time_in_force

    @time_in_force.setter
    def time_in_force(self, time_in_force):
        """Sets the time_in_force of this V2ConditionalListRes.


        :param time_in_force: The time_in_force of this V2ConditionalListRes.  # noqa: E501
        :type: str
        """

        self._time_in_force = time_in_force

    @property
    def stop_order_type(self):
        """Gets the stop_order_type of this V2ConditionalListRes.  # noqa: E501


        :return: The stop_order_type of this V2ConditionalListRes.  # noqa: E501
        :rtype: str
        """
        return self._stop_order_type

    @stop_order_type.setter
    def stop_order_type(self, stop_order_type):
        """Sets the stop_order_type of this V2ConditionalListRes.


        :param stop_order_type: The stop_order_type of this V2ConditionalListRes.  # noqa: E501
        :type: str
        """

        self._stop_order_type = stop_order_type

    @property
    def trigger_by(self):
        """Gets the trigger_by of this V2ConditionalListRes.  # noqa: E501


        :return: The trigger_by of this V2ConditionalListRes.  # noqa: E501
        :rtype: str
        """
        return self._trigger_by

    @trigger_by.setter
    def trigger_by(self, trigger_by):
        """Sets the trigger_by of this V2ConditionalListRes.


        :param trigger_by: The trigger_by of this V2ConditionalListRes.  # noqa: E501
        :type: str
        """

        self._trigger_by = trigger_by

    @property
    def base_price(self):
        """Gets the base_price of this V2ConditionalListRes.  # noqa: E501


        :return: The base_price of this V2ConditionalListRes.  # noqa: E501
        :rtype: str
        """
        return self._base_price

    @base_price.setter
    def base_price(self, base_price):
        """Sets the base_price of this V2ConditionalListRes.


        :param base_price: The base_price of this V2ConditionalListRes.  # noqa: E501
        :type: str
        """

        self._base_price = base_price

    @property
    def order_link_id(self):
        """Gets the order_link_id of this V2ConditionalListRes.  # noqa: E501


        :return: The order_link_id of this V2ConditionalListRes.  # noqa: E501
        :rtype: str
        """
        return self._order_link_id

    @order_link_id.setter
    def order_link_id(self, order_link_id):
        """Sets the order_link_id of this V2ConditionalListRes.


        :param order_link_id: The order_link_id of this V2ConditionalListRes.  # noqa: E501
        :type: str
        """

        self._order_link_id = order_link_id

    @property
    def stop_px(self):
        """Gets the stop_px of this V2ConditionalListRes.  # noqa: E501


        :return: The stop_px of this V2ConditionalListRes.  # noqa: E501
        :rtype: str
        """
        return self._stop_px

    @stop_px.setter
    def stop_px(self, stop_px):
        """Sets the stop_px of this V2ConditionalListRes.


        :param stop_px: The stop_px of this V2ConditionalListRes.  # noqa: E501
        :type: str
        """

        self._stop_px = stop_px

    @property
    def stop_order_id(self):
        """Gets the stop_order_id of this V2ConditionalListRes.  # noqa: E501


        :return: The stop_order_id of this V2ConditionalListRes.  # noqa: E501
        :rtype: str
        """
        return self._stop_order_id

    @stop_order_id.setter
    def stop_order_id(self, stop_order_id):
        """Sets the stop_order_id of this V2ConditionalListRes.


        :param stop_order_id: The stop_order_id of this V2ConditionalListRes.  # noqa: E501
        :type: str
        """

        self._stop_order_id = stop_order_id

    @property
    def created_at(self):
        """Gets the created_at of this V2ConditionalListRes.  # noqa: E501


        :return: The created_at of this V2ConditionalListRes.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this V2ConditionalListRes.


        :param created_at: The created_at of this V2ConditionalListRes.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this V2ConditionalListRes.  # noqa: E501


        :return: The updated_at of this V2ConditionalListRes.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this V2ConditionalListRes.


        :param updated_at: The updated_at of this V2ConditionalListRes.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(V2ConditionalListRes, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V2ConditionalListRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
