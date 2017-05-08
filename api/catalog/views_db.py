from lib.CatalogDB import CatalogDB

from sqlalchemy.sql.expression import literal_column, between
from sqlalchemy.sql import select, and_, or_


class CoaddObjectsDBHelper():
    def __init__(self, table, schema=None, database=None):
        self.schema = schema

        if database:
            com = CatalogDB(db=database)
        else:
            com = CatalogDB()

        self.db = com.database
        if not self.db.table_exists(table, schema=self.schema):
            raise Exception("Table or view  %s.%s does not exist" %
                            (self.schema, table))

        self.table = self.db.get_table_obj(table, schema=self.schema)

    def create_columns_sql_format(self, columns):
        t_columns = self.table
        if columns is not None:
            acolumns = columns.split(',')
            if len(acolumns) > 0:
                t_columns = list()
                for col in acolumns:
                    t_columns.append(self.db.get_column_obj(self.table, col))
        return t_columns

    def create_stm(self, params, properties):
        # Parametros de Paginacao
        limit = params.get('limit', 1000)
        start = params.get('offset', None)

        # Parametros de Ordenacao
        ordering = params.get('ordering', None)

        # Parametro Columns
        pcolumns = params.get('columns', None)
        columns = self.create_columns_sql_format(pcolumns)

        coordinate = params.get('coordinate', None)
        if coordinate is not None:
            coordinate = coordinate.split(',')
        bounding = params.get('bounding', None)
        if bounding is not None:
            bounding = bounding.split(',')
        maglim = params.get('maglim', None)

        coadd_object_id = params.get('coadd_object_id', None)

        property_id = properties.get("meta.id;meta.main", None).lower()
        property_ra = properties.get("pos.eq.ra;meta.main", None).lower()
        property_dec = properties.get("pos.eq.dec;meta.main", None).lower()
        property_id_t = self.db.get_column_obj(self.table, property_id)
        property_ra_t = self.db.get_column_obj(self.table, property_ra)
        property_dec_t = self.db.get_column_obj(self.table, property_dec)

        filters = list()
        if coordinate and bounding:
            ra = float(coordinate[0])
            dec = float(coordinate[1])
            bra = float(bounding[0])
            bdec = float(bounding[1])

            _filters = list()
            if property_ra:
                _filters.append(between(literal_column(str(property_ra_t)),
                                        literal_column(str(ra - bra)),
                                        literal_column(str(ra + bra))))
            if property_dec:
                _filters.append(between(literal_column(str(property_dec_t)),
                                        literal_column(str(dec - bdec)),
                                        literal_column(str(dec + bdec))))
            filters.append(and_(*_filters))

        if maglim is not None:
            # TODO a magnitude continua com a propriedade hardcoded
            maglim = float(maglim)
            mag_t = self.db.get_column_obj(self.table, 'mag_auto_i')
            filters.append(
                literal_column(str(mag_t) <= literal_column(maglim))
            )

        if coadd_object_id is not None:
            filters.append(
                literal_column(str(property_id_t) ==
                               literal_column(str(coadd_object_id)))
            )

        with self.db.engine.connect() as con:
            stm = select(columns).select_from(self.table).\
                            limit(literal_column(str(limit)))
            rows = con.execute(stm).fetchall()
        return rows
