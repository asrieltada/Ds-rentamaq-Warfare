FROM mcantillana/django_unab:3
ADD requirements.txt /code
RUN pip install --upgrade pip
RUN pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2 oauth2client unipath jsonpickle
RUN pip install -r requirements.txt
ADD . /code