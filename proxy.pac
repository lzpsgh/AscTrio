function FindProxyForURL(url, host)
{
    url = url.toLowerCase();
    host = host.toLowerCase();
    return "PROXY 192.168.8.162:8080; DIRECT";
}