import os
import time
import unittest
from quantity.unit import Unit
import quantity.api


class TestQuantity(unittest.TestCase):

    library_path = None

    @classmethod
    def setUpClass(cls):
        cls.detect_library_path()

    def tearDown(self):
        time.sleep(0.5)

    @classmethod
    def tearDownClass(cls):
        pass

    @classmethod
    def detect_library_path(cls):
        if os.path.exists("../lib/libquantity-x86_64-linux-gnu.so"):
            cls.library_path = "../lib/libquantity-x86_64-linux-gnu.so"
        if os.path.exists("./lib/libquantity-x86_64-linux-gnu.so"):
            cls.library_path = "./lib/libquantity-x86_64-linux-gnu.so"

    def test_quantity(self):
        # Since the resource can only be initiated once, all the test-cases are embedded into one test-method.

        u1 = Unit()
        u1.mul("m / s").build()

        u2 = Unit()
        u2.mul(" kg / s s m ").build()

        u3 = Unit()
        u3.mul(" kg / m s s ").build()

        u4 = Unit()
        u4.mul(" m kg m / s  ").build()

        u5 = Unit()
        u5.mul(" m m kg / s  ").build()

        u6 = Unit()
        u6.mul(" cd /  ").build()

        with quantity.api.Resource(TestQuantity.library_path) as res:

            # Test buildUnit()
            unit_str = res.build_unit(str(u1))
            self.assertEqual(unit_str.decode(), " s^-1 m")

            # Test isUnitEqual(). Expect equal
            rv = res.is_unit_equal(str(u2), str(u3))
            self.assertEqual(rv, 1)

            # Test isUnitEqual(). Expect equal
            rv = res.is_unit_equal(str(u4), str(u5))
            self.assertEqual(rv, 1)

            # Test isUnitEqual(). Expect not equal
            rv = res.is_unit_equal(str(u2), str(u5))
            self.assertEqual(rv, 0)

            # Test getQuantityForUnit()
            rv = res.get_quantity_for_unit(str(u1))
            self.assertEqual(rv.decode(), "velocity")

            # Test getQuantityForUnit()
            rv = res.get_quantity_for_unit(str(u2))
            self.assertEqual(rv.decode(), "pressure")

            # Test getQuantityForUnit()
            rv = res.get_quantity_for_unit(str(u4))
            self.assertEqual(rv.decode(), "power")

            # Test getQuantityForUnit()
            rv = res.get_quantity_for_unit(str(u6))
            self.assertEqual(rv.decode(), "luminous_intensity")


if __name__ == '__main__':
    unittest.main()