import pandas as pd
def user_input_getting():
    row = int(input("Enter number of row:"))
    columns_name = input("Enter the column name with , :").split(",")
    data = []
    for i in range(row):
        row_data = input(f"Enter the data with , : {i+1}").split(",")
        # {i=1} for moving to next data input like i = i+1
        data.append(row_data)
        df = pd.DataFrame(data,columns= columns_name)
        return df
df = user_input_getting()
print(df)
        
