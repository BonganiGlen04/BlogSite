from flask import Flask, render_template, url_for
app = Flask(__name__)

post = [
    {
    "title": "First Post",
    "content": "This is the content of the first post.",
    "author": "John Doe"
},
   {
    "title": "Second Post",
    "content": "This is the content of the second post.",
    "author": "John Doe"
}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=post)

@app.route("/about")
def about():
    return render_template("about.html", title = "About")

if __name__ == "__main__":
    app.run(debug=True)