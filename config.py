import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "11973721"))
    API_HASH = os.environ.get("API_HASH", "5264bf4663e9159565603522f58d3c18")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6084923439:AAEZxSVGRP0muae7vE1xq1PBXWFCYa6Yhq8") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "past-file-forward-bot")
    USER_SESSION = os.environ.get("USER_SESSION", "past-file-forward-user")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document video").split()
    OWNER_ID = os.environ.get("OWNER_ID", "1391556668")
    LIMIT = int(os.environ.get("LIMIT", "1000000000000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "+919095030397")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001849017994"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
