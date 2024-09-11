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

```
Casting Assistant: Can view actors and movies
Casting Director: All permissions a Casting Assistant has; Add or delete an actor from the database; Modify actors or movies
Executive Producer: All permissions a Casting Director has; Add or delete a movie from the database
```


***********************************************************************************************************

### Endpoints

```
GET /actors and /movies
DELETE /actors/ and /movies/
POST /actors and /movies and
PATCH /actors/ and /movies/
```

***********************************************************************************************************

### Tokens

```

1. Casting assistant - eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Indwc0N0b2NudkdEZmIwX21OTXZBdyJ9.eyJpc3MiOiJodHRwczovL2Rldi1ndHVrcmZ2ZXYzbXJlcGs4LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNTIzNjExMDI5MzMzOTExNDkwMCIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE3MjYwMzE4OTAsImV4cCI6MTcyNjExODI5MCwic2NvcGUiOiIiLCJhenAiOiJFNzdWZnlPTjhSSm5KczVnOUNrZ3hiZWUwWkMwOVpFZiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.JmXApG1krOd4zHBwBCoMrS8KWP39urcLMIimsfhi7dLwPE_JHxQ3vVywsGqx64OQmeWw-TZy1d2X1lX9XclycbodEji_vnxZMqYqMB-5lCrZNKZTibj9wtrbvR4BCAfeuSn8vb5CMcyZUB3S0q5f4iRwktqRwA3ZcRMnl4ZPjhMtSsDMAlDVGVYbdkL7hqot1kJS91BMLKUWaAw-TUgtctWRhN3pGEpLQOW7C7awHJe15OkKNvKxbecEKvh13gG2Iy5kcff778MXBi5NHI3CQxysYcWMSVqMuqOOGOT7mJKAoSotAqrmzNUDdm1fJ0uG650ti0VXU_msu8zmutHJng

2. Executive producer - eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Indwc0N0b2NudkdEZmIwX21OTXZBdyJ9.eyJpc3MiOiJodHRwczovL2Rldi1ndHVrcmZ2ZXYzbXJlcGs4LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NmRkMWJmODY5ODQ5YTdjYmRhY2ZkNGMiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNzI2MDMzNDA3LCJleHAiOjE3MjYxMTk4MDcsInNjb3BlIjoiIiwiYXpwIjoiRTc3VmZ5T044UkpuSnM1ZzlDa2d4YmVlMFpDMDlaRWYiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.XUdL1qRTSpnoPGiJtQuN-1qXAxnOafsplHrlLgOYM-5tt-ZjuAmvRK0yLdL9a45DknfdYVNfxkUMxUaRgbDmrAf111QWrYHEQSZtrJW6KF0lR6IoOtgHgUi8wCW6wsqHy6fS_Kj0wCdjT4lGXEmEEf0lpVw4opZ19ydt9wYlKPr4zFGwbtJOORTGxJyhcWA6JwSltTFN-a-QTXN1q4lHzMwQQhOS51GOcJqFmX74Fc9Sr0F5HbfgePxlGCNK4Y7Rj_Gby8vpzWwPtDq1MOIqcGEeZS2lmHWO_gCjVMPMfvSRK71qhAw7ce2ErxCJ5FLp_ClHwk7plw1mGMdG0qpuVw

```

***********************************************************************************************************

### Testing

To deploy the tests, run

```bash
python test_app.py
```
