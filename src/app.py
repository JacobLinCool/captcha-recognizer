import gradio as gr
import numpy as np
from preprocess import preprocess
from solve import solve


def run(img: np.ndarray) -> tuple[np.ndarray, str]:
    preprocessed = preprocess(img)

    solved = solve(preprocessed)

    return preprocessed, solved


app = gr.Interface(
    fn=run,
    inputs=[
        gr.Image(label="captcha image", shape=(108, 30)),
    ],
    outputs=[
        gr.Image(label="preprocessed", shape=(108, 30)),
        gr.Textbox(label="solved"),
    ],
    allow_flagging="never",
)

app.queue().launch()
