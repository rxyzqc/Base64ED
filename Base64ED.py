import dearpygui.dearpygui as dpg
import base64

dpg.create_context()
dpg.create_viewport(title='Base 64 ED', width=600, height=400)


def encode():
    input_text = dpg.get_value("Text to Encode Input")
    if input_text:
        encoded_text = base64.b64encode(input_text.encode("utf-8")).decode("utf-8")
        dpg.set_value("Encoded Text Output", encoded_text)


def decode():
    input_text = dpg.get_value("Text to Decode Input")
    if input_text:
        decoded_text = base64.b64decode(input_text.encode("utf-8")).decode("utf-8")
        dpg.set_value("Decoded Text Output", decoded_text)


with dpg.window(width=600, height=400):
    with dpg.group(horizontal=True):
        dpg.add_input_text(label="Text to Encode", tag="Text to Encode Input", width=300)
        dpg.add_button(label="Encode", callback=encode)

    with dpg.group(horizontal=True):
        dpg.add_input_text(label="Text to Decode", tag="Text to Decode Input", width=300)
        dpg.add_button(label="Decode", callback=decode)

    dpg.add_text(label="Encoded Text:", tag="Encoded Text Label")
    dpg.add_input_text(label="", tag="Encoded Text Output", readonly=True, multiline=True)
    dpg.add_text(label="Decoded Text:", tag="Decoded Text Label")
    dpg.add_input_text(label="", tag="Decoded Text Output", readonly=True, multiline=True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
