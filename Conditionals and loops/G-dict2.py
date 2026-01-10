#list of dictionaries

students = [
  {"name":"Yash","house":"Sonipat","College":"HMR"},
  {"name":"Priyansh","house":"Delhi","College":"HMR"},
  {"name":"Aksh","house":"Delhi","College":"HMR"},
  {"name":"Nishant","house":"Delhi","College":None}  #none represent the absence of values


]


for student in students:
  print(student["name"] ,student["house"],student["College"], sep="->") 