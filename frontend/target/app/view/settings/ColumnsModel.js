Ext.define('Target.view.settings.ColumnsModel', {
    extend: 'Ext.app.ViewModel',

    alias: 'viewmodel.columns',

    requires: [
        'Target.model.CurrentSetting',
        'Target.store.ProductDisplayContents',
        'Target.store.ContentSettings'
    ],

    links: {
        currentSetting: {
            type: 'Target.model.CurrentSetting',
            create: true
        }
    },

    stores: {
        currentSettings: {
            type: 'currentsettings'
        },
        displayContents: {
            type: 'product-display-contents',
            autoLoad: false
        },
        contentSettings: {
            type: 'content-settings',
            autoLoad: false
        }
    }
});
