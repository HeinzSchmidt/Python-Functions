import json

class CybrFunctions:

    def __init__(self):
        pass

    def form_to_json(self, form_data):
        # Convert form data to a dictionary
        form_dict = {}
        for key, value in form_data.items():
            # Handle potential list values for multi-select fields or checkboxes
            if isinstance(value, list):
                form_dict[key] = value
            else:
                form_dict[key] = value.strip() if isinstance(value, str) else value
        
        # Convert the dictionary to JSON
        json_data = json.dumps(form_dict, indent=2)
        
        return json_data