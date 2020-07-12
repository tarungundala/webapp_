
from flask import Flask

import os
from datetime import datetime

from flask import render_template, request, redirect

from database import createdb

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index1():
    return redirect('/orders')

@app.route('/orders', methods=['GET', 'POST'])
def orders():
    global query1
    global query2
    if request.method == 'POST':




        global z1

        database = createdb()

        if request.form['search'] != '' and  request.form['searchtime'] != '' :
            z1 = database.loc[database['product'].str.contains(request.form['search'])]
            query2 = datetime.strptime(request.form['searchtime'], '%Y-%m-%d')
            query3 = datetime.strftime(query2, '%d/%m/%Y')
            z2 = z1.loc[z1['Date'] == query3]
            z2.reset_index(drop=True, inplace=True)
            return render_template('/webpage.html/', tables=[z2.to_html()], titles=z2.columns.values)

        if request.form['search'] != '':

            z1 = database.loc[database['product'].str.contains(request.form['search'])]
            z1.reset_index(drop=True, inplace=True)
            return render_template('/webpage.html/', tables=[z1.to_html()], titles=z1.columns.values)

        elif request.form['searchtime'] != '':

            query2 = datetime.strptime(request.form['searchtime'],'%Y-%m-%d')
            query3 = datetime.strftime(query2,'%d/%m/%Y')
            print(query3)
            z1 = database.loc[database['Date'] == query3]
            z1.reset_index(drop = True,inplace = True)
            return render_template('/webpage.html/', tables=[z1.to_html()], titles=z1.columns.values)


        return redirect('/')
    return render_template('/webpage.html/')


if __name__ == '__main__':
    app.run()
