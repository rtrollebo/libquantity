class Unit(object):

    def __init__(self):
        self.str_value = ""
        self.nominator = ""
        self.denominator = ""

    def __repr__(self) -> str:
        return self.str_value

    def mul(self, unit: str):
        """
        Multiplies this unit with a new unit
        :param unit: unit with which to multiply
        :return: this Unit
        """
        unit_array = unit.split("/")
        self.nominator = self.nominator + " " + unit_array[0]
        if len(unit_array) > 1:
            self.denominator = self.denominator + " " + unit_array[1]
        return self

    def build(self):
        """
        Builds the Unit
        :return: this Unit
        """
        if self.nominator:
            self.str_value = " " + self.nominator
        if self.denominator:
            self.str_value = self.str_value + " , " + self.denominator
