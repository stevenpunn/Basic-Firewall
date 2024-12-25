# Create a simple firewall simulation
import random

# generate random ip to represent source IP Address
def generate_random_ip():
    return f"192.168.1.{random.randint(0, 20)}"

# checks if any of the random IP addresses match the rules set
def checkFirewallRules(ip, rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"

def main():
    firewallRules = {
        # define IP addresses for which we wish to block from our system
        "192.168.1.2": "block",
        "192.168.1.4": "block",
        "192.168.1.6": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block",     
    }

    # generate 12 random IP addresses and check against the rules set
    for _ in range(12):
        ip_address = generate_random_ip()
        action = checkFirewallRules(ip_address, firewallRules)
        randNum = random.randint(0, 9999)                # create a unique identifer for each IP and associated action
        print(f"IP: {ip_address}, Action: {action}, Random: {randNum}")

# create main guard to ensure main function runs once script is executed
if __name__ == "__main__":
    main()