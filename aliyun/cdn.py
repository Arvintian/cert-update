from typing import List
from aliyunsdkcdn.request.v20180510.BatchSetCdnDomainServerCertificateRequest import BatchSetCdnDomainServerCertificateRequest
from aliyunsdkcore.client import AcsClient


def do_update(client: AcsClient, domains: List[str], cert_name: str, cert_fullchain: str, cert_key: str):
    while len(domains) > 0:
        _domains = domains[:10]
        request = BatchSetCdnDomainServerCertificateRequest()
        request.set_DomainName(','.join(_domains))
        request.set_accept_format('json')
        request.set_CertName(cert_name)
        request.set_SSLProtocol("on")
        request.set_ForceSet("1")
        request.set_CertType("upload")
        request.set_SSLPub(cert_fullchain)
        request.set_SSLPri(cert_key)
        client.do_action_with_exception(request)
        print("success update aliyun cdn {} ssl cert {}".format(",".join(_domains), cert_name))
        domains = domains[10:]
    return True
