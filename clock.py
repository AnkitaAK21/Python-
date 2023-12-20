import time
# importing time module to use the functions and classes of it.
# Explicitly here, we are using sleep function.
import winsound#to enable the sound in windows OS
def timer(sec): #User defined function "timer" to format the extracted time and display
    while sec:
        mins, secs = divmod(sec, 60) #divmod is the function that returns quotient and remainder.
        timeformat = '{:02d}:{:02d}'.format(mins,secs)#fomats the mins and secs in the format provided.
        print(timeformat,end='\r')# '\r' overwrites the statement
        time.sleep(1)#delays at the speed of 1 sec
        sec -= 1

    print("Oh Oh Time's Up!!")
    print("beep! beep! beep!...")


    

def set_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("It's now the right time!!")
            play_alarm_sound()# You can customize this function to play your preferred sound
            break
        time.sleep(1)

def play_alarm_sound():
    # For Windows users
    winsound.PlaySound("path/to/your/soundfile.wav", winsound.SND_FILENAME)

if __name__ == "__main__":
    while(True):
        print("CLOCK GENIE HERE!!\nYOUR WISH MASTER!")
        user_input = input("Enter wish:'Timer' for countdown timer, 'Alarm' for alarm clock -")
        if user_input == 'Timer':
            try:
        # Input the countdown time in seconds
                entered_time = int(input("Enter countdown time in seconds: "))
                timer(entered_time)#function call
            except ValueError: #error handling
                print("Entered input is not an integer\nplease give a valid intege!")
        elif user_input == 'Alarm':
            # Set the alarm time in 24-hour format (e.g., "07:00:00" for 7:00 AM)
            alarm_time = input("Enter the alarm time in 24-hour format (HH:MM:SS): ")
            set_alarm(alarm_time)
        else:
            exit()
