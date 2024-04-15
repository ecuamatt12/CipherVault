from flask import Flask

# Create Flask application instance
app = Flask(__name__)

# Define a route
@app.route('/')
def index():
    return 'Hello, CipherVault! This is your Flask backend.'

# Run the Flask application if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)
