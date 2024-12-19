from flask import Flask, request

app = Flask(__name__)

@app.route('/count', methods=['GET'])
def count_text():
    text = request.args.get('text')
    if not text:
        return "Error: Missing 'text' parameter", 400
    
    words = len(text.split())
    
    return f"Word Count: {words}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
