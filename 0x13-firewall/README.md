# holberton-system_engineering-devops
## 0x13-firewall
### 0-firewall_ABC
This file contains the answers to these questions:

What is a firewall?
1. A hardware security system
2. A hardware or software security system
3. A software security system

What are the 2 types of firewall:
1. Soft and hard firewall
2. Incoming and outgoing firewall
3. Network and host-based firewall

What is the main function of a firewall?
1. To filter incoming and outgoing network traffic
2. To filter incoming and outgoing TCP traffic
3. To filter outgoing traffic 
### 1-block_all_incoming_traffic_but
This file contains the `ufw` commands used to install and setup the `ufw` firewall on my `web-01` server. It configures `ufw` so that it blocks all incoming traffic, except the following TCP ports: 
- `22` (SSH)
- `443`(HTTPS SSL)
- `80`(HTTP)
