from kivy.app import App
# from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_file("mycalc.kv")
# Set the App Window Size
Window.size = (500, 600)


class MyLayout(Widget):
	

	# create a function to input every number pressed into input box
	def button_press(self, i):
		# create variable that contains what earlier is in the input text box
		previous = self.ids.calc_input.text

		# check for "Error" in input text box
		if "Error" in previous or "=" in previous:
			previous = ""

		# determine if previous is "0"
		if previous == "0":
			self.ids.calc_input.text = ""
			self.ids.calc_input.text = f"{i}"

		else:
			self.ids.calc_input.text = f"{previous}{i}"

	# create a function to input every sign pressed into input box
	def math_sign(self, sign):
		previous = self.ids.calc_input.text

		if "=" in previous:
			previous = previous[1:]
		if previous[-1] == sign:
			self.ids.calc_input.text = f"{previous}{sign}"
		else:
			previous = eval(previous)
			previous = round(previous, 5)
		self.ids.calc_input.text = f"{previous}{sign}"

	# create a decimal function
	def dot(self):
		previous = self.ids.calc_input.text
		if "=" in previous:
			previous = previous[1:]

		# previous = 32.5+32
		if "+" in previous:
			num_list = previous.split("+")
		elif "-" in previous:
			num_list = previous.split("-")
		elif "*" in previous:
			num_list = previous.split("*")
		elif "/" in previous:
			num_list = previous.split("/")
		elif "%" in previous:
			num_list = previous.split("%")

		if ("+" in previous or "-" in previous or "*" in previous or "/" in previous or "%" in previous) and "." not in num_list[-1]:
			# add decimal point to the end
			previous = f"{previous}."
			self.ids.calc_input.text = previous
		elif "." in previous:
			pass
		else:
			previous = f"{previous}."
			self.ids.calc_input.text = previous

	# create a function to remove last character in input box
	def backspace(self):
		previous = self.ids.calc_input.text
		# removing last character from the input text box
		previous = previous[:-1]
		if previous == "":
			self.ids.calc_input.text = "0"
		else:
			self.ids.calc_input.text = previous

	# create a function to change positive num to negative num and vice versa
	def pos_neg(self):
		previous = self.ids.calc_input.text

		if "=" in previous:
			previous = previous[1:]
		# test for "-" sign in input text box
		if "-" in previous:
			self.ids.calc_input.text = f"{previous.replace('-', '')}"
		else:
			self.ids.calc_input.text = f"-{previous}"

	def equals(self):
		previous = self.ids.calc_input.text

		if "=" in previous:
			previous = previous[1:]
		
		# Error Handling
		try:
			answer = round(eval(previous), 5)
			self.ids.calc_input.text = "=" + str(answer)
		except:
			self.ids.calc_input.text = "Error"
	
	def percentage(self):
		previous = self.ids.calc_input.text
		if "=" in previous:
			previous = previous[1:]

		#print(previous)

		if "+" in previous:
			num_list = previous.split("+")
		elif "-" in previous:
			num_list = previous.split("-")
		elif "*" in previous:
			num_list = previous.split("*")
		elif "/" in previous:
			num_list = previous.split("/")
		else:
			num_list = previous

		#print(num_list)

		self.ids.calc_input.text = f"{previous}%"
		previous = self.ids.calc_input.text
		#print(previous)

		if "%" in previous and isinstance(num_list, list):
			previous = previous.replace("%", "/100")
			#print(previous)
			previous = eval(previous)
			self.ids.calc_input.text = "=" + str(previous)
		else:
			pass

	def clearbutton(self):
		self.ids.calc_input.text = "0"


class MyCalc(App):
	def build(self):
		return MyLayout()

if __name__ == "__main__":
	MyCalc().run()