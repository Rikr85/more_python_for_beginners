class Loggable:
    def __init__(self):
        self.title = ''
    def log(self):
        print('Log message from ' + self.title)

class Connection:
    def __init__(self):
        self.server = ''
    def connect(self):
        print('Connecting to database on ' + self.server)

def framework(item):
    if isinstance(item, Connection):
        item.connect()
    if isinstance(item, Loggable):
        item.log()

# Use the framework
# Inherit from Connection and Loggable        
class SqlDatabase(Connection, Loggable):
    def __init__(self):
        self.title = 'Sql Connection Demo'
        self.server = 'Some_Server'
 
# sql_connection = SqlDatabase()

class JustLog(Loggable):
    def __init__(self):
        self.title = 'Just logging'

# sql_connection = SqlDatabase()
# framework(sql_connection)
        
just_log = JustLog()
framework(just_log)