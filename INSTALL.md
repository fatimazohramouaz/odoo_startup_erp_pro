# Quick Install (Ubuntu example)

# 1) Install system dependencies
sudo apt update && sudo apt install -y git python3-pip python3-dev libxml2-dev libxslt1-dev libsasl2-dev libldap2-dev build-essential

# 2) Create user and folders
sudo adduser --system --home=/opt/odoo --group odoo
sudo mkdir /var/log/odoo

# 3) Clone Odoo (example for v16)
# git clone --depth 1 --branch 16.0 https://github.com/odoo/odoo.git /opt/odoo/odoo

# 4) Place this module into Odoo addons and restart Odoo
# cp -r odoo_startup_erp_pro /opt/odoo/addons/
# sudo systemctl restart odoo

# 5) In Odoo: Activate Developer Mode -> Update Apps List -> Install 'Startup ERP PRO'