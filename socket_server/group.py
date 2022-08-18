class Group:
    def __init__(self, id, limit):
        self.id = id
        self.limit = limit
        self.people = set()

    def at_limit(self):
        if len(self.people) < self.limit:
            return False
        return True

    def add_user(self, user):
        self.people.add(user)

    def remove_user(self, user):
        self.people.remove(user)

    def get_people(self):
        return self.people