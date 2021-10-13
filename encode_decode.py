from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.config import Config
import base64


Builder.load_file("encode_decode.kv")


class MyLayout(Widget):

    def Encode(self, key, message):
        self.message = message
        self.key = key
        enc = []

        for i in range(len(self.message)):
            key_c = self.key[i % len(self.key)]
            enc.append(chr((ord(self.message[i]) + ord(key_c)) % 256))
        return base64.urlsafe_b64encode("".join(enc).encode()).decode()

    def Decode(self, key, message):
        self.message = message
        self.key = key
        dec = []
        self.message = base64.urlsafe_b64decode(self.message).decode()
        for i in range(len(self.message)):
            key_c = self.key[i % len(self.key)]
            dec.append(chr((256 + ord(self.message[i])- ord(key_c)) % 256))
        return "".join(dec)

    def result(self):
        if(self.ids.mode_input.text == 'e'):
            res = self.Encode(self.ids.key_input.text, self.ids.msg_input.text)
            self.ids.result_input.text = f"{res}"
        elif(self.ids.mode_input.text == 'd'):
            res = self.Decode(self.ids.key_input.text, self.ids.msg_input.text)
            self.ids.result_input.text = f"{res}"
        else:
            self.ids.result_input.text = "Invalid Mode"

    def reset(self):
        self.ids.msg_input.text = ""
        self.ids.key_input.text = ""
        self.ids.mode_input.text = ""
        self.ids.result_input.text = ""

    def exitb(self):
        App.get_running_app().stop()
        Window.close()


class MyMessage(App):
    def build(self):
        Config.set("graphics", "resizable", 0)
        Window.size = (500, 300)
        return MyLayout()


if __name__ == "__main__":
    MyMessage().run()
