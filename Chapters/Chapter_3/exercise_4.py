from io import StringIO

import json
import pandas as pd
data = [
 {"Empno":9001,"Salary":3000},
 {"Empno":9002,"Salary":2800},
 {"Empno":9003,"Salary":2500}
]
json_data = json.dumps(data)
salary = pd.read_json(StringIO(json_data))
salary = salary.set_index('Empno')
salary.loc[9004] = 3100

data = [[9001,'Jeff Russell', 'sales'],
 [9002,'Jane Boorman', 'sales'],
 [9003,'Tom Heints', 'sales']]
emps = pd.DataFrame(data, columns = ['Empno', 'Name', 'Job'])
column_types = {'Empno': int, 'Name': str, 'Job': str}
emps = emps.astype(column_types)
emps = emps.set_index('Empno')

emps = emps.join(salary, how = 'left')
print(emps)
emps = emps.drop(columns=['Salary'])
emps = emps.join(salary, how = 'outer')

print(emps)