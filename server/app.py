from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Accessibility Audit Server"

if __name__ == "__main__":
    app.run(debug=True)
