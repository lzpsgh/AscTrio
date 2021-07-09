function FindProxyForURL(url, host)
{
    url = url.toLowerCase();
    host = host.toLowerCase();
    return "PROXY 192.168.1.3:8080; DIRECT";
}