import os
from flask import Flask , render_template ,request , jsonify
import google.generativeai as genai
from dotenv import load_dotenv

#Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

#Configure the Gemini API
genai.configure(api_key=GOOGLE_API_KEY)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
   user_message = request.json.get('message')
   model = genai.GenerativeModel('gemini-pro')
   chat = model.start_chat(history=[])
   response = chat.send_message(user_message)
   return jsonify({"response": response.text})




if __name__ == '__main__':
    app.run(debug=True)