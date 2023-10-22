import time
import subprocess
import psutil

if __name__ == "__main__":
    start_time = time.time()

    # Execute your main script (replace 'script.py' with the actual script name)
    result = subprocess.run(['python', 'script.py'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)

    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds

    print ("Performance of python script file:")
    print(f"Execution Time: {execution_time:.2f} ms")

    # Measure CPU usage and memory consumption
    process = psutil.Process()
    cpu_usage = process.cpu_percent(interval=1)  # Measures CPU usage over a 1-second interval
    memory_info = process.memory_info().rss / (1024 ** 2)  # Memory usage in MB

    print(f"Memory Consumption: {memory_info:.2f} MB")

    print ("---------- END ---------")
