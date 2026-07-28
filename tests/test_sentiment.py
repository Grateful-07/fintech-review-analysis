import pandas as pd
from src.sentiment_thematic import assign_theme

def test_theme_keyword_mapping():
    login_sample = "I cannot get my OTP code to login to my account"
    transfer_sample = "The money transfer was slow and failed midway"
    ui_sample = "Clean design and smooth user interface"
    
    assert assign_theme(login_sample) == "Account Access & Authentication"
    assert assign_theme(transfer_sample) == "Transaction & System Performance"
    assert assign_theme(ui_sample) == "UI & User Experience"
