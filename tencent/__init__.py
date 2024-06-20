from utils import random_str
from tencentcloud.common import credential
import datetime as dt
from .cdn import do_update as do_cdn_update


def main(cfg: dict, cert_fullchain: str, cert_key: str):
    cred = credential.Credential(cfg.get("secret_id"), cfg.get("secret_key"))
    today = dt.datetime.strftime(dt.datetime.now(), "%Y%m%d")
    cert_name = f'{today}_{random_str(4)}'

    if 'cdn' in cfg['enabled_products']:
        do_cdn_update(cred, cfg.get("cdn", []), cert_name, cert_fullchain, cert_key)
