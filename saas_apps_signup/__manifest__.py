# Copyright 2020 Eugene Molotov <https://it-projects.info/team/em230418>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": """SaaS Apps: signup""",
    "summary": """Extends saas_apps""",
    "category": "Hidden",
    # "live_test_url": "http://apps.it-projects.info/shop/product/DEMO-URL?version=14.0",
    "images": [],
    "version": "16.0.0.1.1",
    "application": False,
    "author": "IT-Projects LLC, Eugene Molotov",
    "support": "apps@it-projects.info",
    "website": "https://apps.odoo.com/apps/modules/14.0/saas_apps_signup/",
    "license": "AGPL-3",
    "depends": [
        "account_payment",
        "auth_signup_verify_email",
        "base_automation",
        "saas_apps",
        "saas_contract",
        "saas_database_limit",
        "saas_portal",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "data/auth_signup_data.xml",
        "data/website.xml",
        "security/ir.model.access.csv",
        "views/auth_signup.xml",
        "views/calculator.xml",
        "views/portal_templates.xml",
        "views/res_config_views.xml",
    ],
    "demo": [],
    "assets": {
        "web.assets_frontend": [
            "saas_apps_signup/static/src/js/saas_apps.js",
            "saas_apps_signup/static/src/js/signup.js",
        ],
    },
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": "post_init_hook",
    "uninstall_hook": None,
    "auto_install": False,
    "installable": False,
}
