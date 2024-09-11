DESCRIPTION

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

Hosted on Render - https://udacity-casting-agency-dfc1.onrender.com/actors


ROLES

Casting assistant 
casting directors 
executive directors


***********************************************************************************************************

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

To run the server, execute:

```bash
flask run --reload
```

***********************************************************************************************************



***********************************************************************************************************

API Server
All accessable endpoints of the project are located in the app.py file.

Run the following command in the project root folder to start the local development server:

flask run

***********************************************************************************************************

API endpoints

Public endpoints

GET '/movies'
Fetches a dictionary with id and title of movies who posted their release date to the database.
Request Arguments: None
Returns: A JSON object with two keys: 'success' and 'success meessage' - a dictionary with company id and name.
Sample curl request: curl -X GET http://127.0.0.1:5000/movies 

Sample response:

{
    "movies": {
        "1": "Kyle XY",
        "2": "Black Panther",
        "3": "Bob"
    },
    "success": true
}

Sample curl request: curl -X GET http://127.0.0.1:5000/companies 


