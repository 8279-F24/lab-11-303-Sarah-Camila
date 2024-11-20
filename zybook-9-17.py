contact_list_input = input()
search_name = input()

contacts = {}
for entry in contact_list_input.split():
    name, phone = entry.split(',')
    contacts[name] = phone

print(contacts[search_name])
