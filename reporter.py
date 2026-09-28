def format_node_data(nodes):
    results = []
    for node_data in nodes["data"]:
        node = node_data["node"]
        cpu = node_data["cpu"]
        mem = node_data["mem"]
        maxmem = node_data["maxmem"]
        cpu_percentage = cpu * 100
        mem_percentage = mem / maxmem * 100
        mem_GB_conversion = mem / 1024**3
        maxmem_GB_conversion = maxmem / 1024**3
        formatted_string = f"{node}: CPU {cpu_percentage:.2f}%, RAM {mem_percentage:.2f}% ({mem_GB_conversion:.2f}GB / {maxmem_GB_conversion:.2f}GB)"
        results.append(formatted_string)
    return results


def format_resource_data(resources):
    results = []
    for data in resources["data"]:
        name = data["name"]
        vmid = data["vmid"]
        status = data["status"]
        cpu = data["cpu"]
        mem = data["mem"]
        maxmem = data["maxmem"]
        cpu_percentage = cpu * 100
        mem_percentage = mem / maxmem * 100
        mem_GB_conversion = mem / 1024**3
        maxmem_GB_conversion = maxmem / 1024**3
        formatted_string = f"{name}: ID: {vmid}, Status: {status}, CPU {cpu_percentage:.2f}%, RAM {mem_percentage:.2f}% ({mem_GB_conversion:.2f}GB / {maxmem_GB_conversion:.2f}GB)"
        results.append(formatted_string)
    return results
