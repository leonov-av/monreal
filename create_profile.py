import json

# External events
event_probability = dict()
event_probability["Informal condemnation of the company in the media"] = 50
event_probability["Official sanctions against the country"] = 50
event_probability["Official sanctions against company management"] = 50
event_probability["Official sanctions against the company"] = 50
event_probability["The danger of secondary sanctions against the vendor"] = 50

# Degradation of functionality
action_weight = dict()
action_weight["Remote blocking of additional functions"] = 10
action_weight["Update blocking"] = 15
action_weight["Remote blocking of main functions"] = 30
action_weight["License revocation"] = 45
action_weight["Unauthorized transfer of data to third parties"] = 70

action_on_event_probability = dict()
for event in event_probability:
    action_on_event_probability[event] = dict()
action_on_event_probability["Informal condemnation of the company in the media"]["Remote blocking of additional functions"] = 50
action_on_event_probability["Informal condemnation of the company in the media"]["Update blocking"] = 50
action_on_event_probability["Informal condemnation of the company in the media"]["Remote blocking of main functions"] = 50
action_on_event_probability["Informal condemnation of the company in the media"]["License revocation"] = 50
action_on_event_probability["Informal condemnation of the company in the media"]["Unauthorized transfer of data to third parties"] = 50

action_on_event_probability["Official sanctions against the country"]["Remote blocking of additional functions"] = 50
action_on_event_probability["Official sanctions against the country"]["Update blocking"] = 50
action_on_event_probability["Official sanctions against the country"]["Remote blocking of main functions"] = 50
action_on_event_probability["Official sanctions against the country"]["License revocation"] = 50
action_on_event_probability["Official sanctions against the country"]["Unauthorized transfer of data to third parties"] = 50

action_on_event_probability["Official sanctions against company management"]["Remote blocking of additional functions"] = 50
action_on_event_probability["Official sanctions against company management"]["Update blocking"] = 50
action_on_event_probability["Official sanctions against company management"]["Remote blocking of main functions"] = 50
action_on_event_probability["Official sanctions against company management"]["License revocation"] = 50
action_on_event_probability["Official sanctions against company management"]["Unauthorized transfer of data to third parties"] = 50

action_on_event_probability["Official sanctions against the company"]["Remote blocking of additional functions"] = 50
action_on_event_probability["Official sanctions against the company"]["Update blocking"] = 50
action_on_event_probability["Official sanctions against the company"]["Remote blocking of main functions"] = 50
action_on_event_probability["Official sanctions against the company"]["License revocation"] = 50
action_on_event_probability["Official sanctions against the company"]["Unauthorized transfer of data to third parties"] = 50

action_on_event_probability["The danger of secondary sanctions against the vendor"]["Remote blocking of additional functions"] = 50
action_on_event_probability["The danger of secondary sanctions against the vendor"]["Update blocking"] = 50
action_on_event_probability["The danger of secondary sanctions against the vendor"]["Remote blocking of main functions"] = 50
action_on_event_probability["The danger of secondary sanctions against the vendor"]["License revocation"] = 50
action_on_event_probability["The danger of secondary sanctions against the vendor"]["Unauthorized transfer of data to third parties"] = 50

profile = {
    "event_probability":event_probability,
    "action_weight":action_weight,
    "action_on_event_probability":action_on_event_probability
}

name = "profile_name"
f = open("vendor_profiles/" + name + ".json", "w")
f.write(json.dumps(profile, indent=4))
f.close()
