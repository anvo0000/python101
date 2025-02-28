import pandas as pd
PWD_FILE = "mypwd.csv"
columns_name = ["website", "user_name", "pwd"]

website = "chat"
user_name="anvo0000"

def find_pwd(website="", user_name=""):
    df = pd.read_csv(PWD_FILE, sep="|")
    if user_name !="":
        mask = (df["website"]==website) & (df["user_name"]==user_name)
    else:
        mask = (df["website"] == website)
    if mask.any():
        return df.loc[(df["website"]==website) & (df["user_name"]==user_name), ["user_name","pwd"]]

result = find_pwd(website, user_name)
print(result["user_name"].iloc[0])