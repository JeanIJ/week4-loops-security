ip_addresses = [
    "192.168.1.25",
    "10.0.0.8",
    "172.16.5.14",
    "8.8.8.8",
    "172.15.3.2"
]

internal_count = 0
external_count = 0
internal_ips = []
external_ips = []

for ip in ip_addresses:
    if ip.startswith("192.168."):
        zone = "Private (Class C)"
        internal_count += 1
        internal_ips.append(ip)
    elif ip.startswith("10."):
        zone = "Private (Class A)"
        internal_count += 1
        internal_ips.append(ip)
    elif ip.startswith("172.16.") or ip.startswith("172.17.") or ip.startswith("172.31."):
        zone = "Private (Class B)"
        internal_count += 1
        internal_ips.append(ip)
    else:
        zone = "Public"
        external_count += 1
        external_ips.append(ip)
    
    print(f"{ip} -> {zone}")

print(f"Total Internal: {internal_count}")
print(f"Total External: {external_count}")
print(f"Internal IPs: {internal_ips}")
print(f"External IPs: {external_ips}")

while True:
    user_input = input("Enter an IP (or 'done' to finish): ").strip()
    
    if user_input.lower() == 'done':
        break
    
    if user_input.startswith(("192.168.", "10.")):
        print(f"{user_input} is internal.")
    elif user_input.startswith("172.16.") or user_input.startswith("172.17.") or user_input.startswith("172.31."):
        print(f"{user_input} is internal.")
    else:
        print(f"{user_input} is external.")