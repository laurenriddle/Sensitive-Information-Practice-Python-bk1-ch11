'''
Create a class to represent a patient of a doctor's office. The Patient class will accept the following information during initialization

Social security number
Date of birth
Health insurance account number
First name
Last name
Address

The first three properties should be read-only. First name and last name should not be exposed as properties at all, but instead expose a calculated property of full_name. Address should have a getter and setter.
'''

class Patient:
    def __init__(self, SSN, DOB, HI, FN, LN,AD):
        self.Social_security_number = SSN
        self.Date_of_birth = DOB
        self.Health_insurance = HI
        self.first_name = FN
        self.last_name = LN
        self.address = AD

    # @property # The first name getter
    # def Social_security_number(self):
    #     try:
    #         return self.__Social_security_number# Note there are 2 underscores here
    #     except AttributeError:
    #         return ""


cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)

# This should not change the state of the object
cashew.social_security_number = "838-31-2256"

# Neither should this
cashew.date_of_birth = "01-30-90"

# But printing either of them should work
print(cashew.social_security_number)   # "097-23-1003"

# These two statements should output nothing
print(cashew.first_name)
print(cashew.last_name)

# But this should output the full name
# print(cashew.full_name)   # "Daniela Agnoletti"
