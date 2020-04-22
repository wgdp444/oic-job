from flask import Flask,render_template

app = Flask(__name__)

@app.route("/test/test/yadon")
def test():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)