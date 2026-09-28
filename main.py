from connector import ProxmoxConnector
from reporter import format_node_data, format_vm_data


def main():
    proxmox = ProxmoxConnector()
    nodes = proxmox.get("/nodes")
    vms = proxmox.get_vms(nodes)
    vm_lines = format_vm_data(vms)
    report_lines = format_node_data(nodes)

    for line in report_lines:
        print(line)

    for line in vm_lines:
        print(line)

    print(proxmox.get("/nodes/cerberus/lxc"))


if __name__ == "__main__":
    main()
