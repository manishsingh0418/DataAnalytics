#Convert the following dictionary into JSON format.

# import json
# Student_data ={"name":"David","age":13,"marks":87}
# data = json.dumps(Student_data)
# print(data)
# print(type(data))

#Access the value of age from the given data .

# import json
#
# Student_data ="""{"name":"David","age":13,"marks":87}"""
# data = json.loads(Student_data)
# print(data["age"])


#Pretty print following JSON data.
import json
# Student_data ={"name":"David","age":13 ,"marks":87}
#
# data = json.dumps(Student_data,indent=4,separators=(",","="))
# print(data)

#Sort the following JSON keys and write them into a file.
# Student_data ={"name":"David","age":13,"marks":87}
# f=open("demo.json","w")
# data=json.dumps(Student_data,indent=4,sort_keys=True)
# f.write(data)
#
# print("the data has been added to the file")

#Access the nested key marks from the following nested data
student_data="""{"student":
      {"grade":
      {"name":"David",marks":87}
      }
}"""
data = json.loads(student_data)
print (data["student"]["grade"]["marks"])