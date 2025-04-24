# Flask User Management Application

A simple Flask web application for managing user data with a form interface and REST API endpoint.

## Features

- Web form to add new users
- REST API endpoint to view all users
- Data persistence using JSON file
- Error handling for form submissions

## Project Structure

```
.
├── app.py              # Main Flask application
├── data.json           # JSON file storing user data
├── templates/          # HTML templates
│   ├── form.html      # User input form
│   └── success.html   # Success message template
└── README.md          # This file
```

## Setup

1. Make sure you have Python installed
2. Install the required packages:
   ```bash
   pip install flask
   ```

## Running the Application

1. Start the Flask server:
   ```bash
   python app.py
   ```
2. The application will be available at `http://127.0.0.1:5000`

## Usage

### Web Interface
- Visit `http://127.0.0.1:5000/` to access the form
- Fill in the name and role fields
- Submit the form to add a new user

### API Endpoint
- Access `http://127.0.0.1:5000/api` to view all users in JSON format
- The API returns data in the following format:
  ```json
  [
    {"name": "Pushpendu", "role": "Developer"},
    {"name": "John", "role": "Tester"}
  ]
  ```

## Error Handling

- The application includes basic error handling for form submissions
- Error messages will be displayed on the form page if something goes wrong

## Development

The application runs in debug mode, which provides:
- Automatic reloading when code changes
- Detailed error messages
- Debugger PIN for development purposes 