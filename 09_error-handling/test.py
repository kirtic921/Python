file=open('youtube.txt', 'w')

try:
    file.write("python")
finally:
    file.close()

# OR Better way to handle

with open('youtube.txt', 'w') as file:
    file.write("python")