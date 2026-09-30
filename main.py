from connector import ProxmoxConnector
from reporter import format_node_data, format_resource_data
from notifier import send_notification


def main():
    proxmox = ProxmoxConnector()
    nodes = proxmox.get("/nodes")
    vms = proxmox.get_resources(nodes, "qemu")
    lxcs = proxmox.get_resources(nodes, "lxc")

    report_lines = format_node_data(nodes)
    vm_lines = format_resource_data(vms)
    lxc_lines = format_resource_data(lxcs)
    all_lines = report_lines + vm_lines + lxc_lines
    payload = "\n".join(all_lines)
    send_notification(payload)

    for line in report_lines:
        print(line)

    for line in vm_lines:
        print(line)

    for line in lxc_lines:
        print(line)


if __name__ == "__main__":
    main()
