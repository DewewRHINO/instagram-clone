from flask import Flask
from flask import render_template

app = Flask(__name__)

posts=[
    {
        "post-liker":"Lancey Shinigawa",
        "name":"Kyle Rodriguez",
        "profile-picture":"assets/kyle1.png", 
        "pictures":["assets/kyle1.png","assets/kyle2.png","assets/kyle3.png"], 
        "description":"I love taking pictures, taking pictures is so fun.", 
        "Likes":"20 Million", 
        "post-datetime":"2/2/2024"
    }, 
    {
        "post-liker":"Lancey Shinigawa",
        "name":"Kyle Rodriguez",
        "profile-picture":"assets/kyle1.png", 
        "pictures":["assets/kyle1.png","assets/kyle2.png","assets/kyle3.png"], 
        "description":"Checkout my new photography website! I'll be taking orders 😉.", 
        "Likes":"40 Million", 
        "post-datetime":"8/2/2023"
    } 
]

@app.route("/")
def hello_world():
    return render_template('index.html',posts=posts)