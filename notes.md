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
cd /home/project/xrwvm-fullstack_developer_capstone/server
source djangoenv/bin/activate
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

# create admin with staff access
python3 manage.py createsuperuser
python3 manage.py runserver

# database express-mongodb
cd /home/project/xrwvm-fullstack_developer_capstone/server
source djangoenv/bin/activate
cd /home/project/xrwvm-fullstack_developer_capstone/server/database
docker build . -t nodeapp
docker-compose up

# sentiment analyzer
cd /home/project/xrwvm-fullstack_developer_capstone/server
source djangoenv/bin/activate
cd xrwvm-fullstack_developer_capstone/server/djangoapp/microservices
# check if running
ibmcloud ce app list
# else rebuild
docker build . -t us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer
docker push us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer
ibmcloud ce application create --name sentianalyzer --image us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer --registry-secret icr-secret --port 5000

# kill persisting process on port 
  find process and kill it:  
  netstat -anp | grep '<port>'
  kill -9 <pid>

# build client-side/frontend
cd /home/project/xrwvm-fullstack_developer_capstone/server/frontend
npm install
npm run build

# git
git config --list
git config --global user.email <>
git config --global user.name <>