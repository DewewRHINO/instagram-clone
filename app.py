from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

posts=[
    {
        "post-liker":"Aaron Minh",
        "name":"Lance Shinigawa",
        "profile-picture":"assets/villain1.jpg", 
        "pictures":["assets/villain1.jpg", "assets/oopsec.jpg", "assets/1.png"], 
        "description":"I am the funniest mentor, no wonder Minh hired me for Minhtendo. Had a great first day today, my ID card looking dapper. Checkout my blog where I talk about why I am such a villain: https://dewewrhino.github.io/lance-is-a-villain/", 
        "Likes":"2 People 🥺", 
        "post-datetime":"8/2/2023"
    }, 
    {
        "post-liker":"Aaron Minh",
        "name":"Lance Shinigawa",
        "profile-picture":"assets/villain1.jpg", 
        "pictures":["assets/villain1.jpg", "assets/oopsec.jpg", "assets/1.png"], 
        "description":"I am the funniest mentor, no wonder Minh hired me for Minhtendo. Had a great first day today, my ID card looking dapper. Checkout my blog where I talk about why I am such a villain: https://dewewrhino.github.io/lance-is-a-villain/", 
        "Likes":"2 People 🥺", 
        "post-datetime":"8/2/2023"
    },
    {
        "post-liker":"Aaron Minh",
        "name":"Lance Shinigawa",
        "profile-picture":"assets/villain1.jpg", 
        "pictures":["assets/villain1.jpg", "assets/oopsec.jpg", "assets/1.png"], 
        "description":"I am the funniest mentor, no wonder Minh hired me for Minhtendo. Had a great first day today, my ID card looking dapper. Checkout my blog where I talk about why I am such a villain: https://dewewrhino.github.io/lance-is-a-villain/", 
        "Likes":"2 People 🥺", 
        "post-datetime":"8/2/2023"
    }
]

@app.route("/")
def hello_world():
    return render_template('index.html',posts=posts)

@app.route("/iloveminh")
def minhland():
    return render_template('minhworld.html')