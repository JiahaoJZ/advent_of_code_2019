import FileParser

def fuel_requiered(data):
  for line in data:
    print(line + ";")

content = FileParser.get_file_contents("data_1_data.txt")
fuel_requiered(content)
