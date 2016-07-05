
class BaseWrapper():

    def __init__(self, cursor):
        self.cursor = cursor

    def execute(self, query, params=None):
        if (params is None):
            return self.cursor.execute(query)
        else:
            return self.cursor.execute(query, params)

    def fetchall(self, query, params=None):
        return self.execute(query, params).fetchall()

    def fetchone(self, query, params=None):
        return self.execute(query, params).fetchone()

    def fetchall_dict(self, query, params=None):
        """
        Return all rows as a dict
        """
        cursor = self.execute(query, params)
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
            ]

    def fetchall_namedtuple(self, query, params=None):
        """
        Return all rows from as a namedtuple"
        """
        cursor = self.execute(query, params)
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]

    def get_table_columns(self, table):
        """
        Return all columns in a table"
        """
        return self.wrapper.get_table_columns(table)