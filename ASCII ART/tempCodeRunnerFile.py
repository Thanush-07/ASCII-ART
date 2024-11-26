from flask import Flask, render_template, request, jsonify
import pyfiglet

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the ASCII Art generation request
@app.route('/generate', methods=['POST'])
def generate_ascii_art():
    data = request.get_json()

    # Extract the text, font, and color from the request
    text = data.get('text')
    font = data.get('font', 'standard')
    color = data.get('color', 'white')

    # Generate ASCII art using the pyfiglet library
    try:
        ascii_art = pyfiglet.figlet_format(text, font=font)
        return jsonify({"ascii_art": ascii_art, "color": color})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
