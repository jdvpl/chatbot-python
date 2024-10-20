from flask import Flask, render_template, request, jsonify
from chat import get_response
app=Flask(__name__)



@app.post('/predict')
def predict():
    text = request.get_json().get("message")
    print(f"User question: {text}")
    resp = get_response(text)
    return jsonify({'answer': resp})

if __name__ == "__main__":
    app.run(debug=True)