import json
import functions
csv_content = functions.readlines("csv_file.txt")

csv_list = [line.strip() for line in csv_content]
json_list = []
for element in csv_list:
    new = element.split(",")
    json_list.append({"Name": new[0], "Score": new[1], "Country": new[2]})

functions.json_write(json_list, "json_file.txt")
