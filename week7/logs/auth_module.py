from logging_setup import get_logger
import main # מייבאים את המודול הראשון

# יצירת לוגר עבור המודול הנוכחי (main)
logger = get_logger(__name__)

logger.info("The system is starting up...")

# הפעלת הפונקציה מהמודול השני
main.login_user("david_cohen")

logger.info("The system finished running successfully.")