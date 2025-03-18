from flask import Flask, render_template
from fetch_data import fetch_posts
from generate_content import generate_content

app = Flask(__name__)

@app.route("/")
def home():
    accounts = ["elonmusk", "wsj"]  # Your list of accounts
    posts = fetch_posts(accounts, days=7)
    content = generate_content(posts)
    return render_template("index.html", content=content)

if __name__ == "__main__":
    app.run(debug=True)