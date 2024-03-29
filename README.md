# Exercise Tracker API

## Overview

The Exercise Tracker API is a RESTful API built using Flask, designed to interact with a MySQL database. The primary focus of this API is to provide CRUD (Create, Read, Update, Delete) operations for managing exercises stored in the "exercise" table. This project serves as the backend for an application that aims to empower users to select their favorite exercises and create personalized workout routines.

## Technologies Used

- **[Flask](https://flask.palletsprojects.com/):** The lightweight and flexible web framework for building the API.
- **[MySQL](https://www.mysql.com/):** The relational database management system used for storing exercise data.

## Project Status

The project is currently in active development, aiming to create a robust backend to support the Exercise Tracker application.

## Features

- **CRUD Operations:** Perform Create, Read, Update, and Delete operations on exercise data.
- **Database Integration:** Seamless integration with a MySQL database for efficient data storage and retrieval.

## Project Structure

The project is organized into several files and directories for better maintainability. The main components include:

- `app`: Contains the main application files.
- `config.py`: Configuration settings for the project.
- `models.py`: Definitions of database models.
- `routes.py`: Route definitions for the Flask application.
- `schemas.py`: Marshmallow schemas for data serialization.

## Project Setup

To set up the project locally, follow these steps:

1. Clone the repository.
2. Create and activate a virtual environment (optional but recommended).
3. Install the necessary dependencies using `pip install -r requirements.txt`.
4. Configure the database connection details in your `.env` file.
5. Run the Flask application using `python app.py`.

## Contribution

This project is currently not open to external contributions. However, feedback and suggestions are highly appreciated. If you have any questions or comments, feel free to reach out – your input is valuable!


## License

This project is open-source and is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code. No restrictions apply – use it in any way that suits your needs.