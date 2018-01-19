hosts = '/etc/hosts'


with open(hosts) as file_object:
    contents = file_object.read()
    print(contents.lstrip())