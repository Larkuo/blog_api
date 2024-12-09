from app import create_app
import os

# Create the app using the factory function
app = create_app()



if __name__ == '__main__':
    # Run the app in development mode
    app.run(
        host='0.0.0.0',      # Listen on all available interfaces
        port=int(os.getenv('FLASK_PORT', 5000)),  # Default to port 5000 if not specified
        debug=True           # Enable debug mode for development
    )
