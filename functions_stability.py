import json


def get_stability_value(profile_name):
    #name = "rus_vendor"
    f = open("vendor_profiles/" + profile_name + ".json", "r")
    profile = json.loads(f.read())
    f.close()

    sum_action = 0
    sum_action_max = 0
    for current_event in profile["event_probability"]:
        current_event_probability = profile["event_probability"][current_event]
        for current_action in profile["action_on_event_probability"][current_event]:
            current_action_probability = profile["action_on_event_probability"][current_event][current_action]
            current_action_weight = profile["action_weight"][current_action]
            #print(str(current_event_probability) + " * " + str(current_action_probability) + " * " + str(current_action_weight) )
            sum_action += current_event_probability * current_action_probability * current_action_weight
            sum_action_max += 100 * 100 * current_action_weight
    stability = int((1 - sum_action/sum_action_max) * 100)
    return(stability)