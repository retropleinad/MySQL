"""
The QueryHandler class is fed queries as a string, interprets them, then interacts with the data appropriately.

Steps for reading queries:
1.) Find which appropriate, initial keyword is being called
2.) Find which data is being interacted with
3.) Check for middling keywords

For now, CREATE will be handled separately

Current Plan:
1.) Get basic SELECT up and running
2.) Get basic other things up and running
3.) Figure out how to group middle keywords
"""


class QueryHandler:

    def __init__(self, query):
        self.modifiers = (
            "ADD",
            "ALL"
        )
        self.commands = {
            "ALTER": self.alter,
            "SELECT": self.select,
            "DELETE": self.delete,
            "INSERT": self.insert,
            "UPDATE": self.update,
            "WITH": self.sql_with
        }
        self.input(query)

    def input(self, query):
        if len(query) == 0:
            raise Exception
        entries = query.split(" ")
        if entries[0] in self.commands:
            self.commands[entries[0]](query)

    def alter(self, query):
        pass

    # Steps:
    # 0.) Check to make sure the query is of appropriate length
    # 1.) Check if the next argument is *
    # 2.) If not, grab rows until you reach another keyword/row that doesn't work
    # 3.) FROM
    # 4.) WHERE
    def select(self, query):
        if len(query) < 4:
            raise Exception
        elif query[1] == "*" and query[2] == "FROM":
            pass

    def delete(self, query):
        pass

    def insert(self, query):
        pass

    def update(self, query):
        pass

    def sql_with(self, query):
        pass


test = QueryHandler("SELECT * FROM id")
