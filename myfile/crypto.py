import gradio as gr
import hashlib

def generate_md5_hash(input_value):

    if not isinstance(input_value, str):
        input_value = str(input_value)
    
    md5_hash = hashlib.md5()
    
    md5_hash.update(input_value.encode('utf-8'))
    
    return md5_hash.hexdigest()

def md5_interface(input_value):

    try:
        result = generate_md5_hash(input_value)
        return result
    except Exception as e:
        return f"An error occurred: {str(e)}"

iface = gr.Interface(
    fn=md5_interface,
    inputs=gr.Textbox(label="Enter Name or Number"),
    outputs=gr.Textbox(label="Your Result"),
    title="Chipering an Input",
    description="Give an input to the box below. And let magic happen!",
    theme="default"
)

if __name__ == "__main__":
    iface.launch(share=True)