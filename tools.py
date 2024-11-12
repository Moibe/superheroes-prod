import gradio as gr
import random

def theme_selector():

    temas_posibles = [
        gr.themes.Base(),
        gr.themes.Default(),
        gr.themes.Glass(),
        gr.themes.Monochrome(),
        gr.themes.Soft()
    ]

    return random.choice(temas_posibles)
