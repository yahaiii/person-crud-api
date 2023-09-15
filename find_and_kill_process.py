import psutil

def find_process_by_port(port):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            connections = proc.connections()
            for conn in connections:
                if conn.laddr.port == port:
                    return proc.pid, proc.info['name']
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            pass
    return None, None

def kill_process_by_pid(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()
    except psutil.NoSuchProcess:
        pass

if __name__ == "__main__":
    port_to_check = 5000  # Replace with the port number you want to check
    pid, process_name = find_process_by_port(port_to_check)

    if pid is not None:
        print(f"Process with PID {pid} ({process_name}) is using port {port_to_check}.")
        print(f"Terminating the process...")
        kill_process_by_pid(pid)
    else:
        print(f"No process found using port {port_to_check}. Port is available.")
