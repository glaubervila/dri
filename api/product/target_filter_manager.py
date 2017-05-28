import dri.settings
from dri.settings.local_vars import *
from sqlalchemy import create_engine, inspect, MetaData, func, Table
from sqlalchemy.sql import select
from lib.sqlalchemy_wrapper import DBDRIHelper, DBOracle
from sqlalchemy.sql.expression import Executable, ClauseElement
from sqlalchemy.ext.compiler import compiles
import csv
from tabulate import tabulate

class CreateTableAs(Executable, ClauseElement):
    """
    Creates a new table in the database using a query result.
    """
    def __init__(self, schema, name, query):
        self.schema = schema
        self.name = name
        self.query = query


# Os DB que uso podem usar a mesma sintaxe.
@compiles(CreateTableAs)
def _create_table_as(element, compiler, **kw):
    _schema = "%s." % element.schema if element.schema is not None else ''
    return "CREATE TABLE %s%s AS (%s)" % (
        _schema,
        element.name,
        compiler.process(element.query))


class DBPool:
    engine = None

    @staticmethod
    def getConnection():
        if not DBPool.engine:
            print("Creating engine")
            db = DBOracle(DBDRIHelper.prepare_connection("catalog"))
            DBPool.engine = create_engine(db.get_string_connection())
        return DBPool.engine.connect()


class FilterCommand:
    "Implements routines to convert target filter into product"
    def __init__(self, filter_id):        
        self.filter_id = filter_id
        self.conn = DBPool.getConnection()

    def createSQLFromFilter(self):
        return "select * from (select * from nomad) where ROWNUM <= 5"

    def getHeaders(self):
        return ['ra','dec', 'value']

    def execute(self):
        pass

class SaveFilterAsProduct(FilterCommand):
    "Implements routines to convert target filter into product"
    def __init__(self,tablename, filter_id):
        self.tablename = tablename
        super().__init__(filter_id)

    def createTableFromFilter(self):
        self.conn.execute("create table " + self.tablename + " as (" + self.createSQLFromFilter() + ")")

    def registerProductFromFilter(self):
        pass

    def execute(self):
        self.createTableFromFilter()
        self.registerProductFromFilter()
        self.conn.close()

class ExporteFilter(FilterCommand):
    "Implement Methods to export target filter into many formats"
    def __init__(self, filter_id):
        super().__init__(filter_id)

    def export2CSV(self, filename):
        q = self.conn.execute(self.createSQLFromFilter())
        outfile = open(filename, 'w')
        outcsv = csv.writer(outfile)
        outcsv.writerows(q.fetchall())
        outfile.close()

    def export2FITS(self):
        pass

    def export2LatexTable(self, filename):
        q = self.conn.execute(self.createSQLFromFilter())
        outfile = open(filename, 'w')
        outfile.write(tabulate(q.fetchall(), self.getHeaders(), tablefmt="latex"))
        outfile.close()

    def export2JSON(self):
        pass

class ReportFilter(FilterCommand):
    "Implements method to get a report from a target filter"
    def __init__(self, filter_id):
        super().__init__(filter_id)


