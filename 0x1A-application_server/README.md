# AirBnB Clone - Application Server Configuration

## Project Overview

This project sets up a development and production environment for the AirBnB clone application. The application is served using Gunicorn and Nginx.

## Requirements

- Nginx
- Gunicorn
- Flask

## Setup Instructions

1. **Install Required Packages:**

   - Ensure `gunicorn` and `flask` are installed.
   - Install Nginx on your server.

2. **Nginx Configuration:**

   - Place the Nginx configuration file (`2-app_server-nginx_config`) in the appropriate directory.
   - Reload or restart Nginx to apply the changes.

3. **Run the Application:**

   - Start the Flask application with Gunicorn on port 5000.

4. **Verify the Setup:**
   - Access the application at `http://54.146.58.195/airbnb-onepage/` to ensure it's working correctly.

## Files

- `2-app_server-nginx_config`: Nginx configuration file for the AirBnB clone application.
- `README.md`: This file.
