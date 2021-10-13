from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder

import datetime
import time
import winsound

Builder.load_file("alarm.kv")


class MyLayout(Widget):

    def alarm_set(self, set_alarm_timer):
        while True:
            time.sleep(1)
            current_time = datetime.datetime.now()
            now = current_time.strftime("%H:%M:%S")
            date = current_time.strftime("%d/%m/%Y")
            # print("The Set Date is:",date)
            # print(now)
            # print(set_alarm_timer)
            if now == set_alarm_timer:
                print("Time to Wake up")
                winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
                break

    def set_alarm(self):
        try:
            hr = int(self.ids.hr_input.text)
            min = int(self.ids.min_input.text)
            sec = int(self.ids.sec_input.text)

            if hr > 23 or hr < 0:
                self.ids.update_label.text = "Error: Hours should be between 0 and 23"
                return
            elif min > 59 or min < 0:
                self.ids.update_label.text = "Error: Minutes should be between 0 and 59"
                return
            elif sec > 59 or sec < 0:
                self.ids.update_label.text = "Error: Seconds should be between 0 and 59"
                return

        except:
            self.ids.update_label.text = "Error: Invalid Input"
            return

        if hr in range(10):
            hr = f"0{hr}"
        if min in range(10):
            min = f"0{min}"
        if sec in range(10):
            sec = f"0{sec}"

        set_alarm_timer = f"{hr}:{min}:{sec}"
        # self.ids.update_label.text = f"Alarm Set to {hr}:{min}:{sec}"

        self.alarm_set(set_alarm_timer)


    def reset(self):
        self.ids.hr_input.text = ""
        self.ids.min_input.text = ""
        self.ids.sec_input.text = ""
        self.ids.update_label.text = "Enter Time in 24 Hr Format"

    def exitb(self):
        App.get_running_app().stop()
        Window.close()


class MyAlarm(App):
    def build(self):
        Window.size = (500, 300)
        return MyLayout()


if __name__ == "__main__":
    MyAlarm().run()
