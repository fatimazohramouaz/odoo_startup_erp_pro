# Startup ERP PRO - Odoo Module

This module is a Pro starter kit for a web & app development agency.

## Features
- Customers model (linked to res.partner)
- Projects model (linked optionally to Sale Orders)
- Tasks with progress computation
- Simple wizard to create invoices from project
- HR employee extension (github username flag)
- Demo data and placeholders for dashboard and reports

## Installation
1. Copy the folder `odoo_startup_erp_pro` to your Odoo addons directory.
2. Restart Odoo server.
3. Activate Developer Mode in Odoo, Update Apps List, search for "Startup ERP PRO" and install it.

## Notes
- After installing, configure your accounting (company, taxes) and sales settings.
- To auto-create projects from sales orders, add a server action that calls the helper method provided in `startup.sale.integration`.

If you want: I can also prepare a GitHub-ready repo structure and an install script for Ubuntu + Odoo 15/16.