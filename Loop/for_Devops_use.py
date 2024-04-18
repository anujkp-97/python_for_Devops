
log_file=[
            "Info: Operation successful!",
            "Error: File not found",
            "Debug: Connection established",
            "Error: Database connection failed",
            "Error: Connection not established"
         ]
for line in log_file:
    if "Error" in line:
        print(line)
