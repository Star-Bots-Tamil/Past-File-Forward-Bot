#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) TRTECHGUIDE

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "11973721"))
    API_HASH = os.environ.get("API_HASH", "5264bf4663e9159565603522f58d3c18")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6084923439:AAEZxSVGRP0muae7vE1xq1PBXWFCYa6Yhq8") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "<b>{file_name}</b>")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", None)
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document")
    OWNER_ID = os.environ.get("OWNER_ID", "1391556668")
    LIMIT = int(os.environ.get("LIMIT", "1000000000000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "BQC2tFkAh5dhyS7ng1gcrSCxJzz22culDpXboh8k8uGmVXnFYDJqDir_N0JMCOPvTL-7N2fxTAhkci8jxoQKtw0YZD70RTt8JWCb6entBonI1GvM8oshhiIat_Y1CeYpiSUzwbgbyg-Jd3j8s10bXwo-tO7-3Z5lS_W281abHsHAMQEXAro_T51WYn2C0BJPWdk3r2_dX0o4fqRSCYJyu6BDqwG6a_qz51QVjLWUW-euQ4oo4OQnOa6KXs-FWo9rIsutT_kYj5zpzMTqLwMKdDHQWBgnpwJYvshBhJBuWZ9quo69ENiMEQ-tWQkL4J3ad_hQjF_UenF_Ui8DXY2GRQEhactoSwAAAAE4UbnNAA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001849017994"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
