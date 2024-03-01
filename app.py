from flask import Flask
from flask import render_template

app = Flask(__name__)

posts=[
    {
        "post-liker":"Aaron Minh",
        "name":"Lance Shinigawa",
        "profile-picture":"assets/villain1.jpg", 
        "pictures":["assets/villain1.jpg"], 
        "description":"I am the funniest mentor", 
        "Likes":"2 People 🥺", 
        "post-datetime":"8/2/2023"
    }, 
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
        "post-liker":"Minh Duy Tran",
        "name":"Lance Shinigawa",
        "profile-picture":"assets/villain1.jpg", 
        "pictures":["assets/villain6.jpg"], 
        "description":"I wasn't always a villain", 
        "Likes":"20k", 
        "post-datetime":"8/2/2023"
    },
    {
        "post-liker":"Lancey Shinigawa",
        "name":"Kyle Rodriguez",
        "profile-picture":"assets/kyle1.png", 
        "pictures":["assets/kyphoto1.jpg","assets/kyphoto2.jpg"], 
        "description":"Checkout my new photography website! I'll be taking orders 😉.", 
        "Likes":"40 Million", 
        "post-datetime":"8/2/2023"
    }, 
    {
        "post-liker":"Ashley Minh",
        "name":"Lance Shinigawa",
        "profile-picture":"assets/villain1.jpg", 
        "pictures":["assets/villain3.jpg"], 
        "description":"I'm so funny", 
        "Likes":"No one", 
        "post-datetime":"1 Day ago"
    }, 
    {
        "post-liker":"Ashley Minh",
        "name":"Lance Shinigawa",
        "profile-picture":"assets/villain9.jpg", 
        "pictures":["assets/villain9.jpg"], 
        "description":"Met my idol today!", 
        "Likes":"No one", 
        "post-datetime":"5/27/2022"
    }

]

@app.route("/")
def hello_world():
    return render_template('index.html',posts=posts)