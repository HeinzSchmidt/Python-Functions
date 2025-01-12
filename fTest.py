from CybrFunctions import CybrFunctions

form_data = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'interests': ['python', 'data science']
}
cybr = CybrFunctions()
result = cybr.form_to_json(form_data)
print(result)