function FindProxyForURL(url, host) 
{ 
    if (shExpMatch( host, "192.168.*" )
    ||  shExpMatch( host, "127.*" )
    ||  shExpMatch( host, "localhost" )
    ||  shExpMatch( host, "*.iiit.ac.in" )
    ||  shExpMatch( host, "10.*" )
    ||  isPlainHostName( host )
    ||  dnsDomainIs( host, ".iiit.ac.in" )) {
        return "DIRECT"; 
    }
 
// You shouldn't need this, but in some cases it might be handy:
    if (isInNet(host, "10.0.0.0", "255.0.0.0")) {
        return "DIRECT"; 
    }
 
// This uses the Dan's Guardian port by default, squid if that isn't
// working, and direct if that isn't working.  On my network, i don't
// use DIRECT, because i block outgoing access in the firewall.
    return "PROXY proxy.iiit.ac.in:8080; DIRECT"; 
}
