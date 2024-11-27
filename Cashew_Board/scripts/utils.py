import streamlit as st


def android_to_hex(color_code):
    hex_code = "#{:06x}".format(color_code & 0xffffff)
    return hex_code