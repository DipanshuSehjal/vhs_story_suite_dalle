"""
run.py

This script is used to run the Flask application.
"""

from app import create_app

# Create the Flask application instance
app = create_app()

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)  # Set debug=True for development environment
