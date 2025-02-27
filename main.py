
class UserInputValidator:
    """Takes list as input and returns list of positive integers"""
    def __init__(self, validator):
        self.valid = validator

    def validate_positive_integers(self):
        txt = "The list has been checked for positive integers, the following has been validated: \n"
        print(txt, self._valid)


    @property
    def valid(self):
        """returns an encapsulated list of positive integers"""
        return self._valid

    @valid.setter
    def valid(self, validator):
        self._valid = []
        for variable in validator:
            variable = int(variable)
            if variable > 0:
                self._valid.append(variable)
        self._valid.sort()
