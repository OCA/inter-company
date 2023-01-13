# Copyright 2017 Florent THOMAS (Mind And Go), Odoo Community Association (OCA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Connector Odoo",
    "summary": """
        Base connector for Odoo To Odoo scenarios""",
    "version": "16.0.2.0.0",
    "website": "https://github.com/yibudak/connector-odoo2odoo",
    "category": "Connector",
    "license": "AGPL-3",
    "author": "Yigit Budak, Florent THOMAS (Mind And Go), Odoo Community Association (OCA)",
    "application": False,
    "installable": True,
    "external_dependencies": {"python": ["odoorpc", "lxml"], "bin": []},
    "depends": [
        "base",
        "product",
        "connector",
        "connector_base_product",
        "sale",
        "purchase",
        "product_dimension",
        "l10n_tr_address",
        "altinkaya_ecommerce",
    ],
    "data": [
        "data/cron.xml",
        "security/connector_odoo_base_security.xml",
        "security/ir.model.access.csv",
        "views/odoo_backend.xml",
        "wizards/import_external_id.xml",
        "wizards/wizards_menu.xml",
        "views/product_uom.xml",
        "views/odoo_connector_menus.xml",
        "views/product_category.xml",
        "views/product.xml",
        "views/product_template.xml",
        "views/partner.xml",
        "views/partner_category.xml",
        "views/users.xml",
        "views/account_account.xml",
        "views/ir_attachment.xml",
        "views/res_currency.xml",
        "views/purchase_order.xml",
        "views/stock_warehouse.xml",
        "views/stock_location.xml",
        "views/openerp_picking_type.xml",
        "views/stock_picking.xml",
        "views/stock_move.xml",
        "views/stock_inventory.xml",
        "views/sale_order.xml",
    ],
    "demo": [],
    "qweb": [],
}
