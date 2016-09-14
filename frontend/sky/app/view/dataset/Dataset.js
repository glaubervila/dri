Ext.define('Sky.view.dataset.Dataset', {
    extend: 'Ext.panel.Panel',

    xtype: 'dataset',

    requires: [
        'Sky.view.dataset.Visiomatic',
        'Sky.view.dataset.DatasetController',
        'Sky.view.dataset.DatasetModel',
        'Sky.view.dataset.Compare'
    ],

    controller: 'dataset',

    viewModel: 'dataset',

    config: {
        dataset: null,
        coordinate: null,
        fov: null,
        radec: null,

        defaultFov: 0.5
    },

    initComponent: function () {
        var me = this;

        Ext.apply(this, {
            layout: 'border',
            items: [
                {
                    xtype: 'sky-visiomatic',
                    reference: 'visiomatic',
                    region: 'center',
                    split: true
                },{
                    xtype: 'sky-compare',
                    reference: 'compare',
                    region: 'east',
                    width: 400,
                    split: true,
                    hidden: true,
                    closable: true,
                    closeAction: 'hide'
                    // tools: [
                    //     {
                    //         type:'close',
                    //         tooltip: 'Refresh form Data',
                    //         // hidden:true,
                    //         handler: function(event, toolEl, panelHeader) {
                    //             // refresh logic
                    //         }
                    //     }
                    // ]
                    // collapsible: true,
                    // collapseMode: 'mini',
                    // collapseDirection: 'right'
                }
            ]
        });

        me.callParent(arguments);
    },

    loadPanel: function (arguments) {
        var me = this,
            dataset = me.getDataset(),
            coordinate = me.getCoordinate(),
            fov = me.getFov(),
            vm = this.getViewModel(),
            radec, coordinates;

        if (dataset > 0) {

            vm.set('dataset', dataset);

            me.setParameters(coordinate, fov);

            me.setLoading(true);

            this.fireEvent('loadpanel', dataset, this);
        }
    },

    updatePanel: function (arguments) {
        var me = this,
            old = me.getDataset(),
            dataset = arguments[1],
            coordinate = arguments[2],
            fov = arguments[3],
            vm = this.getViewModel(),
            visiomatic = me.down('sky-visiomatic');

        me.setParameters(coordinate, fov);

        // Remover a ImageLayer do Visiomatic
        visiomatic.removeImageLayer();

        if ((dataset > 0) && (dataset != old)) {
            me.setDataset(dataset);

            vm.set('dataset', dataset);

            this.fireEvent('updatePanel', dataset, this);

        } else {
            this.fireEvent('updatePosition', dataset, this);

        }
    },

    setParameters: function (coordinate, fov) {
        var me = this,
            coordinates, radec;

        coordinate = decodeURIComponent(coordinate);
        if (coordinate.includes('+')) {
            coordinates = coordinate.split('+');

        } else {
            coordinates = coordinate.split('-');
            coordinates[1] = '-' + coordinates[1];
        }

        radec = {
            ra: parseFloat(coordinates[0].replace(',', '.')),
            dec: parseFloat(coordinates[1].replace(',', '.'))
        };

        me.setRadec(radec);

        if (fov) {
            me.setFov(fov.replace(',', '.'));
        } else {
            me.setFov(me.getDefaultFov());
        }

        coordinate = radec.ra + ', ' + radec.dec;
        me.setCoordinate(coordinate);

    }
});
