class User:
    def __init__(self, conn, addr, name=None, group_id=None):
        self.conn = conn
        self.addr = addr
        self.name = name
        self.group_id = group_id

    def set_name(self, name):
        self.name = name

    def set_group_id(self, group_id):
        self.group_id = group_id

    def get_group(self):
        return self.group_id
    
