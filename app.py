import os
import json
import openai
from flask import Flask, redirect, render_template, request, url_for
from dotenv import load_dotenv # Add
load_dotenv()
app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


conversation = [
    {"role": "system", "content": "You are a customer serivce."}
]
@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        conversation.append(
            {
            'role': 'user',
            'content': request.form["prompt"]
            }
        )
        response = openai.ChatCompletion.create(
            # model="text-davinci-003",
            model="gpt-3.5-turbo",
            # prompt=generate_prompt(animal),
            messages=conversation
            
            # prompt=request.form["prompt"],
            # temperature=0.6,
            # temperature=0,
        )
        conversation.append(
            {
                'role': response.choices[0].message.role,
                'content': response.choices[0].message.content
            }
        )
        # return redirect(url_for("index", result=response.choices[0].text))
        # return redirect(url_for("index", result=json.dumps(conversation)))

    # result = request.args.get("result")
    # return render_template("index.html", result=result)
    return render_template("index.html", result=json.dumps(conversation))


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )
