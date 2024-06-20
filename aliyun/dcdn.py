from typing import List
from aliyunsdkdcdn.request.v20180115.BatchSetDcdnDomainCertificateRequest import BatchSetDcdnDomainCertificateRequest
from aliyunsdkcore.client import AcsClient


def do_update(client: AcsClient, domains: List[str], cert_name: str, cert_fullchain: str, cert_key: str):
    while len(domains) > 0:
        _domains = domains[:10]
        request = BatchSetDcdnDomainCertificateRequest()
        request.set_DomainName(','.join(_domains))
        request.set_accept_format('json')
        request.set_CertName(cert_name)
        request.set_SSLProtocol("on")
        request.set_CertType("upload")
        request.set_SSLPub(cert_fullchain)
        request.set_SSLPri(cert_key)
        client.do_action_with_exception(request)
        print("success update aliyun dcdn {} ssl cert {}".format(",".join(_domains), cert_name))
        domains = domains[10:]
    return True
