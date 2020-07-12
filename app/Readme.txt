# Web Application to display customer order details

Web Application that retrieves order history based on search results using order name (e.g. Sanitizer etc.) or date of purchase using Python, Flask, Sqlite and HTML  

## Getting Started

The application has following files:
 2 python files: app.py and database.py
 1 HTML file: webpage.html
 1 css file: style.css
Install the required frameworks and run the app.py in CMD. Procedure for Framework installation is provided below in the ### Installing section. All the files must be arranged in the following format:

directory
├── app
│    |--- app.py
│    |--- database.py
│    |--- database1.db (will be created automatically when the python file is running)
│    |--- database2.db (will be created automatically when the python file is running)
│   
├── template
│    |--- webpage.html
|
├──static
│    |--- style.css

### Prerequisites
Python 3.6.0
Flask 1.1.2
Pandas 1.0.5
sqlite 3.32.3

### Installing



Install Flask Framework using following command in the command prompt:


```
pip install flask
```

Install Pandas using following command in the command prompt:

```
pip install pandas
```

Install sqlite using 

```
pip install pysqlite
```

## Deploy

In your command prompt, change the directory to the location of app folder

eg: cd C:\Users\tarun\Documents\app

Once the command prompt changes directory, pass the command: python app.py

Once the server runs, you will be able to see the following output in cmd:
 Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

### Test Case
Step 1:
Once the app starts running, you can view the webpage by pasting the port path (for e.g. http://127.0.0.1:5000/) in your desired browser

Step 2:
the port automatically redirects to the /orders page i.e. http://127.0.0.1:5000/orders

Step 3:
In the /orders page, you can view two input fields, 'search' and 'date'. You can search the order with the order name, date or both.
Search example: search using 'Hand' or 'sanitizer' or 'san' or 'Box'
Date example: select date '2020 - 01 - 02' (calender is already provided in the webpage
Search and Date: search for 'san' on '2020 - 01 - 02' to get the search results for sanitizer on 2nd January 2020 
Total of 5 results are generated and to view more, click on the page bar below the table 


   
## Built With

* [Flask](https://flask-doc.readthedocs.io/en/latest/) - The web framework 
* [Python](https://docs.python.org/3/) - Python for Backend
* [SQLite](https://www.sqlite.org/docs.html) - Used to create and manage Database



