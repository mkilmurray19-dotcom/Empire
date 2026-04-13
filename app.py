"""
Empire - Australian Investment Property Analyzer
Main Flask Application

This is the entry point for the web application.
"""

from flask import Flask, render_template, request, jsonify
from config import Config
import os

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Import routes
from routes import search_routes, property_routes

# Register blueprints
app.register_blueprint(search_routes.bp)
app.register_blueprint(property_routes.bp)

@app.route('/')
def home():
    """Home page route"""
    return render_template('index.html')

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)