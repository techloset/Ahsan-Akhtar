from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
#mongodb+srv://ahsan:1095@eventapp.6ancirw.mongodb.net/

if __name__=="__main__":
    app.run()