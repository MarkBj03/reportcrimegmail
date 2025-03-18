# Flask Crime Reporting Application

This project is a Flask web application that allows users to submit crime reports, including optional file attachments. The application sends the submitted data via email and provides a thank you page upon successful submission.

## Project Structure

```
server
├── api
│   └── server.py        # Contains the Flask application and routes
├── requirements.txt      # Lists the project dependencies
├── vercel.json           # Configuration for deploying on Vercel
└── README.md             # Documentation for the project
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd server
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application Locally**
   ```bash
   python api/server.py
   ```
   The application will be available at `http://127.0.0.1:5000`.

## Deployment on Vercel

1. **Create a `vercel.json` Configuration File**
   Ensure that the `vercel.json` file is correctly set up to define the framework and build settings for your Flask application.

2. **Deploy to Vercel**
   - Install the Vercel CLI if you haven't already:
     ```bash
     npm i -g vercel
     ```
   - Run the following command in your project directory:
     ```bash
     vercel
     ```
   - Follow the prompts to complete the deployment.

## Usage

- Navigate to the application in your web browser.
- Fill out the crime report form and optionally upload a file.
- Submit the form to send the report via email and view the thank you page.

## License

This project is licensed under the MIT License.