from os import path, getenv
import os, time 

class Config:
    API_ID = int(getenv("API_ID", "21406615"))
    API_HASH = getenv("API_HASH", "d66b1900ea3a7438ee22dd389085949a")
    BOT_TOKEN = getenv("BOT_TOKEN", "7895883671:AAFSp7wa7-fMdoXzP38Hz8O724Pr3g191CE")
 
    ADMIN = list(map(int, getenv("ADMIN", "7974532619").split()))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "0"))
    FORCE_SUB = int(getenv("FORCE_SUB", "0"))

    # database configs
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://tharkihoobooji:tharkihoobooji@cluster0.sje0k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DB_NAME = os.environ.get("DB_NAME", "tharkihoobooji")
    
    #web response 
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    BOT_UPTIME  = time.time()
    PORT = os.environ.get("PORT", "8080")

rkn1 = Config()
