# Interactive app
[README em português](./README-portuguese.md)
## Description
This repository contains the solution to a past Uber backend challenge.

Imagine that you are developing a monitoring application for a smart vegetable garden, equipped with humidity, temperature and light sensors. Your task is to design an interactive menu for this application. How would you structure and implement a menu that allows the user to view the current sensor readings, adjust alert settings for each sensor (for example, set a minimum humidity threshold). Describe the logic of the menu, the options available to the user and how you would handle user input to navigate between the different functionalities of the application

In my solution, I implemented Python with Streamlit to develop a web page that users can interact and setup settings of min and max values for the sensors.

You can check the challenge's result at: [Render Deployed](https://arduino-final-test.onrender.com/)

## Technologies Used
1. Python
2. Render
3. Streamlit

> [!NOTE]
> Since Render is FREE maybe in the next months the page isn't available anymore, try access this and wait some minutes to the Render start the web service.

## How to Replicate and Run the Application
1. Clone the repository
2. Create a Python virtual environment with `py -m venv venv`
3. Activate the virtual environment (this step may vary depending on your operating system):
```.\venv\Scripts\activate```
4. Install the project dependencies with `pip install -r requirements.txt`
5. Have the keys of a user with permissions to use Amazon SES
6. Run the application server using the command `streamlit run main.py`
7. Access the link provided by streamlit
