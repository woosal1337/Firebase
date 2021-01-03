import pyrebase
from credentials.credentials import credentials
credentials = credentials()

firebase = pyrebase.initialize_app(credentials)

db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

