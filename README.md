# Email Service
[README em português](./README-portuguese.md)
## Description
This repository contains the solution to a past Uber backend challenge.

It involves developing an email service that abstracts between email providers and provides a way for the application to handle it if one of the services goes offline.

In my solution, I implemented the AWS Simple Email Service and used the SMTPLIB library to create a local service in the Flask application. I also went beyond and developed separate endpoints for using the providers independently.

You can check the challenge's GitHub page at: [Uber Challenge](https://github.com/uber-archive/coding-challenge-tools/blob/master/coding_challenge.md)

## Technologies Used
1. Flask, with Flask and Flask-Smorest
2. AWS Simple Email Service
3. SMTPLib

The application supports Swagger UI, so you can access **.../swagger-ui** to check the application's documentation.

![Screenshot of the Swagger UI of the application](./swagger-ui.jpg)

> [!NOTE]
> The documentation may not be complete as I have not fully configured Swagger, and I do not have the knowledge to do so.

## How to Replicate and Run the Application
1. Clone the repository
2. Create a Python virtual environment with `py -m venv venv`
3. Activate the virtual environment (this step may vary depending on your operating system):
```.\venv\Scripts\activate```
4. Install the project dependencies with `pip install -r requirements.txt`
5. Have the keys of a user with permissions to use Amazon SES
6. Have credentials to use an email service such as Google, Outlook (to use the SMTPLib-based service)
7. Create a file in the root directory called **.flaskenv**
8. Add the following necessary variables:
```
FLASK_APP=app
FLASK_DEBUG=1
```
7. For Amazon SES usage:
```
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
```
8. For SMTPLib library usage:
```
MAIL_PORT=service_port
MAIL_SERVER=service_server
MAIL_USER=authentication_user
MAIL_PASSWORD=authentication_password
```
9. Run the application server using the command `flask run`
   
## Usage
To use the application for sending an email, you can use the following POST method endpoints:
1. `/api/send_mail/`
To send the email using the available service verification system
2. `/api/send_mail/flask/`
To send the email using the SMTPLib service
3. `/api/send_mail/aws/`
To send the email using the Amazon Simple Email Service

### Body Definition
Requires the body to be a JSON
```
{
"body": "Email message",
"subject": "Email subject",
"to": "Email recipient",
}
```
