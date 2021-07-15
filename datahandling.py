import collections
import pandas as pd

from collections import defaultdict

class ExtractData:

    def __init__(self):
        
        self.dataFrame = pd.read_excel("cookie_project.xlsx")
        
    def seperated_data(self):

        self.name_list = self.dataFrame["Name "]
        self.sender_class = self.dataFrame["Class"]
        self.recipients = self.dataFrame["Recipients"]
        self.message = self.dataFrame["message"]
        self.recipients_class = self.dataFrame["recipients_class"]
        
        return self.name_list, self.sender_class, self.recipients, self.recipients_class, self.message 

    def compiled_data(self):

        return self.dataFrame.values.tolist()

    def split_message(self,n_message):

        #from collections import defaultdict
        message = self.compiled_data()
        
        # Initialized an empty dictionary with default values
        dictionary = collections.defaultdict(list)

        # Gather all the data into a single dictionary
        for i, split in enumerate(message):
            dictionary["Name"].append(message[i][0])
            dictionary["Class"].append(message[i][1])
            dictionary["Recipient"].append(message[i][2])
            dictionary["Recipient_class"].append(message[i][3])
            dictionary["Message"].append(message[i][4])

        # Create an empty list for the next for loop
        new_message = []
        final_message = []
        
        # A variable to check the length of a message in our data
        message_length = 0
        n_grid = 1
        max_char = 38

        sentence = dictionary["Message"][n_message]
        split_string = list(sentence.split(" "))

        urlist_len = len(split_string)-1

        for index, word in enumerate(split_string):

            get_length = len(word) + 1
            message_length += get_length

            # We have to check if the word is the last one in the list so that we would append it before we break the loop
            if index == urlist_len:
                new_message.append(word)
                new_message = ' '.join(new_message)
                final_message.append(new_message)
                new_message = []
                message_length = 0

            # Check the length of the total characters in one line so that it does not exceed the grid
            if message_length <= max_char:
                new_message.append(word)
                #print(new_message)

            # If it exceeds, clear the new_message list and set the message_length back to zero
            elif message_length > max_char:
                new_message.append(word)
                new_message = ' '.join(new_message)
                final_message.append(new_message)
                new_message = []
                message_length = 0
                
        # Will return something like this ['My name is Muhammad Khalid Al-Walid', 
        # 'and this is just a test for my python', 'program cookie project']
        return final_message

