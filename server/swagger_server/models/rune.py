# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Rune(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, rune_type: str=None, level: str='RED2'):  # noqa: E501
        """Rune - a model defined in Swagger

        :param rune_type: The rune_type of this Rune.  # noqa: E501
        :type rune_type: str
        :param level: The level of this Rune.  # noqa: E501
        :type level: str
        """
        self.swagger_types = {
            'rune_type': str,
            'level': str
        }

        self.attribute_map = {
            'rune_type': 'runeType',
            'level': 'level'
        }

        self._rune_type = rune_type
        self._level = level

    @classmethod
    def from_dict(cls, dikt) -> 'Rune':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Rune of this Rune.  # noqa: E501
        :rtype: Rune
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rune_type(self) -> str:
        """Gets the rune_type of this Rune.


        :return: The rune_type of this Rune.
        :rtype: str
        """
        return self._rune_type

    @rune_type.setter
    def rune_type(self, rune_type: str):
        """Sets the rune_type of this Rune.


        :param rune_type: The rune_type of this Rune.
        :type rune_type: str
        """
        allowed_values = ["ACCURACY", "CRITRATE", "ATTACK", "EVASION", "ARMORBREAK", "SKILLDAMAGE", "CRITDAMAGE", "HP"]  # noqa: E501
        if rune_type not in allowed_values:
            raise ValueError(
                "Invalid value for `rune_type` ({0}), must be one of {1}"
                .format(rune_type, allowed_values)
            )

        self._rune_type = rune_type

    @property
    def level(self) -> str:
        """Gets the level of this Rune.


        :return: The level of this Rune.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level: str):
        """Sets the level of this Rune.


        :param level: The level of this Rune.
        :type level: str
        """
        allowed_values = ["BLUE1", "BLUE2", "GREEN1", "GREEN2", "YELLOW1", "YELLOW2", "YELLOW3", "PURPLE1", "PURPLE2", "PURPLE3", "ORANGE1", "ORANGE2", "ORANGE3", "ORANGE4", "RED1", "RED2"]  # noqa: E501
        if level not in allowed_values:
            raise ValueError(
                "Invalid value for `level` ({0}), must be one of {1}"
                .format(level, allowed_values)
            )

        self._level = level