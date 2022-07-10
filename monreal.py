import functions_stability
import functions_vulnerability_status

def print_stability_examples():
    profile = "rus_local_vendor"
    print(profile + ": " + str(functions_stability.get_stability_value(profile)))
    profile = "western_vendor_partially_ignores_sanctions"
    print(profile + ": " + str(functions_stability.get_stability_value(profile)))
    profile = "western_vendor_complies_with_formal_sanctions"
    print(profile + ": " + str(functions_stability.get_stability_value(profile)))
    profile = "western_vendor_used_as_backdoor"
    print(profile + ": " + str(functions_stability.get_stability_value(profile)))

# print_stability_examples()

input_data = {
    "software_vendor":{
        "resident_of_russia": False
    },
    "network":{
        "vulnerability_is_on_the_perimeter": False
    },
    "vulnerability":{
        "public_poc_is_available": False,
        "type": "LPE",
        "cvss_base_score": 6
    },
    "business":{
        "impact_on_business_in_case_of_service_failure_is_significant": True
    },
    "security_tools":{
        "exploitation_of_the_vulnerability_is_blocked": False
    }
}

print(functions_vulnerability_status.get_should_we_patch_vulnerability_status(input_data))

