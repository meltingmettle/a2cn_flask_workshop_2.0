import datetime # Allows datetime.now() for creation timestamps
import json # Allows some helpful json formatting
import re # Regex for string parsing capability
import requests # Allows your program to make web requests

from flaskr.db import *

################################################################################
#################### Zendesk Integration B-) ###################################
#
#  The ticket class is built to match the basic ticket as described in the Zendesk API docs
#  https://developer.zendesk.com/rest_api/docs/support/tickets
#
################################################################################

def zendesk_api_post(company, new_ticket):
    headers = {'Content-Type': 'application/json',}


    response = requests.post('https://z3n-hack-in-place.zendesk.com/api/v2/tickets.json', headers=headers, data=new_ticket, auth=("eling@zendesk.com", "REPLACE"))
    if response.status_code == 200 or response.status_code == 201:
        print("Zendesk ticket submitted!")
    else:
        print("breh you broke something")
    return None  # For simplicity

def zendesk_api_update():
    return #TODO

def zendesk_api_delete():
    return #TODO

# Don't forget to add "import datetime", "import json", and "import requests" to the top of your file
# Run "python3 -m pip install requests" or "pip3 install requests"
# From: https://stackoverflow.com/questions/17309288/importerror-no-module-named-requests
class Ticket(object):
    def __init__(self, subject, comment, ticket_type = "urgent", priority = "incident", tags=[]):
        self.id = "PLACEHOLDER"  #This is set by the Zendesk API
        self.url = "PLACEHOLDER" #This is set by the Zendesk API
        self.subject = subject
        self.comment = comment
        self.type = ticket_type
        self.priority = priority
        self.created_at = datetime.datetime.now().strftime("%B %d %Y, %I:%M%p")  #Current timestamp
        self.updated_at = ""  #Apparently, this defaults to created_at
        self.status = "open"
        if tags: #Parse single string input into multiple single-word string tags.  Need to bug test later.
            self.tags = tags.split(",")
        else:
            self.tags = ""

    def ticket_toJSON(self): #subject, comment
        tickets = {"ticket": {
            "id": self.id,
            "url": self.url,
            "subject":  self.subject,
            "comment":  self.comment,
                        "type": self.type,
            "priority": self.priority,
            "created_at": self.created_at,
            "updated_at": "",
            "status": self.status,
            #"problem_id": "TEST SELF SUBMITTER",
            "tags": self.tags
            }
        }
        #Removed some attributes for simplicity while trying to retain as much functionality as possible.
        return json.dumps(tickets)

    def __str__(self):
        return "Ticket #" + str(self.id)
