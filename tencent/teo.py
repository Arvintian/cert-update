from typing import List
from tencentcloud.common.credential import Credential
from tencentcloud.teo.v20220901 import teo_client
from tencentcloud.teo.v20220901 import models as teo_models
from tencentcloud.ssl.v20191205 import ssl_client
from tencentcloud.ssl.v20191205 import models as ssl_models
import time
import json


def do_update(cred: Credential, domains: List[dict], cert_name: str, cert_fullchain: str, cert_key: str):
    if not domains:
        return
    certificate_id = upload_certificate(cred, cert_name, cert_fullchain, cert_key)
    client = teo_client.TeoClient(cred, "")
    req = teo_models.ModifyHostsCertificateRequest()
    for item in domains:
        zone_id, domain = item.get("zone_id"), item.get("domain")
        params = {
            "ZoneId": zone_id,
            "Hosts": [domain],
            "Mode": "sslcert",
            "ServerCertInfo": [
                {
                    "CertId": certificate_id
                }
            ]
        }
        req.from_json_string(json.dumps(params))
        client.ModifyHostsCertificate(req)
        print("success update tencent teo {} ssl cert {}".format(domain, cert_name))
        time.sleep(1.5)


def upload_certificate(cred: Credential, cert_name: str, cert_fullchain: str, cert_key: str):
    client = ssl_client.SslClient(cred, "")
    request = ssl_models.UploadCertificateRequest()
    request.Alias = cert_name
    request.CertificateType = "SVR"
    request.CertificatePublicKey = cert_fullchain
    request.CertificatePrivateKey = cert_key
    response = client.UploadCertificate(request)
    return response.CertificateId
