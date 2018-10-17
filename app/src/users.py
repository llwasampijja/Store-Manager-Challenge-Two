users = [
    {
        "username": "annnight",
        "password": "admin",
        "name": "Ann Night",
        "contact-phone": "0992882838",
        "residence": "Mbajja, Ntanzi",
        "joined": "12th August 2024",
        "kin": "Edward Army",
        "kin-contact": "0058780283",
        "role": "admin"
    },
    {
        "username": "noone",
        "password": "admin",
        "name": "No One",
        "contact-phone": "342465634",
        "residence": "Bravos, Westeros",
        "joined": "18th october 2024",
        "kin": "Jon Snow",
        "kin-contact": "0058780283",
        "role": "secondary admin"
    },
    {
        "username": "dallkased",
        "password": "admin",
        "name": "Dall Kased",
        "contact-phone": "8337927829",
        "residence": "Bolongatiya",
        "joined": "31th October 2213",
        "kin": "Lwasa Lamech",
        "kin-contact": "0058780283",
        "role": "store attendant"
    }
]

from flask import Flask, jsonify, request, Response, json
app = Flask(__name__)

# GET store attendants
@app.route('/users')
def get_users():
    return jsonify({'users': users})

app.run(debug=True, port=5000)