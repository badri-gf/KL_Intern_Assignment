import json
list=["badri","sabari","rakesh","vamshi","gayathri","omesh","rakesh","aashrith"]
with open('python files.txt', 'w') as f:  #open python names.txt file in write mode
    f.write(json.dumps(list))             #writing the list into the text file
