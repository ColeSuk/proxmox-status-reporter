from connector import ProxmoxConnector
from reporter import format_node_data, format_resource_data


def main():
    proxmox = ProxmoxConnector()
    nodes = proxmox.get("/nodes")
    vms = proxmox.get_resources(nodes, "qemu")
    lxcs = proxmox.get_resources(nodes, "lxc")

    report_lines = format_node_data(nodes)
    vm_lines = format_resource_data(vms)
    lxc_lines = format_resource_data(lxcs)

    for line in report_lines:
        print(line)

    for line in vm_lines:
        print(line)

    for line in lxc_lines:
        print(line)


if __name__ == "__main__":
    main()
