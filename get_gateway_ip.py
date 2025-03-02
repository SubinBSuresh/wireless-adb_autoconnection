import re

def get_wifi_gateway_ip(filename="conf.txt"):
    try:
        with open(filename, "r") as f:
            output_lines = f.readlines()

        wifi_adapter_found = False
        default_gateway_found = False
        gateway_ip = None

        for i, line in enumerate(output_lines):
            line = line.strip()

            if "Wireless LAN adapter Wi-Fi:" in line:
                wifi_adapter_found = True

            if wifi_adapter_found and "Default Gateway" in line:
                default_gateway_found = True
                if i + 1 < len(output_lines):
                    next_line = output_lines[i + 1].strip()
                    match = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", next_line)
                    if match:
                        gateway_ip = match.group(1)
                        break

        return gateway_ip

    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

wifi_gateway_ip = get_wifi_gateway_ip()

if wifi_gateway_ip:
    print(wifi_gateway_ip) #print only the ip address
else:
    print("Error") # print only error