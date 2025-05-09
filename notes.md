once:
pip install virtualenv
virtualenv djangoenv
source djangoenv/bin/activate
python3 -m pip install -U -r requirements.txt


when needed:
source djangoenv/bin/activate
python3 manage.py makemigrations
python3 manage.py mirgrate
python3 manage.py runserver

python3 manage.py createsuperuser
python3 manage.py runserver


  find process and kill it:  
  netstat -anp | grep '<port>'
  kill -9 <pid>

# build client-side
cd /home/project/xrwvm-fullstack_developer_capstone/server/frontend
npm install
npm run build