def test():
    
    from collections import defaultdict

    message = [['Natasha Alia', 19.3, 'name_1296', 14.2, 
    'My name is Muhammad Khalid Al-Walid and this is just a test for my python program cookie project'], 
    ['Khalid Al-Walid', 19.3, 'name_1297', 14.2, 
    'My name is Muhammad Khalid Al-Walid and this is just a test for my python program cookie project'], 
    ['Peekabo', 19.3, 'name_1298', 14.2, 
    'My name is Muhammad Khalid Al-Walid and this is just a test for my python program cookie project']]

    dictionary = collections.defaultdict(list)
    print(dictionary)

    for i, split in enumerate(message):
        dictionary["Name"].append(message[i][0])
        dictionary["Class"].append(message[i][1])
        dictionary["Recipient"].append(message[i][2])
        dictionary["Recipient_class"].append(message[i][3])
        dictionary["Message"].append(message[i][4])

    print(dictionary)


    
if __name__ == '__main__':
    
    games = []
    while True:
        a = input()
        if a == '':
            break
        else:
            games.append(a)

    print(games)