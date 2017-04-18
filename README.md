# CTC-web-app
A web application for the Cascades Tech Club. Built using Flask.

## To use this code you will need to set some things up first:
- Create a folder where the code will live and pull it on down
- If you don't have python installed, get dat
- It's good practice to use a virtual environment but you don't have to
	- I use VirtualEnv, install it by running:
		- `$ pip install virtualenv`
	- If you want to go this route, you need to then create your virtual environment
	  and give it a name for example if ENV is your desired virtual environment, run:
      - `$ virtualenv ENV`
      - Also, make sure your .gitignore file contains the correct name of your virtual environment,
      by default it ignores `venv` under the heading `#virtual environment`
	- Then turn your new virtual environment on by running:
		- `$ source bin/activate`
        - `or on Windows: ENV\Scripts\activate`
	- You should now see a `(ENV)` before your prompt
- In the root of the project run:
	- `$ pip install -r requirements.txt`
- You will now need to set some environment variables:
	- To give a user admin rights set the `CTC_ADMIN` variable:
	  - `$ export CTC_ADMIN=youremailhere@example.com`
	- In order for the emailer to work properly:
	  - `$ export MAIL_USERNAME=emailformailer@example.com`
	  - `$ export MAIL_PASSWORD=emailpasswordhere`
	- By default SQLite is used but if you want to use a different DB
	  you will need to set the DB URI environment variables:
	  - For development set `DEV_DATABASE_URL`
	  - For testing set `TEST_DATABASE_URL`
	  - For production set `DATABASE_URL`
	  - I'm using MySQL with a URI variable set like this:
	  	- `$ export DATABASE_URL=mysql://username:password@localhost/db_name`
- You're almost up and running, you will now have to deploy the database model to do that run:
	- `$ python manage.py deploy`
- Your environment should be ready to go! To start the server run:
	- `$ python manage.py runserver`

### If you want to build off this project I suggest reading [Miguel Grinberg's](http://shop.oreilly.com/product/0636920031116.do) book.
#### Reach out if you have questions!
