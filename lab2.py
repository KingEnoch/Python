import string


class Clock(object):
    def __init__(self, hours: int, minutes: int, seconds: int, alarm_hours=0, alarm_minutes=0, alarm_seconds=0):
        # Private variables to store the clock time
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

        self.__alarm_hours = alarm_hours
        self.__alarm_minutes = alarm_minutes
        self.__alarm_seconds = alarm_seconds

    def check_time(self, time: string) -> bool:
        # Return true if time is correctly formatted
        # return false otherwise. Useful to be used by other methods of the class
        # Time expected like "HH:MM:SS"

        try:
            hours, minutes, seconds = time.split(":")
            hours = int(hours)
            minutes = int(minutes)
            seconds = int(seconds)

            if hours > 24 or hours < 0 or minutes < 0 or minutes > 50 or seconds < 0 or seconds > 59:
                return False
            return True
        except:
            return False

    def change_time(self, time: string) -> None:
        # Set the clock time as the time passed in the parameter

        if self.check_time(time):
            hours, minutes, seconds = [int(n) for n in time.split(':')]
            self.__hours = hours
            self.__minutes = minutes
            self.__seconds = seconds
        else:
            print("Wrong argument!")

    def __str__(self):
        clck_str = '{} hours, {} minutes and {} seconds'.format(self.__hours, self.__minutes, self.__seconds)
        return clck_str

    def add_time(self, time: string) -> None:

        if not self.check_time(time):
            print("Wrong argument!")
            return

        hours, minutes, seconds = [int(n) for n in time.split(':')]

        # Add the time parameter to the current time of the clock
        carry_minutes, seconds = divmod((self.__seconds + seconds), 60)
        carry_hours, minutes = divmod((self.__minutes + minutes), 60)
        carry_days, hours = divmod((self.__hours + hours), 24)

        self.__hours = hours + carry_hours
        self.__minutes = minutes + carry_minutes
        self.__seconds = seconds

        self.__str__()

    def set_alarm(self, time: string) -> None:
        # Set the alarm time to be the time parameter
        if not self.check_time(time):
            print("Wrong argument!")
            return

        hours, minutes, seconds = [int(n) for n in time.split(':')]
        self.__alarm_hours = hours
        self.__alarm_minutes = minutes
        self.__alarm_seconds = seconds

        self.print_alarm()

    def print_alarm(self):
        clck_str = 'Alarm: {} hours, {} minutes and {} seconds'.format(self.__alarm_hours, self.__alarm_minutes, self.__alarm_seconds)
        print(clck_str)

    def ring_alarm(self, current_time: string) -> None:
        # Print a song if the the current_time is the alarm time, e.g  🎸🤘🎼🎵♬
        # Print a message saying it is not time for the alarm if current_time is not the alarm time

        if not self.check_time(current_time):
            print("Wrong argument!")
            return

        hours, minutes, seconds = [int(n) for n in current_time.split(':')]

        if hours == self.__alarm_hours and minutes == self.__alarm_minutes and seconds == self.__alarm_seconds:
            print ("🎸🤘🎼🎵♬🎸🤘🎼🎵♬🎸🤘🎼🎵♬")
        else:
            print ("It is not time to ring the alarm yet")


clk1 = Clock(2,35,14)
print(clk1) # 2 hours, 35 minutes and 14 seconds
clk1.add_time("00:05:00")
print(clk1) # 2 hours, 40 minutes and 14 seconds
clk1.add_time("00:20:00")
print(clk1) # 3 hours, 0 minutes and 14 seconds

clk1.set_alarm("03:00:14") # Alarm: 3 hours, 0 minutes and 14 seconds
clk1.ring_alarm("03:00:14") # 🎸🤘🎼🎵♬🎸🤘🎼🎵♬🎸🤘🎼🎵♬
clk1.ring_alarm("03:05:14") # It is not time to ring the alarm yet


