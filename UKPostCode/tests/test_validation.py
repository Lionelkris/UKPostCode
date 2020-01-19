from UKPostCode.validate import UKPostCode
import unittest


class TestPostcodeValidation(unittest.TestCase):

    def test_good_postcodes_with_right_format(self):
        test_input = 'SW1W 0NY'
        postcode_obj = UKPostCode()
        result = postcode_obj.validate(test_input)
        self.assertTrue('Valid UK Post Code' in result)

    def test_good_postcodes_with_wrong_format(self):
        test_input = 'st1-0NY'
        postcode_obj = UKPostCode()
        result = postcode_obj.validate(test_input)
        self.assertTrue('Invalid format of Post Code' in result)

    def test_invalid_postcode(self):
        test_input = 'QO16 7GZ'
        postcode_obj = UKPostCode()
        result = postcode_obj.validate(test_input)
        self.assertTrue('InValid UK Post Code' in result)

    def test_terminated_postcode(self):
        test_input = 'AB1 0BB'
        postcode_obj = UKPostCode()
        result = postcode_obj.validate(test_input)
        self.assertTrue('InValid UK Post Code' in result)


if __name__ == '__main__':
    unittest.main()