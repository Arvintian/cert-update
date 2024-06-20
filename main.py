from aliyun import main as aliyun_main
from tencent import main as tencent_main
import yaml
import sys

USAGE = "Usage: main.py CONFIG_FILE_PATH"

if len(sys.argv) < 2:
    print(USAGE)
    sys.exit(-1)

CONFIG_FILE = sys.argv[1].strip()

with open(CONFIG_FILE, 'r', encoding="utf-8") as f:
    CONFIG: dict = yaml.safe_load(f)

CERT_FULLCHAIN = CERT_KEY = None
with open(f'{CONFIG["cert_path"]}/{CONFIG["cert_file_name"]}', 'r', encoding="utf-8") as f:
    CERT_FULLCHAIN = f.read()
with open(f'{CONFIG["cert_path"]}/{CONFIG["cert_key_file_name"]}', 'r', encoding="utf-8") as f:
    CERT_KEY = f.read()

if __name__ == '__main__':
    if CONFIG['aliyun']['enabled']:
        aliyun_main(CONFIG["aliyun"], CERT_FULLCHAIN, CERT_KEY)

    if CONFIG['tencent']['enabled']:
        tencent_main(CONFIG["tencent"], CERT_FULLCHAIN, CERT_KEY)
