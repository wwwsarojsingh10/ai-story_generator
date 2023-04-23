import openai
import os
import json
from flask import Flask, jsonify, request, render_template
from dotenv import load_dotenv # Add


print("bchgfhxfgb")

app = Flask(__name__)


# set the env file connection


# set up OpenAI API credentials
openai.api_key = 'OPENAI_API_KEY'
model_engine = 'text-davinci-003'

@app.route('/')
def index():
	return app.send_static_file('index.html')

@app.route('/generate', methods=['POST'])
def generate_story():
	data = request.get_json()
	prompt = data['prompt']


def generate_story():
    # Get prompt from the form data
    prompt = request.form['prompt']

    # Initialize GPT-3 API client
    gpt3_client = openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Get the generated story from the API response
    generated_story = response.choices[0].text

    return render_template('index.html', prompt=prompt, story=generated_story)

if __name__ == '__main__':
    app.run(debug=True)