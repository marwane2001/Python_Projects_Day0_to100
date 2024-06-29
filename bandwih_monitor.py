#Difficultty:Medium
#What is this project:This is a network bandwith monitor somewhat close to realtime 
###########################################################################
import time
import psutil

def get_network_usage(last_received, last_sent):
    bytes_received = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent

    new_received = bytes_received - last_received
    new_sent = bytes_sent - last_sent

    mb_new_received = new_received / 1024 / 1024
    mb_new_sent = new_sent / 1024 / 1024

    return bytes_received, bytes_sent, mb_new_received, mb_new_sent

def main():
    last_received = psutil.net_io_counters().bytes_recv
    last_sent = psutil.net_io_counters().bytes_sent

    print("Monitoring network bandwidth usage (Press Ctrl+C to stop)...")
    try:
        while True:
            bytes_received, bytes_sent, mb_new_received, mb_new_sent = get_network_usage(last_received, last_sent)

            print(f"{mb_new_received:.4f} MB received, {mb_new_sent:.4f} MB sent")

            last_received = bytes_received
            last_sent = bytes_sent

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    main()
