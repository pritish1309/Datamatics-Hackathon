# These are imports for using the Gmail API
from simplegmail import Gmail
from simplegmail.query import construct_query
from datetime import date,datetime

# Imports for using vision API
import os, io
from google.cloud import vision_v1


# Import for extracting text from PDF
from PyPDF2 import PdfReader

# Import to send the data to a google form
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Creating environment for vision API (Store the image in the same location as the project)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"visionAPI_token.json"
client = vision_v1.ImageAnnotatorClient()

