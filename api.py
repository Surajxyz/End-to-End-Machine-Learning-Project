from flask import Flask
from housing.logger import logging 
app=Flask(__name__)
@app.route("/hello",methods=["Post","GET"])
def index():
    logging.info("app is running")
    return "hello world"

if __name__=="__main__":
    app.run()