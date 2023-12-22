class SalaryNotRangeException(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message='Salary is not in (5000, 15000) range, your salary: {}'):
        self.message = message.format(salary)
        super().__init__(self.message)
