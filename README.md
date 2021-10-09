
# Chatapp

Here's a list of the packages we will use to accomplish this:
Start Chatting on  [open-chatapp](https://open-chatapp.herokuapp.com/) .

-   Django
-   HTML5
-   Tailwind CSS
-  daphne
- whitenoise
- django-channels
- postgreSQL
- dj-database-url
- javascript
- websockets
-   and more .

## Code 

### Install Virtualenv 
```
pip install virtualenv
cd /path/to/folder
mkdir chatapp
cd chatapp
python -m venv .
```
### Activate the Virtualenv
```
source scripts/activate
```
### Install Dependencies
```
cd /path/to/folder/chatapp
mkdir src
cd src 
git clone https://github.com/Arvind-4/Chatapp.git .
pip install -r requirements.txt
```

### Run the Code
```
cd /path/to/folder/chatapp/src
./run.sh
```

### Create Super User
```
cd /path/to/folder/chatapp/src
./superuser.sh
```
