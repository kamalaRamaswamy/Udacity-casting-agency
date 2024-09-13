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

1. Casting assistant - eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Indwc0N0b2NudkdEZmIwX21OTXZBdyJ9.eyJpc3MiOiJodHRwczovL2Rldi1ndHVrcmZ2ZXYzbXJlcGs4LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNTIzNjExMDI5MzMzOTExNDkwMCIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE3MjYyMDQyNTUsImV4cCI6MTcyNjI5MDY1NSwic2NvcGUiOiIiLCJhenAiOiJFNzdWZnlPTjhSSm5KczVnOUNrZ3hiZWUwWkMwOVpFZiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.FM38AaNQToF_-MpMneW77btKBsPP0c3v-joT5NuSHSqTlvljqnTDe7qeUTC_xBA0N9nrg-T2UygB4clSHzP5tH0PcwWkHIKYHx42jJlGSxlboA9h7P9kWehf2C1pJlkRLRDJcK-A_m03-t4sbx6guCch396FuesC53W4JHLJ75BIvzuV5AxDW8gfPp6Mhu3kAQf5XYAeMoC1k65fk3eKtIQJjIyScBx2srWdutnp2DMfo862E3NL4_gSn-0c5MiyywMrljqbo07GHOAg2SN5PwCKBCAtr8S8R-LeiNHpj_A6WZUNT_dKogataS3lApD4PrsszhEI-BjdN2bqaQIw-Q

2. Executive producer - eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Indwc0N0b2NudkdEZmIwX21OTXZBdyJ9.eyJpc3MiOiJodHRwczovL2Rldi1ndHVrcmZ2ZXYzbXJlcGs4LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NmRkMWJmODY5ODQ5YTdjYmRhY2ZkNGMiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNzI2MjAzMjgwLCJleHAiOjE3MjYyODk2ODAsInNjb3BlIjoiIiwiYXpwIjoiRTc3VmZ5T044UkpuSnM1ZzlDa2d4YmVlMFpDMDlaRWYiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.edQKWG2VYbLldKku5Log-K3jBj0g4KW87afqHwTrsPfQ6x9Oyb-HWpFyw83kVoLDhNSjjNTRhGuZwnjubXEfaqTcpK0alR-yQxdEzK1COn9e7Y8m4mu16wwwUXsi1huu2KW4gvhEkUnRqi_rpI2Dy4GrEnEJJCCW2S2CZLpmLd7lY7mKTN1LD8tik9VJA-KwF1e5r9hNTrgDT4xjkyWpcLdnrwKuTqPZLo2lcV2NFrWVj3b_GWLDyj9QOYA3GO5okS7qTmy44WeZMGQxzrdN2ZhvbZ9tJ1xiN-NWIrvFya3AxJRShxiUH-5kofO1Z34376Svkqy5frPerWgB1OqMLg

```

***********************************************************************************************************

### Testing

To deploy the tests, run

```bash
python test_app.py
```
