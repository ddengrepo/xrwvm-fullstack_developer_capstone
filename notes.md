# dev env setup
cd /home/project/xrwvm-fullstack_developer_capstone/server
pip install virtualenv
virtualenv djangoenv
source djangoenv/bin/activate
python3 -m pip install -U -r requirements.txt

# setup terminal when needed
cd /home/project/xrwvm-fullstack_developer_capstone/server
source djangoenv/bin/activate

# source updates made to db scheme(models)
python3 manage.py makemigrations
python3 manage.py mirgrate
python3 manage.py runserver

# create admin with staff access
python3 manage.py createsuperuser
python3 manage.py runserver

# microservice
docker build . -t nodeapp
docker-compose up

# kill persisting process on port 
  find process and kill it:  
  netstat -anp | grep '<port>'
  kill -9 <pid>

# build client-side
cd /home/project/xrwvm-fullstack_developer_capstone/server/frontend
npm install
npm run build

# git
git config --list
git config --global user.email <>
git config --global user.name <>