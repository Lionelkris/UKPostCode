import re
import requests

# reference https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom


class UKPostCode(object):

    def validate(self, post_code):
        # the below validation will check the format. The valid format is "SW1W 0NY", if you provide a UK post code
        # with no space in between outward and inward code, it will accept that format as well
        validate_pattern = re.match('^[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}$', post_code)
        if validate_pattern:
            return self.validate_code(post_code)
        else:
            return "Invalid format of Post Code"

    def validate_code(self, post_code):
        code_validation = re.match('^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$', post_code)
        if code_validation:
            try:
                termination_check = self.check_terminated(post_code)
                if termination_check:
                    return "Valid UK Post Code"
                else:
                    return "InValid UK Post Code"

            except requests.exceptions.ConnectionError:
                return "Valid UK Post Code. However, no Internet Connection to check termination status"

    @staticmethod
    def check_terminated(post_code):
        trimmed_code = post_code.replace(' ', '')
        response = requests.get('https://api.postcodes.io/postcodes/{}'.format(trimmed_code))
        return response.ok

