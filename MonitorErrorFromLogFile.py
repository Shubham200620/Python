import time

def monitor_log(file_path):
    with open(file_path,"r") as file:
        file.seek(0,2)
        print(f"Monitoring {file_path} for changes...")

        while True:
            line=file.readline()
            if line: #if there is a new line
                if "ERROR" or "error" or "Error" in line:
                    print("Alert!: Error occurred!")
                    print(line.strip())
            else:
                    time.sleep(1)

#call the function with the log file path
monitor_log("app.log")