print("Please configure appropriately and then remove this line !"); exit();

# ===== Your specific configuration goes below / please adapt ========

# the HCP account id - trial accounts typically look like p[0-9]*trial
hcp_account_id='account'

# you only need to adapt this part of the URL if you are NOT ON TRIAL but e.g. on PROD
hcp_landscape_host='.hanatrial.ondemand.com'
# hcp_landscape_host='.hana.ondemand.com' # this is used on PROD

# optional network proxy, set if to be used, otherwise set to ''
proxy_url='http://proxy.phl.sap.corp:8080'
# proxy_url='http://proxy_host:proxy_port'

# the following values need to be taken from the IoT Cockpit
device_id='blah'
oauth_credentials_for_device='blah-blah'

message_type_id_From_device='blah-blah-blah'

# ===== nothing to be changed / configured below this line ===========
