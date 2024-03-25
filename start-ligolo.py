import subprocess
import argparse


# arguments
parser = argparse.ArgumentParser(description='Python script to quick start Ligolo-NG tun interface')
parser.add_argument('username', help='choose username for tun interface')
parser.add_argument('cert_option', choices=['-selfcert', '-autocert'], help='choose certificate option')
args = parser.parse_args()

# create tun interface
create_tun = ['sudo', 'ip', 'tuntap', 'add', 'user', args.username, 'mode', 'tun', 'ligolo']
subprocess.run(create_tun, check=True)

# start interface
start_tun = ['sudo', 'ip', 'link', 'set', 'ligolo', 'up']
subprocess.run(start_tun, check=True)

# make ligolo proxy executable
proxy_exec = ['chmod', '+x', './proxy']
subprocess.run(proxy_exec, check=True)

# run proxy
start_proxy = ['./proxy', args.cert_option]
subprocess.run(start_proxy, check=True)
