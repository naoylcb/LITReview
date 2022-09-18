*(Project realized during my training)*

# LITReview

Site allowing to consult or request a book review on demand.

## Installing and running

If you already have Python installed, make sure it is up to date.
If not, download and install Python. [Website](https://www.python.org/downloads/)

Start by downloading the repository by clicking on the "Code" menu, then "Download ZIP".

Extract the folder. 

In it, create and activate a virtual environment. To do this:
- Open your terminal and place yourself in the extracted folder,
- Run the command: `python -m venv env`,
- Then run the command: `source env/bin/activate` (On Windows, activation will be done with the file env/Scripts/activate.bat).

Still in the terminal, install the dependencies by running the command: `pip install -r requirements.txt`.

Move to the "litreview_project" folder and run the command: `python manage.py runserver`

In your browser, write in the url : http://127.0.0.1:8000/

You can connect with this account to test the interface : yoan | test-test1