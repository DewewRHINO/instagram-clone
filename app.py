from flask import Flask
from flask import render_template

app = Flask(__name__)

posts=[{"post-liker":"Lanceyboi","name":"Maria","profile-picture":"assets/maria1.jpg", "pictures":["assets/maria1.jpg","assets/maria2.jpg","assets/maria3.jpg"], "description":"Lance Likes Guys", "Likes":"80", "post-datetime":"2/2/2024"}]

@app.route("/")
def hello_world():
    return render_template('index.html',posts=posts)