from ctypes import cdll, c_char_p, c_int
from quantity import LIBRARY_PATH_DEFAULT


class Resource(object):
    """
    This is a wrapper class around the libquantity library, containing API
    definitions to construct and compare physical Units and convert from Unit to Quantity.
    """
    def __init__(self, library_path=None):
        if library_path is None:
            self.resource = cdll.LoadLibrary(LIBRARY_PATH_DEFAULT)
        else:
            self.resource = cdll.LoadLibrary(library_path)

    def __enter__(self):
        self.resource.quantity_init()
        return self

    def __exit__(self, type, value, tb):
        self.resource.quantity_exit()

    def build_unit(self, unit):
        """
        A parser to build a formatted-unit based on a un-formatted raw-string unit.
        :param unit: raw-string
        :return: Formatted Unit
        """
        api_build_unit = getattr(self.resource, "buildUnit")
        api_build_unit.restype, api_build_unit.argtypes = (c_char_p, [c_char_p])
        return self.resource.buildUnit(bytes(unit, "utf-8"))

    def is_unit_equal(self, unit1, unit2):
        """
        Checks the units, and determines whether they are equal.
        :param unit1: raw-string Unit
        :param unit2: raw-string Unit
        :return: 1 if unit1 and unit2 are equal. 0 if not.
        """
        api_is_unit_equal = getattr(self.resource, "isUnitEqual")
        api_is_unit_equal.restype, api_is_unit_equal.argtypes = (c_int, [c_char_p, c_char_p])
        return self.resource.isUnitEqual(bytes(unit1, "utf-8"), bytes(unit2, "utf-8"))

    def get_quantity_for_unit(self, unit1):
        """
        Finds the quantity to which the unit corresponds.
        :param unit1: raw-string Unit
        :return: quantity
        """
        api_get_quantity_for_unit = getattr(self.resource, "getQtyForUnit")
        api_get_quantity_for_unit.restype, api_get_quantity_for_unit.argtypes = (c_char_p, [c_char_p])
        return self.resource.getQtyForUnit(bytes(unit1, "utf-8"))
