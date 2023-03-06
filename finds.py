x = "#איסט סייד | eastside\nhttps://t.me/+BdNuzhVBayplODM0\ntype:url\n#"

# split the string into a list of name, link, and type
data = x.strip().split('\n')
name = data[0].replace("#","")
link = data[1]
file_type = data[2].split(':')[1]

print(name)
print(link)
print(file_type)
