from pydms_config_server import start_server,load_config

cfg=load_config('./pydms-config-server.json')
start_server(cfg)