def check_ip(ip: str) -> bool:
    return ip.startswith('192.168.')

if __name__ == "__main__":
    test_ip = "192.168.1.0"
    print(f'Checking ip {test_ip}: {check_ip(test_ip)}')