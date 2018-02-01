*** To setup***
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

*** Admin Credentials***
id : admin
password : movie123

use /api/get_auth_token/ for generating auth token

set Authorization header as Token <token>
with /api/rest/ urls

no auth required for /api/public