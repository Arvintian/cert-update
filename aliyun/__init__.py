from utils import random_str
from aliyunsdkcore.auth.credentials import AccessKeyCredential
from aliyunsdkcore.client import AcsClient
import datetime as dt
from .cdn import do_update as do_cdn_update
from .dcdn import do_update as do_dcdn_update


def main(cfg: dict, cert_fullchain: str, cert_key: str):
    client = AcsClient(credential=AccessKeyCredential(cfg.get('access_key'), cfg.get('access_token')))
    today = dt.datetime.strftime(dt.datetime.now(), "%Y%m%d")
    cert_name = f'{today}_{random_str(4)}'

    if 'cdn' in cfg['enabled_products']:
        do_cdn_update(client, cfg.get("cdn", []), cert_name, cert_fullchain, cert_key)

    if 'dcdn' in cfg['enabled_products']:
        do_dcdn_update(client, cfg.get("dcdn", []), cert_name, cert_fullchain, cert_key)
