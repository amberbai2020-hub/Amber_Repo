# RPS-Game

## Prerequisites

Install python version 3.x (for example using Anaconda)

## Instructions

1. Clone [the repo](https://github.com/amberbai2020-hub/Amber_Repo.git) from GitHub

2. Navigate to the local repo from the command line
#Always need to confirm before running the project

```sh
cd ~/Downloads/Amber_Repo
```

3. Create a new Anaconda virtual environment called "rps-env" (first time only):
#Virtual environment created such that we satisfy the dependencies the code requires, such as the version of Python and the necessary third-party packages

```sh

conda create -n rps-env python=3.11

```

4. Activate the virtual environment (every time you come back to the project):

```sh
conda activate rps-env
```

5. Install package dependencies

```sh
pip install -r requirements.txt
```

## Usage

Run files: 

```sh 

#Shell command here

python app/rps.py

#Alternatively: This directly uses the . functions instead of path location above
#Invoke using Python tools still, but invoked with a -m flag
python -m app.rps

 ```

 #Quality control is important because we want to ensure product quality, user acquisition and experience and retention, reduce maintenance cost and increase profit
 #We can use automated testing or code review to catch the bug in our code
 #Beyonce Rule: If you like it, put a test on it

 #Two school of thought of code testing
 ##1: Put test file in the app directory next to where the code being tested is
 ##2: Create a separate test directory

 ## Testing

 #We run tests to make sure that our code is working

 To run tests:

```sh

pytest

```
#We don't run the test via Python, but use the pytest package instead
#pytest package will find all test files in the directory, and all test functions within the file and run them all

#Refactoring: When we reorgnize the code but the functionality doesn't change

# Alpha Vantage Stock Data 

The instructions below overlap with RPS game instructions, so depending on your progress, please start with the step that best matches your needs.

## Prerequisite

1. Clone [the repo](https://github.com/amberbai2020-hub/RPS-Game.git) from GitHub

2. Navigate to the local repo from the command line
#Always need to confirm before running the project

```sh
cd ~/Downloads/Amber_Repo
```

3. Access API Key: This project requires you to obtain an Alpha Vantage API key, which you can get a premium version by using the [form](https://www.alphavantage.co/support/#api-key) or shared by the professor.

4. Create environment variable: For security purposes, we do not want API keys to be uploaded to Github (you will NOT see a .env file or API key in the github link above)

Double click on the left-side bar of your text editor to create a new local file called ".env". Store your environment variable as the following:

store your environment variable in there:

```sh

ALPHAVANTAGE_API_KEY= "______________"

```

where the blank space represents your personalized API key.

5. Create a new Anaconda virtual environment called "stocks-env" (first time only):

```sh

conda create -n stocks-env python=3.11

```

6. Activate the virtual environment (every time you come back to the project):

```sh
conda activate stocks-env
```

7. Install package dependencies

```sh
pip install -r requirements.txt
```

## Usage

Run files: 

```sh 

python app/stocks.py

#OR

python -m app.stocks

```

## Test

To run tests:

```sh

pytest

```
