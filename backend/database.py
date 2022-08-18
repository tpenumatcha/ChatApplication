import pymongo


class Database:

    def __init__(self):
        self.db_client = pymongo.MongoClient('localhost', 27017)
        self.db = self.db_client['mydb']
        self.messages = self.db['messages']

    def add_entry(self, entry):
        self.messages.insert_one(entry)
        
        
    def recieve_messages(self, group):
        query = {'group': group}
        return self.messages.find(query)

    def delete_user(self, user):
        query = {'user': user}
        self.messages.delete_one(query)

    def drop(self):
        self.messages.drop()
        self.messages = self.db['messages']