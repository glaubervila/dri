/**
 *
 */
Ext.define('Target.view.objects.Grid', {
    extend: 'Ext.grid.Panel',

    xtype: 'targets-objects-grid',

    requires:[
        'Ext.ux.CheckColumn',
        'Ext.grid.column.Number',
        'Ext.grid.column.Widget',
        'Ext.ux.rating.Picker'
        // 'Ext.grid.filters.Filters'
    ],

    /**
    * @event ready
    * Evento disparado depois que a grid de objetos e reconfigurada
    * @param {Portal.view.target.Objects} [this] this panel
    */

    scrollable: true,

    // plugins: 'gridfilters',

    config: {
        ready: false,
        columnRating: true,
        columnAccept: true,
        columnComments: true
    },

    emptyText: 'No data to dysplay.',

    initComponent: function () {
        var me = this;

        Ext.apply(this, {
            columns: [
                Ext.create('Ext.grid.RowNumberer'),
                {text: 'Placeholder',  dataIndex: '', hidden: true}
            ],
            viewConfig: {
                stripeRows: false,
                getRowClass: function (record) {
                    return record.get('reject') === true ? 'rejected-row' : '';
                }
            }
        });

        me.callParent(arguments);
    },

    showHideTilename: function (visible) {

        var me = this,
            headerCt = me.headerCt,
            columns = headerCt ? headerCt.items.getRange() : objectsGrid.columns;

        for (var i in columns) {
            if (columns[i].dataIndex == 'tilename') {

                columns[i].setVisible(visible);
            }
        }

    },

    reconfigureGrid: function (storeColumns) {
        // console.log('Targets Objects - reconfigureGrid(%o)', storeColumns)

        var me = this,
            columns = [];

        // Coluna RowNunber
        columns.push(Ext.create('Ext.grid.RowNumberer', {
            width: 50,
            resizable: true
        }));

        if (storeColumns.count() > 0) {

            flag = false;

            // Criar as colunas de acordo com as propriedades na store
            storeColumns.each(function (record) {
                type = me.getTypeColumn(record.get('data_type'));

                var column = {
                    text: me.createColumnText(record),
                    dataIndex: record.get('catalog_column_name').toLowerCase(),
                    tooltip: me.createColumnTooltip(record)
                };
                if (type != undefined) {
                    column.filter = {type: type, itemDefaults: {emptyText: 'Search for...'}};
                }

                //  Tratamento Tilename default hidden
                if (record.get('catalog_column_name') == 'tilename') {
                    // column.hidden = true;
                    column.width = 120;

                }

                // Tratamento Ra e Dec caso possua colunas com estes ucds
                // Formata a coluna para decimal com 4 casas.
                if ((record.get('ucd') == 'pos.eq.ra;meta.main') ||
                    (record.get('ucd') == 'pos.eq.dec;meta.main')) {

                    column.xtype = 'numbercolumn';
                    column.format = '0.0000';
                    flag = true;
                }

                columns.push(column);

            },this);

            // Coluna Rating
            if ((me.getColumnRating()) && (flag == true)) {

                columns.push({
                    xtype: 'widgetcolumn',
                    width: 100,
                    sortable: true,
                    text: 'Rating',
                    dataIndex: 'rating',
                    tooltip: 'Rating',
                    widget: {
                        xtype: 'rating',
                        // overStyle: 'color: orange;'
                        selectedStyle: 'color: rgb(96, 169, 23);',
                        style: {
                            'color': '#777777'
                        }
                    }
                });
            }
            // Coluna Reject
            if ((me.getColumnAccept()) && (flag == true)) {
                columns.push({
                    xtype: 'checkcolumn',
                    text: 'Reject',
                    dataIndex: 'reject',
                    tooltip: 'Reject'
                });
            }
            // Coluna Comments
            if ((me.getColumnComments()) && (flag == true)) {
                columns.push({
                    text: 'Comments',
                    dataIndex: 'comments',
                    tooltip: 'Comments',
                    align: 'center',
                    renderer: function (value, metadata, record) {
                        var newValue = '';
                        if (value > 0) {
                            if (value == 1) {
                                //newValue = '<img src="resources/comment.png" title="Comment">';
                                newValue = '<i class="fa fa-comment-o"> </i>';
                            } else {
                                //newValue = '<spam class="x-fa fa-comments-o"> </span>';
                                newValue = '<i class="fa fa-comments-o"></i>';

                            }
                        }
                        return newValue;
                    }
                });
            }

        } else {

            columns.push({text: 'Placeholder',  dataIndex: '', hidden: true});
        }

        // // Ultima coluna tamanho variavel
        // var lastColumn = columns[columns.length - 1]
        // lastColumn.flex = 1;

        me.reconfigure(null, columns);

        // Marcar como ready
        me.setReady(true);
        this.fireEvent('ready', this);

    },

    getTypeColumn: function (type) {
        // console.log(type)
        // console.log(typeof(type))
        switch (type) {
            case 'integer':
            case 'real':
            case 'double precision':
            case 'bigint':
            case 'smallint':
                return 'number';
                break;
            case 'text':
                return 'string';
                break;
            // default:
        }
    },

    createColumnText: function (record) {

        var unit = record.get('unit'),
            name = record.get('property_name');

        var text = unit != '' ? Ext.String.format('{0} ( {1} )', name, unit) : name;

        return text;

    },

    createColumnTooltip: function (record) {

        var tpl = new Ext.XTemplate(
            '<div>',
            '<p><spam>{property_name}</spam></p>',
            '<tpl if=\'catalog_column_name != ""\'>',
                '<p><spam>Name:</spam> {catalog_column_name}</p>',
            '</tpl>',
            '<tpl if=\'unit != ""\'>',
                '<p><spam>Unit:</spam> {unit}</p>',
            '</tpl>',

            '<tpl if=\'ucd != ""\'>',
                '<p><spam>ucd:</spam> {ucd}</p>',
            '</tpl>',

            '<tpl if=\'reference != ""\'>',
                '<p><spam>Reference:</spam> {reference}</p>',
            '</tpl>',

            '</div>'
        );

        return tpl.apply(record.data);
    }
});
