from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

openai.api_key = 'sk-proj-PY6vtg94r8h13KLrGdEsT3BlbkFJJzWIY1441HU7iCl3KICx' 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-trends', methods=['POST'])
def get_trends():
    prompt = "List the top 3 fashion trends."
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        
        trends = response['choices'][0]['message']['content'].strip()
        return jsonify({'trends': trends}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
