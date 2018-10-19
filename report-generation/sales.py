import json
import pprint as pretty
with open('sales.json') as f: # change the file what every you call sales.json
    data = json.load(f)
    output = ''
    for person in data:
        id = person['id']
        indexStatement = {"index" :{"_id" :id}}
        output = output + str(indexStatement) +"\n" + str(person) + "\n"
    output = output.replace("'", "\"")
    print(output)
text_file = open("formatted.json", "w") # change the file what every yon call formattd.json
text_file.write(output)
text_file.close()
