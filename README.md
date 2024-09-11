DESCRIPTION

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

Hosted on Render - https://udacity-casting-agency-dfc1.onrender.com/actors


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

### Models

```
Movies with attributes title and release data.
Actors with attributes name, age and gender
```

***********************************************************************************************************

### Roles

Casting assistant,
casting directors,
executive directors,


***********************************************************************************************************

### Endpoints

GET /actors and /movies
DELETE /actors/ and /movies/
POST /actors and /movies and
PATCH /actors/ and /movies/
