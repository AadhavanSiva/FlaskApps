# FlaskApps

Database Requirements:

Connects to MySql database that is installed locally and take login credentials from below system environment variables:
         authentication.mysql.login.id
         authentication.mysql.login.password

Environment Variables:

Set the following environment variables before running the UserAuthentication app (a local `.env` file is gitignored and can be used to store them):

         authentication.mysql.login.id       MySQL username
         authentication.mysql.login.password MySQL password
         AUTHENTICATION_SECRET_KEY           Flask secret key for the UserAuthentication app
         AUTHENTICATION_MYSQL_HOST           MySQL host (defaults to localhost)
         AUTHENTICATION_MYSQL_DB             MySQL database name (defaults to authentication)
         OAUTH_SECRET_KEY                    Flask secret key for the Oauth app
         GOOGLE_OAUTH_CLIENT_ID              Google OAuth client ID
         GOOGLE_OAUTH_CLIENT_SECRET          Google OAuth client secret
