import pandas as pd

class Excel:

    def __init__(self):
        pass

    def open_an_excel(self, directory):
        data = pd.read_excel(directory)
        pass

data = pd.read_excel(r'C:\Users\khali\OneDrive\My Workspace\CookieProject\Cookie Project KMS.xlsx')
df = pd.DataFrame(data, columns=['name','class', 'recipients', 'recipients_class', 'message'])

data_list = df.values.tolist()
print(len(data_list))