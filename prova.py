from haaska import HomeAssistant, Configuration, event_handler
import json

#nomefile='./json/Discovery.request.json'
#nomefile='./json/ModeController.SetMode.request.json'
nomefile='./json/PowerController.TurnOn.request.json'
with open(nomefile, 'r') as infile:
    event=json.load(infile)  

contest= { }

resp = event_handler(event,contest)

""" with open('event.json', 'w') as outfile1:
    json.dump(event, outfile1, indent=4)

with open('contest.json', 'w') as outfile2:
    json.dump(contest, outfile2, indent=4)    """ 

with open('./json/resp.json', 'w') as outfile3:
    json.dump(resp, outfile3, indent=4)      