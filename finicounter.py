from sanic import Sanic, response
import datetime
import logging
import os
import pymongo
import validators

logger = logging.getLogger("finicounter")
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
logger.addHandler(consoleHandler)
logger.setLevel(logging.DEBUG)

MONGODB_URL = os.environ.get("MONGODB_URL")
CORS_ORIGINS = os.environ.get("CORS_ORIGINS")
DB_NAME = os.environ.get("DB_NAME") if os.environ.get("DB_NAME") is not None else "MyCounter"
COLLECTION_NAME = "Counter"
logger.info(f"MongoDB Url: [{MONGODB_URL}] DB_NAME: [{DB_NAME}]")

# MONGODB_URL = ""
# CORS_ORIGINS = ""

cors_headers = {"Access-Control-Allow-Origin": CORS_ORIGINS, "Access-Control-Allow-Method": "POST, GET, OPTIONS"}

mongoClient = pymongo.MongoClient(MONGODB_URL)
db = mongoClient[DB_NAME]
collection= db[COLLECTION_NAME]

app = Sanic("finicounter")
app.static("/", "./docs/index.html")
app.static("/en", "./docs/en.html")
app.static("/logo.png", "./docs/logo.png")
app.static("/finicounter.js", "./docs/finicounter.js")
app.static("main.css", "./docs/main.css")

@app.route("/counter")
async def counter(request):
    args = request.get_args()
    host = args["host"][0]
    if not validators.domain(host) and not validators.ipv4(host):
        return response.json({"message": "Invalid hostname"}, status = 401)
    
    result = collection.find_one_and_update({"host": host}, {"$inc": {"views": 1}, "$set": { "updateTime": datetime.datetime.utcnow()}}, upsert = True, return_document = pymongo.collection.ReturnDocument.AFTER, maxTimeMS=50)
    logger.info(f"[{result['updateTime']}] | [{result['host']}]: {result['views']}")
    return response.json({"views": result['views']}, headers = cors_headers)


#app.run(host="0.0.0.0", port=8000, fast=True)
