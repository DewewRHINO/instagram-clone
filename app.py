from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

posts=[
    {
        "name": "notkyle",
        "post-title": "Kyle Post 1",
        "post-datetime": "Aug 10, 2024",
        "description": "Loved coming up here to take some photos! Always a great sunset to see.",
        "pictures": ["assets/kp1/1.jpg", "assets/kp1/2.jpg", "assets/kp1/3.jpg", "assets/kp1/4.jpg", "assets/kp1/5.jpg", "assets/kp1/6.jpg"],
        "comments": [
            ["J0sh", "wow amazing photos man! We gotta shoot together some time."],
            ["Jetjared", "I've been there recently too! When I went it was kinda cloudy though."],
            ["Lunarlance", "Thumbs up emoji x 2"],
            ["Marmaria", "Where is this?!"],
            ["Travelingtina", "Next time I’m in town, I have to visit!"]
        ]
    },
    {
        "name": "notkyle",
        "post-title": "Kyle Post 2",
        "post-datetime": "Aug 10, 2024",
        "description": "This place at night is even better! My friend and I got to use the telescope and see the rings of Jupiter!!",
        "pictures": ["assets/kp2/1.jpg", "assets/kp2/2.jpg", "assets/kp2/3.jpg", "assets/kp2/4.jpg"],
        "comments": [["Travelingtina", "What kind of telescope was it?!"]]
    },
    {
        "name": "notkyle",
        "post-title": "Kyle Post 3",
        "post-datetime": "Sept 26, 2024",
        "description": "Talk about a throwback thursday! This was wayyyy before I landed my gig at MASA. I was so young then... Underwater Robotics in middle school was so much fun!",
        "pictures": ["assets/kp3/1.jpg", "assets/kp3/2.jpg", "assets/kp3/3.jpg", "assets/kp3/4.jpg"],
        "comments": [
            ["J0sh", "I never would have thought that you competed in Underwater Robotics!"],
            ["Jetjared", "Cool!!!!"],
            ["Marmaria", "Amazing Kyle!"]
        ]
    },
    {
        "name": "notkyle",
        "post-title": "Kyle Post 4",
        "post-datetime": "Oct 1, 2024",
        "description": "What a night!!!! I got to see my favorite composer live!",
        "pictures": ["assets/kp4/1.jpg"],
        "videos": ["assets/kp4/1.mov","assets/kp4/2.mov"],
        "comments": [
            ["Jetjared", "I love his themes, he’s done alot of my favorite movies as well!"],
            ["Lunarlance", "handshake emoji x5"]
        ]
    },
    {
        "name": "notkyle",
        "post-title": "Kyle Post 5",
        "post-datetime": "Nov 7, 2024",
        "description": "Another throwback! I can’t believe that these pictures were taken over 5 years ago at this point!",
        "pictures": ["assets/kp5/1.jpg", "assets/kp5/2.jpg", "assets/kp5/3.jpg", "assets/kp5/4.jpg"],
        "comments": [["Travelingtina", "What’s your dog's name?! How have you never mentioned him in our meetings!"]]
    },
    {
        "name": "Jetjared",
        "post-title": "Jared Post 1",
        "post-datetime": "Nov 8, 2024 10:14pm",
        "description": "Saw another SpaceX launch today!",
        "pictures": [],
        "videos": ["assets/jp1/1.mp4"],
        "comments": [["Lunarlance", "Rocket Emoji x 10"]]
    },
    {
        "name": "marmaria",
        "post-title": "Maria Post 1",
        "post-datetime": "Nov 28, 2024",
        "description": "Looking ahead and traveling throughout the world!",
        "pictures": ["assets/mp1/1.png", "assets/mp1/2.png", "assets/mp1/3.png"],
        "comments": [
            ["Jetjared", "Where did you go?!"],
            ["Lunarlance", "Let the team know about your travels!!"],
            ["Travelingtina", "Putting that spot on my list now!"]
        ]
    },
    {
        "name": "marmaria",
        "post-title": "Maria Post 2",
        "post-datetime": "Aug 23, 2024",
        "description": "I LOVE FOOD AND MATCHA!",
        "pictures": ["assets/mp2/1.jpg"],
        "comments": [["notkyle", "I LOVE MATCHA TOO!"]]
    },
    {
        "name": "marmaria",
        "post-title": "Maria Post 3",
        "post-datetime": "Nov 24, 2024",
        "description": "Shopping for Christmas!",
        "pictures": ["assets/mp3/1.png"],
        "comments": []
    },
    {
        "name": "J0sh",
        "post-title": "Josh Post 1",
        "post-datetime": "Sept 28, 2024",
        "description": "Spent the day going to local museums here in orange! Spent the night looking at the stars and a rocket launch!!",
        "pictures": ["assets/jop1/1.png", "assets/jop1/2.png", "assets/jop1/3.png"],
        "comments": [
            ["Jetjared", "wow which museum is that one?"],
            ["Lunarlance", "fire emoji x5"],
            ["notkyle", "tell the team all about it when you get the chance!"]
        ]
    },
    {
        "name": "lunarlance",
        "post-title": "Lance Post 1",
        "post-datetime": "Aug 28, 2024",
        "description": "I went on a plane with my cousin. Plane emoji",
        "pictures": ["assets/lp1/1.jpg"],
        "comments": [
            ["Jetjared", "What kind of plane did you go on?"],
            ["Travelingtina", "WOW! I’d love to learn how to fly so I can see the rest of the world."]
        ]
    },
    {
        "name": "lunarlance",
        "post-title": "Lance Post 2",
        "post-datetime": "Oct 1, 2024",
        "description": "I went to get some katsu with the boys. Food emoji",
        "pictures": ["assets/lp2/1.jpg"],
        "comments": [["notkyle", "Who is that on the left of the picture?! He looks so cool. Minhsane."]]
    },
    {
        "name": "lunarlance",
        "post-title": "Lance Post 3",
        "post-datetime": "Nov 12, 2024",
        "description": "I am the funniest mentor. Crying emoji",
        "pictures": ["assets/lp3/1.jpg"],
        "comments": [
            ["J0sh", "You are. Are you."],
            ["marmaria", "Yes Lance, you are the funniest mentor."]
        ]
    }
]

@app.route("/")
def hello_world():
    print(posts)
    return render_template('index.html',posts=posts)

if __name__ == "__main__":
    app.run(debug=True)

