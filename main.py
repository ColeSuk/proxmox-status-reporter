from connector import ProxmoxConnector


def main():
    proxmox = ProxmoxConnector()
    version = proxmox.get("/version")
    print(version)


if __name__ == "__main__":
    main()
