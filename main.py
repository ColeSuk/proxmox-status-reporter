from connector import ProxmoxConnector
from reporter import format_lxc_data, format_node_data, format_vm_data


def main():
    proxmox = ProxmoxConnector()
    nodes = proxmox.get("/nodes")
    vms = proxmox.get_vms(nodes)
    lxcs = proxmox.get_lxcs(nodes)

    report_lines = format_node_data(nodes)
    vm_lines = format_vm_data(vms)
    lxc_lines = format_lxc_data(lxcs)
    for line in report_lines:
        print(line)

    for line in vm_lines:
        print(line)

    for line in lxc_lines:
        print(line)


if __name__ == "__main__":
    main()
