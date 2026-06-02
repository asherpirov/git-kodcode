import logging

""" q5 """
logging.basicConfig(level=logging.INFO, format='%(levelname)s | %(message)s')
logger = logging.getLogger(__name__)
logger.info('Application started')

""" q6 """
def process_payment(user_id, amount):
    logger.info("Starting payment for user %s", user_id)
    if amount <= 0:
        logger.error('ERROR: Invalid amount')
        return
    if amount > 10000:
        logger.warning('WARNING: Large transaction')
    logger.info("Payment of %s completed for user %s", amount,user_id)

""" q7 """
logger = logging.getLogger("payments")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("app.log", encoding="utf-8")

formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def payment(amount):
    logger.info("Starting payment process for %s shekels", amount)
    if amount <= 0:
        logger.error('ERROR: Invalid amount')
        return
    if amount > 1000:
        logger.warning("Notice: This is a particularly large transaction!")

    logger.info("Payment process completed successfully.")

payment(150)
payment(-50)

""" q8 """

def read_config(filepath):
    logger.debug("open file function")
    try:
        with open(filepath) as f:
            data = f.read()
            logger.info("successful file open")
            return data
    except FileNotFoundError:
        logger.exception("file not found")
        return None

read_config("app.log")

"""q10"""

logger.info('done')
#The message does not provide enough information.

logger.error("failed")
#It is not clear enough what the error was about.

# logger.info('user=%s', user_id)
#There is information here about
# both the user and their ID.
# You can also add a message about the action.


"""q11"""
"""סווג כל אירוע מהמערכת לרמת הלוג הנכונה:

• אדמין נכנס למערכת הניהול
info

• שירות חיצוני לא מגיב
error

• פונקציית חישוב מס החלה לרוץ
debug

• תעודת SSL עומדת לפוג בעוד 7 ימים
warning

• הזמנה בוטלה על ידי לקוח
info

• תשלום נכשל 3 פעמים ברצף
error

"""

"""q12"""
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("users")
logger.addHandler(file_handler)

def register_user(email, password, age):
    logger.info("User registration started",
                extra={"user_email": email, "user_age": age})

    if age < 18:
        logger.warning("Registration rejected: Age %s is under the legal limit.", age)
        return
    logger.info('ok email=%s password=%s', email, bool(password))
    logger.info('Login completed.')

register_user("asherpirov@gmail.com", 1234, 24)


