import http.client
import socket
import psutil
import subprocess
welcome_message = (" "
      f"""
\033[90m█░█░█ █ █▀▀ █ ▄▄ █░█ █▀▀ █░░ █▀█ █▀▀ █▀█
▀▄▀▄▀ █ █▀░ █ ░░ █▀█ ██▄ █▄▄ █▀▀ ██▄ █▀▄\033[0m"""
f"\033[92m\f           by: Rest-Ped\033[0m")

class active:
    def welcome(self):
        print(welcome_message)
    def list(self):
        net_info = NetworkMonitoring()
        net_type = net_info.getnetworkstaff()
        net_monitor = net_info.checkMonitoring()
        ip, port = self.mydata()
        print(f"\n\nMyData:\n ip: {ip}\n port: {port}\n NET-Type: {net_type}")
        print(f" NET-Monitor:")
        for key, value in net_monitor.items():
            print(f"  {key}: {value}")
    def mydata(self):
        try:
            temp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            temp_socket.bind(('', 0))
            port = temp_socket.getsockname()[1]
            temp_socket.close()

            self.conn = http.client.HTTPConnection("ifconfig.me")
            self.conn.request("GET", "/ip")
            resp = self.conn.getresponse()
            ip_read = resp.read()
            ip = ip_read.decode("UTF-8").strip()
            self.conn.close()
            return ip, port
        except Exception as e:
            print(f"ERROR: {type(e).__name__}: {e}")
            return"Не удалось получить все данные"
class NetworkMonitoring:
    def getnetworkstaff(self):
        try:
            interfaces = psutil.net_if_stats()
            for interface, stats in interfaces.items():
                if stats.isup:
                    if "WiFi" in interface or "wlan" in interface:
                        return "Wi-Fi"
                    elif "Ethernet" in interface or "eth" in interface:
                        return "Ethernet"
            return "No active connection"
        except Exception as e:
            return f"Error: {e}"
    def checkMonitoring(self):
        arp, DNS, port, traffic = self.checkingMonitoring() 
        data = {
            "ARP Monitoring": arp,
            "DNS Monitoring": DNS,
            "Open PORTS": port,
            "Traffic": traffic
        }
        return data
    def checkingMonitoring(self):
        try:
            import dns.resolver
            arp_check = subprocess.run(["arp", "-a"], capture_output=True, text=True)
            arp = "Normal" if "dynamic" in arp_check.stdout else "Suspicious"
            dns_check = dns.resolver.resolve("google.com", "A")
            DNS = "Normal" if dns_check else "Suspicious"
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                port_check = s.connect_ex(("127.0.0.1", 8080))
                port = "Monitoring possible" if port_check == 0 else "Normal"
            traffic_check = psutil.net_io_counters()
            if traffic_check.bytes_sent > 1000000 or traffic_check.bytes_recv > 1000000:
                traffic = "High Traffic - possible monitoring"
            else:
                traffic = "Normal"
            return traffic, DNS, arp, port
        except Exception as e:
            return f"Error: {e}"


def main():
    app = active()
    app.welcome()
    app.list()

    
if __name__ == "__main__":
    main()