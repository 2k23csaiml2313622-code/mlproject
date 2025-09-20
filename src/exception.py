# this will contain everything related to exception handling
# sys module will give information about exception like which line of code caused exception
# exception module will give information about exception like type of exception and value of exception
import sys
from src.logger import logging

def error_message_detail(error, error_detail:sys):
    """this function will return the error message"""
    _,_,exc_tb=error_detail.exc_info() # it will give tuple of three values type of exception, value of exception and traceback object
    file_name=exc_tb.tb_frame.f_code.co_filename # it will give the file name where exception occurred
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message
# now this function tells which file and which line of code caused exception exc.info() will give tuple of three values type of exception, value of exception and traceback object
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Logging has started")
        raise CustomException(e,sys)
    