with open("Practice1.txt","w") as f:
    f.write("High everyone\nwe are learning  file ")
    f.write("I like Java programming")
data = f.read()
new_data = data.replace("Java","Python")
print(new_data)
