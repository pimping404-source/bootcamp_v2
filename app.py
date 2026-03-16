from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Bootcamp V2: Day 1 Deployment Successful!</h1><p>It's just us and the code now.</p>"

if __name__ == "__main__":
    app.run(debug=True)