# read data from a json file
import json
import pprint as pretty
with open('more_sales_staff.json') as f:
    data = json.load(f)
    output = ''
    for person in data:
        id = person['id']
        indexStatement = {"index" :{"_id" :id}}
        output = output + str(indexStatement) +"\n" + str(person) + "\n"
    output = output.replace("'", "\"")
    print(output)
text_file = open("formatted.json", "w")
text_file.write(output)
text_file.close()
