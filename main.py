from connector import ProxmoxConnector


def main():
    proxmox = ProxmoxConnector()
    nodes = proxmox.get("/nodes")
    print(nodes)


if __name__ == "__main__":
    main()
