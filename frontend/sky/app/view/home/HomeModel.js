/**
 *
 */
Ext.define('Sky.view.home.HomeModel', {
    extend: 'Ext.app.ViewModel',

    alias: 'viewmodel.home',

    requires: [
        'Sky.store.Releases',
        'Sky.store.Datasets',
        'Sky.store.Footprints',
        'Sky.store.Surveys',
        'Sky.model.Release',
        'Sky.store.Tags',
        'Sky.model.Dataset'
    ],

    links: {
        currentRelease: {
            type: 'Sky.model.Release',
            create: true
        },
        currentDataset: {
            type: 'Sky.model.Dataset',
            create: true
        }
    },

    stores: {
        // Releases  = Todos os releases disponiveis.
        releases: {
            type: 'releases'
        },
        // Tags = esta store e filtrada localmente e possui todos os tags
        // independente de release.
        tags: {
            type: 'tags',
            storeId: 'AllTags',
            autoLoad: true,
            remoteFilter: false
        }, 

        // Datasets = Skys que estao nos tags de um release 
        // esta store e paginada       
        datasets: {
            type: 'datasets'
        },
        // Surveys = Imagens que estao disponiveis para um release
        surveys: {
            type: 'surveys'
        },

        tagsbyrelease: {
            type: 'tags'
        }, 

        tiles: {
            type: 'footprints',
            pageSize: 0
        }

    }

});