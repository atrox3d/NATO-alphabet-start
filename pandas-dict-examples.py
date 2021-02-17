test_dict = {
    #  "col1": [f"column1:{x}" for x in range(2)],
    #  "col2": [f"column2:{x}" for x in range(2)]
    "student": ["robb", "fabb"],
    "score": [50, 70],
}

print("test_dict")
print(test_dict)
print("*" * 80)

for key, val in test_dict.items():
    print(f"key={key}, val={val}")
print("*" * 80)

import pandas

testdf = pandas.DataFrame(test_dict)

print("testdf\n", testdf)
print("*" * 80)

for key, val in testdf.items():
    print(f"key={key}\nval:\n{val}")
print("*" * 80)

for index, row in testdf.iterrows():
    print("index:", index)

for index, row in testdf.iterrows():
    print(row, "\n")
print("*" * 80)
for index, row in testdf.iterrows():
    print(row.student, row.score)
