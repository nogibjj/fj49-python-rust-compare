import time
import subprocess
import psutil

if __name__ == "__main__":
    start_time = time.time()

    # Execute your main script (replace 'script.py' with the actual script name)
    subprocess.run(['python', 'script.py'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Execution Time: {execution_time:.4f} seconds")

    # Measure CPU usage and memory consumption
    process = psutil.Process()
    cpu_usage = process.cpu_percent(interval=1)  # Measures CPU usage over a 1-second interval
    memory_info = process.memory_info().rss / (1024 ** 2)  # Memory usage in MB

    print(f"CPU Usage: {cpu_usage:.10f}%")
    print(f"Memory Consumption: {memory_info:.4f} MB")