import select
import sys
import pybonjour


timeout  = 5
resolved = []
_services = []


def resolve_callback(sdRef, flags, interfaceIndex, errorCode, fullname, hosttarget, port, txtRecord):
    if errorCode == pybonjour.kDNSServiceErr_NoError:
        _services.append({'fullname': fullname, 'hosttarget': hosttarget, 'port': port})


def browse_callback(sdRef, flags, interfaceIndex, errorCode, serviceName, regtype, replyDomain):
    if errorCode != pybonjour.kDNSServiceErr_NoError:
        return

    if not (flags & pybonjour.kDNSServiceFlagsAdd):
        print 'Service removed'
        return

    resolve_sdRef = pybonjour.DNSServiceResolve(0,
                                                interfaceIndex,
                                                serviceName,
                                                regtype,
                                                replyDomain,
                                                resolve_callback)
    
    try:
        while not resolved:
            ready = select.select([resolve_sdRef], [], [], timeout)
            if resolve_sdRef not in ready[0]:
                print 'Resolve timed out'
                break
            pybonjour.DNSServiceProcessResult(resolve_sdRef)
        else:
            resolved.pop()
    finally:
        resolve_sdRef.close()
    


def get_services(regtype):
    global _services
    _services = []
    
    browse_sdRef = pybonjour.DNSServiceBrowse(regtype=regtype, callBack=browse_callback)
    pybonjour.DNSServiceProcessResult(browse_sdRef)
    browse_sdRef.close()
    
    return _services
