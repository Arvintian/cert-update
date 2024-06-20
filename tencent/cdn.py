from typing import List
from tencentcloud.common.credential import Credential
from tencentcloud.cdn.v20180606 import cdn_client
from tencentcloud.cdn.v20180606 import models as cdn_models
from tencentcloud.ssl.v20191205 import ssl_client
from tencentcloud.ssl.v20191205 import models as ssl_models
import time
import json


def do_update(cred: Credential, domains: List[str], cert_name: str, cert_fullchain: str, cert_key: str):
    certificate_id = upload_certificate(cred, cert_name, cert_fullchain, cert_key)
    client = cdn_client.CdnClient(cred, "")
    req = cdn_models.UpdateDomainConfigRequest()
    for domain in domains:
        params = {
            "Domain": domain,
            "Https": {
                "Switch": "on",
                "CertInfo": {
                    "CertId": certificate_id
                }
            }
        }
        req.from_json_string(json.dumps(params))
        client.UpdateDomainConfig(req)
        print("success update tencent cdn {} ssl cert {}".format(domain, cert_name))
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
