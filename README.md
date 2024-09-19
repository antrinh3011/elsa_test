- Read "docs/System Design Document.docx" for more detail about the Architecture Diagram,Data Flow,Technology Justification
- Install VS code or other IDE : https://code.visualstudio.com/docs/languages/python
- Install Python 3.10 : https://www.python.org/downloads/release/python-3100/
- Install MySQL Workbench > Connect to mysql and execute the script name : "db_schema.sql" to create your database
- Execute the mock data by order to the file name in mock_data/
- If you're using the VS code for development. Press Ctrl + Shift + P > Python Create Environment > Create a '.venv' virtual environment in the current workspace
- If you're using the VS code for development. You need to access Terminal > New Terminal and install dependencies Python library
>> pip install -r requirements.txt
- Database migration
>>flask db init
Open file migrations > alembic.ini > Adding the database URL connection
    # database URL
    sqlalchemy.url = mysql+pymysql://root:Admin301188@localhost/quiz_app_db  (change to your mysql account)
>>flask db migrate -m "Initial migration."
>>flask db upgrade
- Start server and checking the app
>> python run.py
- Open some browsers and access the URL for checking : http://127.0.0.1:5000/

ORM : https://www.fullstackpython.com/object-relational-mappers-orms.html