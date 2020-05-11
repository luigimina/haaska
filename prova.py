from haaska import HomeAssistant, Configuration, event_handler
import json

event = {
  "directive": {
    "header": {
      "namespace": "Alexa.Discovery",
      "name": "Discover",
      "payloadVersion": "3",
      "messageId": "1bd5d003-31b9-476f-ad03-71d471922820"
    },
    "payload": {
      "scope": {
        "type": "BearerToken"
      }
    }
  }
}

contest= { }

resp = event_handler(event,contest)

""" with open('event.json', 'w') as outfile1:
    json.dump(event, outfile1, indent=4)

with open('contest.json', 'w') as outfile2:
    json.dump(contest, outfile2, indent=4)    """ 

with open('resp.json', 'w') as outfile3:
    json.dump(resp, outfile3, indent=4)      