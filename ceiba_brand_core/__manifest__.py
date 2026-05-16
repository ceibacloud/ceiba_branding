{
    'name': 'Ceiba Branding',
    'version': '18.0.1.0.0',
    'category': 'Hidden',
    'summary': 'Custom branding and UI for Ceiba Clouds',
    'author': 'Ceiba Clouds',
    'website': 'https://www.ceibacloud.com',
    'license': 'LGPL-3',
    'depends': [
        'web',
        'base_setup',
        'portal',
    ],
    'data': [
        'views/login_templates.xml',
        'views/res_config_settings_views.xml',
        'views/portal_templates.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('prepend', 'ceiba_brand_core/static/src/scss/primary_variables.scss'),
        ],
        'web.assets_backend': [
            'ceiba_brand_core/static/src/scss/backend_overrides.scss',
        ],
    },
    'installable': True,
    'auto_install': False,
}
