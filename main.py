from connector import ProxmoxConnector
from reporter import format_node_data


def main():
    proxmox = ProxmoxConnector()
    nodes = proxmox.get("/nodes")
    report_lines = format_node_data(nodes)
    for line in report_lines:
        print(line)


if __name__ == "__main__":
    main()
