student_data = {"id1":{"name":["Sara"],"age":[12],"subject_integration":["Sci","Eng","Math"]},
                "id2":{"name":["Jack"],"age":[11],"subject_integration":["Sci","Eng","Math"]},
                "id3":{"name":["Sara"],"age":[12],"subject_integration":["Sci","Eng","Math"]},}

result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value

print(result)

        
    