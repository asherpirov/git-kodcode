from logging_setup import get_logger

# יצירת לוגר שמקבל את שם המודול הנוכחי
logger = get_logger("apps.log")

def login_user(username):
    logger.info(f"User '{username}' is trying to log in.")
    # כאן היה קוד התחברות...
    logger.warning(f"Login successful for '{username}'.")
