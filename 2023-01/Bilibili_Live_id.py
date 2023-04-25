# Import the required Python library
import wmi

# Connect to the WMI namespace
c = wmi.WMI()

# Set the IP protocol stack to prefer IPv6
for interface in c.Win32_NetworkAdapterConfiguration():
    if interface.IPEnabled:
        interface.SetIPv6PreferredLifetime(0)
        interface.SetIPv6ValidLifetime(0)