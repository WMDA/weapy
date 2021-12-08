from modules.enumerate.enum import find_input_forms, get_form_details


def payloads():
    payloads={
        'basic': "<script>alert('weapy')</script>"
    
    
    }


def xss_scanner(url):
    forms = find_input_forms(url)
    details = get_form_details(forms)

