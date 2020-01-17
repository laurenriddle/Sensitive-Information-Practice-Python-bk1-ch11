'''
Create a class to represent a patient of a doctor's office. The Patient class will accept the following information during initialization

1. Social security number
2. Date of birth
3. Health insurance account number
4. First name
5. Last name
6. Address

The first three properties should be read-only. First name and last name should not be exposed as properties at all, but instead expose a calculated property of full_name. Address should have a getter and setter.

'''

class Patient:
    def __init__(self, SSN, DOB, HI, FN, LN,AD):
        self.__social_security_number = SSN
        self.__date_of_birth = DOB
        self.__health_insurance = HI
        self.__first_name = FN
        self.__last_name = LN
        self.__address = AD

# GETTERS
    @property # The address getter
    def address(self):
        try:
            return self.__address # Note there are 2 underscores here
        except AttributeError:
            return ""
    @property # The address getter
    def social_security_number(self):
        try:
            return self.__social_security_number # Note there are 2 underscores here
        except AttributeError:
            return ""
    @property # The address getter
    def date_of_birth(self):
        try:
            return self.__date_of_birth # Note there are 2 underscores here
        except AttributeError:
            return ""
    @property # The address getter
    def health_insurance(self):
        try:
            return self.__health_insurance # Note there are 2 underscores here
        except AttributeError:
            return ""
    @property # The address getter
    def first_name(self):
        try:
            return self.__first_name # Note there are 2 underscores here
        except AttributeError:
            return ""
    @property # The address getter
    def last_name(self):
        try:
            return self.__last_name # Note there are 2 underscores here
        except AttributeError:
            return ""
    @property # The address getter
    def full_name(self):
        try:
            return f"{self.first_name} {self.last_name}" # Note there are 2 underscores here
        except AttributeError:
            return ""


# SETTERS
    @address.setter # The address Setter
    def address(self, new_address):
        if type(new_address) is str:
            self.__address = new_address
        else:
            raise TypeError('Please provide a floating point value for the price')
    # @Social_security_number.setter # The Social_security_number Setter
    # def Social_security_number(self, new_Social_security_number):
    #         self.__Social_security_number = self.__Social_security_number

    #         return "This is a read only attribute"
    # @Date_of_birth.setter # The Date_of_birth Setter
    # def Date_of_birth(self, new_Date_of_birth):
    #         return "This is a read only attribute"
    # @Health_insurance.setter # The Health_insurance Setter
    # def Health_insurance(self, new_Health_insurance):
    #         return "This is a read only attribute"
    # @first_name.setter # The first_name Setter
    # def first_name(self, new_first_name):
    #         return "This is a read only attribute"
    # @last_name.setter # The last_name Setter
    # def last_name(self, new_last_name):
    #         return "This is a read only attribute"


cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)

# This should not change the state of the object
# cashew.social_security_number = "838-31-2256"

# Neither should this
# cashew.date_of_birth = "01-30-90"

# But printing either of them should work
print(cashew.social_security_number)   # "097-23-1003"

# These two statements should output nothing
print(cashew.first_name)
print(cashew.last_name)

# But this should output the full name
print(cashew.full_name)   # "Daniela Agnoletti"
