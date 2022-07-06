from flask import Flask
app=Flask(__name__)
@app.route("/hello",methods=["Post","GET"])
def index():
    return "hello world"

if __name__=="__main__":
    app.run()