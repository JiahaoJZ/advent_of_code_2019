'''
Input -> path(str)
Output -> the content of the file as str
'''
def Read(path):
  f = open(path, 'r')
  return f.read()

'''
Input -> path(str)
Output -> an array with each line as a element
'''
def ReadLines(path):
  f = open(path, 'r')
  data = f.read()
  return data.split('\n')

'''
Input -> path(str)
Output -> an array with each data as a element
'''
def ReadWithCommaSeparator(path):
  f = open(path, 'r')
  data = f.read()
  return data.split(',')
