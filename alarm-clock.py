import time
import winsound

def set_alarm(alarm_time):
    while True:
        current_time = time.strftime('%H:%M:%S')
        
        if current_time == alarm_time:
            print("Time to wake up!")
            frequency = 2500  # Frequency of the beep sound (in Hz)
            duration = 1000   # Duration of the beep sound (in milliseconds)
            winsound.Beep(frequency, duration)
            break
        
        time.sleep(1)  # Wait for 1 second before checking the time again

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time in HH:MM:SS format: ")
    set_alarm(alarm_time)
