from flask import Flask,redirect,request



app = Flask(__name__)

@app.route("/")
def index():
    print(request.remote_addr)
    return redirect("https://www.google.com")


if __name__=="__main__":
    app.run(debug=True,port=3000)