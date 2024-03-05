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
        "description":"I love taking pictures, taking pictures is so fun. All started back in my Cypress High School Days. What a time.", 
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
        "description":"Checkout my new photography website! I'll be taking orders 😉. Just started this company today! You can visit it at https://dewewrhino.github.io/kyphoto/", 
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
    },
    {
        "post-liker":"Lance Minh",
        "name":"The Legend",
        "profile-picture":"assets/MINHDUYTRAN.png", 
        "pictures":["assets/MINHDUYTRAN.png"], 
        "description":"I am Minh, I am very epic. (ignore the rest of this, it's for lance): MDAgMSAxIDAgMDAgMSAxMCAwIDExIDAxIDAxIDAwMCAxMTAgMCAwIDAwMCAwMTEgMTEgMTExIDAxMDEgMTEwIDExMSAxMTEgMDEwMCAwMDAgMTEwIDEwMSAwMTEgMSAwMCAwMDAgMCAxMSAwMDAgMDE=", 
        "Likes":"20 Billion", 
        "post-datetime":"5/13/2022"
    },
    {
        "post-liker":"Lance Minh",
        "name":"Maria",
        "profile-picture":"assets/maria1.jpg", 
        "pictures":["assets/maria1.jpg", "assets/maria2.jpg", "assets/maria3.jpg", "assets/maria4.jpg"], 
        "description":"Had a great time at the aquarium in Long Beach!!! Saw this really epic scorpion.", 
        "Likes":"100 Billion", 
        "post-datetime":"3/1/2024"
    }, 
    {
        "post-liker":"Maria",
        "name":"Josh",
        "profile-picture":"assets/mfa.jpg", 
        "pictures":["assets/mfa.jpg"], 
        "description":"Just got this MFA token today! Very epic.", 
        "Likes":"50 Billion", 
        "post-datetime":"3/1/2024"
    }
    
]

@app.route("/")
def hello_world():
    return render_template('index.html',posts=posts)