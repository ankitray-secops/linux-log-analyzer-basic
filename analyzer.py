def analyze_log(file_path):
    failed_attempts = 0

    try:
        with open(file_path, "r") as file:
            for line in file:
                if "Failed password" in line:
                    failed_attempts += 1
    except FileNotFoundError:
        print("Log file not found.")
        return

    print(f"Total failed login attempts: {failed_attempts}")


if __name__ == "__main__":
    log_file = "auth.log"
    analyze_log(log_file)
