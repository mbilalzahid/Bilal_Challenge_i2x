Complete Documentation
----------------------

I used Python 3.7

1. User Registration
	- This service creates and registers a new user.

	API Endpoint 	: /api/accounts/register/
	Request Type 	: POST
	Request Params 	: username, email, password, password_2, first_name, last_name, invite_code
	Non-mandatory params : invite_code

	Response Http status codes : HTTP_200_OK or HTTP_400_BAD_REQUEST
	
	Sample Input 	: {
    "username": "ken",
	"email": "test@gmail.com",
	"password": "password",
	"password_2": "password",
	"first_name": "Ken",
	"last_name": "Ben"
	}

2. User Email Verification
	- This service verifies the email to activate the user account. User receives an email on successful registration with the verification_code.
	
	API Endpoint 	: /api/accounts/verify/<verification_code>/
	Request Type 	: GET
	Request Params 	: invite_code
	
	Response Http status codes : HTTP_200_OK or HTTP_404_NO_CONTENT
	
3. User Login
	- This service requires the user credentials and then returns authentication token after successful user login

	API Endpoint 	: /api/accounts/login/
	Request Type 	: POST
	Request Params 	: email (or username) and password
	
	Response 	: { "token": <token> }
	HTTP status code: HTTP_200_OK or HTTP_400_BAD_REQUEST
	
	Sample Input 	: {
	"email": "test@gmail.com",
	"password": "password"
	}
	
4. User Request for Password Reset
	- This service sends an email to user containing password reset link

	API Endpoint 	: /api/accounts/password_reset/
	Request Type 	: POST
	Request Params 	: email
	HTTP status code: HTTP_200_OK
	
	Sample Input 	: {
	"email": "test@gmail.com"
	}
	
5. User Password Change
	- This service changes the password. Link as received from email using above request (4).
	
	API Endpoint 	: /api/accounts/reset/<reset_code>/
	Request Type 	: POST
	HTTP status code: HTTP_200_OK or HTTP_400_BAD_REQUEST
	
	Sample Input 	: {
	"new_password": "12345678",
	"new_password_2": "12345678"
	}

6. User Retrieve Profile
	- This service retrieves the logged in users profile

	API Endpoint 	: /api/accounts/user-profile/
	Request Type 	: GET
	Request Headers : 
		Authorization : Token <token>
	HTTP status code: HTTP_200_OK or HTTP_401_UNAUTHORISED
	
7. Team Create
	- This service create a new team

	API Endpoint 	: /api/teams/create/
	Request Type 	: POST
	Request Headers : 
		Authorization : Token <token>
	HTTP status code: HTTP_200_OK or HTTP_400_BAD_REQUEST or HTTP_401_UNAUTHORISED
	
	Sample Input 	:{
		"name": "Django Developers",
		"description": "Best i2x team in the world"
	}
	
8. Team Invite
	- This service invites other users to join the team.

	API Endpoint 	: /api/teams/<team_id>/invite/
	Request Type 	: POST
	Request Headers : 
		Authorization : Token <token>
	HTTP status code: HTTP_200_OK or HTTP_400_BAD_REQUEST or HTTP_401_UNAUTHORISED
	
	Sample Input 	:{
	"emails": ["test@gmail.com"]
	}	


How to run the project locally
------------------------------

1. Clone the repository

2. Go to directory of manage.py and install the requirements using folling command

	pip install -r requirements.txt
	
**Note:**
You may configure the virtual environment if required.

For instructions, click here : https://virtualenv.pypa.io/en/latest/installation/
    
3. Create local_settings.py inside i2x_demo directory. (OR else you can just change following field in i2x_demo/setting.py)

	EMAIL_HOST_USER = '<to_be_filled>'

	EMAIL_HOST_PASSWORD = '<to_be_filled>'

	DEFAULT_FROM_EMAIL = '<to_be_filled>'

**Note:**
By default, Sqlite3 database is used. You may also use different database in local_settings file if required.

4. Run migrations

	python manage.py migrate

5. Run the server.

	python manage.py runserver
	
	
	
## Configuration Variables ##

#### VERIFICATION_KEY_EXPIRY_DAYS ####

Validity (in days) of user account activation email. Defaulted to 2
	
#### SITE_NAME ####

Name of Website to be displayed on outgoing emails and elsewhere. Defauled to i2x Demo

#### PASSWORD_MIN_LENGTH #### 

A constraint that defines minimum length of password. Defaulted to 8

#### INVITATION_VALIDITY_DAYS #### 

Validity (in days) of user team invitation email. Defaulted to 7
