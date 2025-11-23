import json

dictionary = {
    "profile1": {
        "name" : "melih",
        "email": "test.mail@email.com.tr"
    }
}

with open("zoom_automation_data.json","w") as file:
    write_json = json.dumps(dictionary)
    file.write(write_json)