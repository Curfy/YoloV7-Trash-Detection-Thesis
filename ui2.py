import tkinter
import customtkinter

# customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
	def __init__(self):
		super().__init__()

		# window
		self.title("Street Litter Detection using Object Detection and YoloV7 Algorithm")
		# self.resizable(False, False)
		self.minsize(width=1000, height=600)
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=1)
		
		# topbar
		self.tabmenu = customtkinter.CTkTabview(self, corner_radius=5)
		self.tabmenu.grid(row=0, column=0, sticky="nsew")
		self.tabmenu.add("Home")
		self.tabmenu.add("Settings")
		self.tabmenu.add("About")
		self.tabmenu.add("Manual")
		self.tabmenu.add("Summary Report")
		self.tabmenu.tab("Home").grid_columnconfigure((0,1), weight=1)
		self.tabmenu.tab("Home").grid_rowconfigure(0, weight=1)
		self.tabmenu.tab("Settings").grid_columnconfigure((0), weight=1)
		self.tabmenu.tab("Settings").grid_rowconfigure((0,1,2,3), weight=1)


		# video frame
		self.video_frame = customtkinter.CTkFrame(self.tabmenu.tab("Home"), width=700, corner_radius=2, border_width=1, border_color="gray")
		self.video_frame.grid(row=0, column=0, sticky="nsew")

		# sidebar frame
		self.sidebar_frame = customtkinter.CTkFrame(self.tabmenu.tab("Home"), corner_radius=0)
		self.sidebar_frame.grid(row=0, column=1, sticky="nsew")
		self.sidebar_frame.grid_rowconfigure((1,2,3,4), weight=1)
		self.sidebar_frame.grid_columnconfigure(0, weight=1)

		# object
		self.sidebar_object = customtkinter.CTkFrame(self.sidebar_frame)
		self.sidebar_object.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
		self.sidebar_object.grid_columnconfigure(0, weight=1)
		self.sidebar_object.grid_rowconfigure(0, weight=1)
		self.object_label = customtkinter.CTkLabel(self.sidebar_object, text="Object Detection", font=customtkinter.CTkFont(size=12, weight="normal"))
		self.object_label.grid(row=0, column=0, padx=20, pady=0)
		self.object_display = customtkinter.CTkLabel(self.sidebar_object, text="5 Objects", font=customtkinter.CTkFont(size=16, weight="bold"))
		self.object_display.grid(row=1, column=0, padx=20, pady=0)
		
		# identification
		self.sidebar_ident = customtkinter.CTkScrollableFrame(self.sidebar_frame, label_text="Identification")
		self.sidebar_ident.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
		self.sidebar_ident.grid_columnconfigure(0, weight=1)
		self.items = []
		for i in range(10):
				item = customtkinter.CTkLabel(master=self.sidebar_ident, text=f"Label {i}", font=customtkinter.CTkFont(size=14, weight="normal"))
				item.grid(row=i, column=0, padx=3, pady=0)
				self.items.append(item)
		
		# accuracy
		self.sidebar_accuracy = customtkinter.CTkFrame(self.sidebar_frame)
		self.sidebar_accuracy.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
		self.sidebar_accuracy.grid_columnconfigure(0, weight=1)
		self.sidebar_accuracy.grid_rowconfigure((1, 2), weight=1)
		self.accuracy_label = customtkinter.CTkLabel(self.sidebar_accuracy, text="Average Accuracy", font=customtkinter.CTkFont(size=12, weight="normal"))
		self.accuracy_label.grid(row=0, column=0, padx=20, pady=0)
		self.accuracy_display = customtkinter.CTkLabel(self.sidebar_accuracy, text="80%", font=customtkinter.CTkFont(size=20, weight="bold"))
		self.accuracy_display.grid(row=1, column=0, padx=20, pady=0)

		# classification
		self.sidebar_class = customtkinter.CTkFrame(self.sidebar_frame)
		self.sidebar_class.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
		self.sidebar_class.grid_columnconfigure(0, weight=1)
		self.sidebar_class.grid_rowconfigure((1, 2, 3), weight=1)
		self.class_label = customtkinter.CTkLabel(self.sidebar_class, text="Classification", font=customtkinter.CTkFont(size=12, weight="normal"))
		self.class_label.grid(row=0, column=0, padx=20, pady=0)
		self.class_display1 = customtkinter.CTkLabel(self.sidebar_class, text="3 Recyclable", font=customtkinter.CTkFont(size=20, weight="bold"))
		self.class_display1.grid(row=1, column=0, padx=20, pady=0)
		self.class_display2 = customtkinter.CTkLabel(self.sidebar_class, text="2 Non recyclable", font=customtkinter.CTkFont(size=20, weight="normal"))
		self.class_display2.grid(row=2, column=0, padx=20, pady=0)

		# settings view
		self.settings_detection = customtkinter.CTkFrame(self.tabmenu.tab("Settings"), corner_radius=5)
		self.settings_detection.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
		self.detection_label = customtkinter.CTkLabel(self.settings_detection, text="Object Detection Mode", font=customtkinter.CTkFont(size=12, weight="normal"))
		self.detection_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
		self.detection_switch = customtkinter.CTkSwitch(self.settings_detection, text="Automatic Detection")
		self.detection_switch.grid(row=1, column=0, padx=20, pady=10, sticky="w")
		# self.detection_note_label = customtkinter.CTkLabel(self.settings_detection, text="Note: Disabling automatic detection will disable time schedule detection", font=customtkinter.CTkFont(size=10, weight="normal"))
		# self.detection_note_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
		
		# Time Schedule
		# self.settings_time = customtkinter.CTkFrame(self.tabmenu.tab("Settings"), corner_radius=5)
		# self.settings_time.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
		# self.time_label = customtkinter.CTkLabel(self.settings_time, text="Time Schedule", font=customtkinter.CTkFont(size=12, weight="normal"))
		# self.time_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
		# self.timemenu = customtkinter.CTkOptionMenu(self.settings_time, dynamic_resizing=False,
    #                                                     values=["1:00", "2:00", "3:00", "4:00", "5:00", "6:00", "7:00", "8:00", "9:00", "10:00", "11:00", "12:00"])
		# self.timemenu.grid(row=1, column=0, padx=20, pady=10)
		# self.shiftmenu = customtkinter.CTkOptionMenu(self.settings_time, dynamic_resizing=False,
    #                                                     values=["AM", "PM"])
		# self.shiftmenu.grid(row=1, column=1, padx=20, pady=10)

		# Options
		self.settings_system = customtkinter.CTkFrame(self.tabmenu.tab("Settings"), corner_radius=5)
		self.settings_system.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
		self.camera_label = customtkinter.CTkLabel(self.settings_system, text="Camera Source", font=customtkinter.CTkFont(size=12, weight="normal"))
		self.camera_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
		self.camera_source_menu = customtkinter.CTkOptionMenu(self.settings_system, dynamic_resizing=False,
						 																								values=["Source1", "Source2", "Source3"])
		self.camera_source_menu.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="w")
		self.output_label = customtkinter.CTkLabel(self.settings_system, text="Output", font=customtkinter.CTkFont(size=12, weight="normal"))
		self.output_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
		self.source_path = tkinter.StringVar(self, "C://Documents/code/sourcepath")
		self.source_entry = customtkinter.CTkEntry(self.settings_system, textvariable=self.source_path, width=400)
		self.source_entry.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="w")
		self.source_button = customtkinter.CTkButton(self.settings_system, text="Select Source", height=30, command=self.select_source)
		self.source_button.grid(row=3, column=2, padx=20, pady=10, sticky="s")

		# Slider confidence
		self.settings_confidence = customtkinter.CTkFrame(self.tabmenu.tab("Settings"), corner_radius=5)
		self.settings_confidence.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
		self.confidence_level_label = customtkinter.CTkLabel(self.settings_confidence, text="1st-Confidence Level", font=customtkinter.CTkFont(size=12, weight="normal"))
		self.confidence_level_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

		self.slider_confidence_group = customtkinter.CTkFrame(self.settings_confidence, fg_color="transparent")
		self.slider_confidence_group.grid(row=1, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
		self.slider_label_frame = customtkinter.CTkFrame(self.slider_confidence_group, fg_color="transparent", width=500)
		self.slider_label_frame.grid(row=0, column=0, padx=20, pady=5, sticky="ew")
		self.slider_label_frame.columnconfigure((0,1,2,3,4), weight=1)
		self.slider_label_1 = customtkinter.CTkLabel(self.slider_label_frame, text="0", font=customtkinter.CTkFont(size=12, weight="normal"))
		self.slider_label_1.grid(row=0, column=0, padx=20, pady=0, sticky="w")
		self.slider_label_2 = customtkinter.CTkLabel(self.slider_label_frame, text="0.25", font=customtkinter.CTkFont(size=12, weight="normal"))
		self.slider_label_2.grid(row=0, column=1, padx=20, pady=0, sticky="w")
		self.slider_label_3 = customtkinter.CTkLabel(self.slider_label_frame, text="0.50", font=customtkinter.CTkFont(size=12, weight="normal"))
		self.slider_label_3.grid(row=0, column=2, padx=20, pady=0, sticky="nsew")
		self.slider_label_4 = customtkinter.CTkLabel(self.slider_label_frame, text="0.75", font=customtkinter.CTkFont(size=12, weight="normal"))
		self.slider_label_4.grid(row=0, column=3, padx=20, pady=0, sticky="e")
		self.slider_label_5 = customtkinter.CTkLabel(self.slider_label_frame, text="1", font=customtkinter.CTkFont(size=12, weight="normal"))
		self.slider_label_5.grid(row=0, column=4, padx=20, pady=0, sticky="e")

		self.slider_1 = customtkinter.CTkSlider(self.slider_confidence_group, from_=0, to=1, number_of_steps=4, width=500, command=self.slider_event)
		self.slider_1.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
		
		# self.radio_var = tkinter.IntVar(value=2)
		# self.label_radio_group = customtkinter.CTkLabel(self.settings_format, text="Display File Format:", font=customtkinter.CTkFont(size=12, weight="normal"))
		# self.label_radio_group.grid(row=0, column=0, padx=20, pady=10, sticky="w")
		# self.radio_button_1 = customtkinter.CTkRadioButton(self.settings_format, variable=self.radio_var, value=0, text="Video File")
		# self.radio_button_1.grid(row=1, column=0, pady=20, padx=10, sticky="n")
		# self.radio_button_2 = customtkinter.CTkRadioButton(self.settings_format, variable=self.radio_var, value=1, text="Image File")
		# self.radio_button_2.grid(row=1, column=1, pady=20, padx=10, sticky="n")
		# self.radio_button_3 = customtkinter.CTkRadioButton(self.settings_format, variable=self.radio_var, value=2, text="Live Video")
		# self.radio_button_3.grid(row=1, column=2, pady=20, padx=10, sticky="n")

		# Appearance
		self.settings_appearance = customtkinter.CTkFrame(self.tabmenu.tab("Settings"), corner_radius=5)
		self.settings_appearance.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
		self.appearance_mode_label = customtkinter.CTkLabel(self.settings_appearance, text="Appearance Mode:", font=customtkinter.CTkFont(size=12, weight="normal"))
		self.appearance_mode_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
		self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.settings_appearance, values=["Light", "Dark", "System"],
																		command=self.change_appearance_mode_event)
		self.appearance_mode_optionemenu.grid(row=2, column=0, padx=20, pady=10)
		self.scaling_label = customtkinter.CTkLabel(self.settings_appearance, text="Text Display Scaling:", font=customtkinter.CTkFont(size=12, weight="normal"))
		self.scaling_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")
		self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.settings_appearance, values=["80%", "90%", "100%", "110%", "120%"],
																command=self.change_scaling_event)
		self.scaling_optionemenu.grid(row=4, column=0, padx=20, pady=10)
	

		# self.button_group = customtkinter.CTkFrame(self.tabmenu.tab("Settings"), fg_color="transparent")
		# self.button_group.grid(row=3, column=1, padx=20, pady=10, sticky="nsew")
		self.save_button = customtkinter.CTkButton(self.tabmenu.tab("Settings"), text="Save", height=35, command=self.save)
		self.save_button.grid(row=3, column=1, padx=20, pady=10, sticky="s")
		self.run_button = customtkinter.CTkButton(self.tabmenu.tab("Settings"), text="Run", height=35, command=self.run)
		self.run_button.grid(row=2, column=1, padx=20, pady=10, sticky="s")

		# set default values
		self.detection_switch.select()
		# self.radio_button_3.select(1)
		self.camera_source_menu.set("Source1")
		# self.shiftmenu.set("PM")
		self.appearance_mode_optionemenu.set("System")
		self.scaling_optionemenu.set("100%")
		self.slider_1.set(0.5)

	def change_appearance_mode_event(self, new_appearance_mode: str):
		customtkinter.set_appearance_mode(new_appearance_mode)

	def change_scaling_event(self, new_scaling: str):
		new_scaling_float = int(new_scaling.replace("%", "")) / 100
		customtkinter.set_widget_scaling(new_scaling_float)

	def save(self):
		print("SAVED")

	def run(self):
		print("RUN")

	def slider_event(self, value):
		print("SLIDER", value)

	def select_source(self):
		print("SELECT SOURCE")

if __name__ == "__main__":
    app = App()
    app.mainloop()