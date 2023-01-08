# password generator API

from flask import Flask, request, jsonify
import random
import string
import io
app = Flask('password generator')

@app.route('/random_password')
def generate_password():
    # Get the length and character types of the password from the query string
    length = request.args.get('length')
    character_types = request.args.get('character_types')
    if not length:
        return jsonify({'error': 'Length parameter is required'})
    # Convert the length to an integer
    length = int(length)
    # Build the character set to use for generating the password
    characters = string.ascii_lowercase
    if character_types == 'uppercase':
        characters += string.ascii_uppercase
    elif character_types == 'digits':
        characters += string.digits
    elif character_types == 'punctuation':
        characters += string.punctuation
    elif character_types == 'all':
        characters += string.ascii_uppercase + string.digits + string.punctuation
    # Generate the password
    password = ''.join(random.choices(characters, k=length))
    # Return the password as the API response
    return password

if __name__ == '__main__':
    app.run()
