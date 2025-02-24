import pandas as pd

data_nam = [name.capitalize() for name in ['jeff russell','jane boorman','tom heints']]
data_em = ['jeff.russell','jane.boorman','tom.heints']
data_num = ['15846293714', '26738467263', '14947372839']

emps_names = pd.Series(data_nam,index=[9001,9002,9003], name = 'names')
emps_emails = pd.Series(data_em,index=[9001,9002,9003], name = 'emails')
emps_phones = pd.Series(data_num,index=[9001,9002,9003], name = 'phone_number')

emps_df = pd.concat([emps_names, emps_emails, emps_phones], axis=1)

print(emps_df)