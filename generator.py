import json
import random
import os

resource = "none"
newfile = False

with open("lastused.txt", "r") as file:
    if os.path.getsize("lastused.txt") == 0:
        print("Please input the resource file name.")
        resource = input()
        print("Selected file: " + resource)
        newfile = True
    else:
        while True:
            print("Use previous resource file or input new? Y to use previous. N to input new. Previous file: " + file.read())
            response = input()
            if response == "Y" or response == "y":
                file.seek(0)
                resource = file.read()
                print("Selected file: " + resource)
                break
            elif response == "N" or response == "n":
                print("Please input the resource file name.")
                resource = input()
                print("Selected file: " + resource)
                newfile = True
                break
            else:
                print("Please input Y or N.")

if newfile == True:
    with open("lastused.txt", "w") as file:
        file.write(resource)

with open(resource, "r") as file:
    data = json.load(file)
    randomcount = "0"
    if data["variables"][0]["randomcount"] < 2:
        base = data["variables"][0]["randombase1"][0]["value"]
        randomcount = "1"
    else:
        randomcount = str(random.randrange(0, data["variables"][0]["randomcount"]) + 1)
        base = data["variables"][0]["randombase" + randomcount][0]["value"]
    for counter in range(8):
        template = "[[Item$]]"
        template = template.replace("$", str(counter))
        finder = counter + 1
        tester = base.find(template)
        if data["variables"][0]["randombase" + randomcount][finder]["randomcount"] == 0:
            print("Variable " + template + " is empty!")
            continue
        roll = random.randrange(0,data["variables"][0]["randombase" + randomcount][finder]["randomcount"]) + 1
        randomtemplate = "random" + str(roll)
        base = base.replace(template, data["variables"][0]["randombase" + randomcount][finder][randomtemplate])

print("Generated sentence: \"" + base + "\"")