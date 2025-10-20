#Voice Ui with Gradio 

import os

import gradio as gr

from brain_of_the_doctor import encode_image,analyse_the_image
from voice_of_the_patient import record_audio,transacribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts,text_to_speech_elevenlabs

System_prompt="""You are a medical expert with 15+ years experience in all fields of medicine. 
You will analyze the provided image (X-ray, MRI, pathology slide, or skin lesion) and answer ONLY relevant medical findings, diagnosis, or next steps. 
Do NOT provide unrelated or speculative information. 
Answer concisely, in this format:

[Findings]: <observations from image>
[Diagnosis / Likely Cause]: <short explanation>
[Next Step / Recommendation]: <tests, treatment, or advice if applicable>"""

def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = transacribe_with_groq(GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
                                                audio_filepath=audio_filepath,
                                                stt_model="whisper-large-v3-turbo")

    # Handle the image input
    if image_filepath:
        doctor_response = analyse_the_image(query=System_prompt+speech_to_text_output, encoded_image=encode_image(image_filepath), model="meta-llama/llama-4-scout-17b-16e-instruct")
    else:
        doctor_response = "No image provided for me to analyze"
    

    #voice_of_doctor = text_to_speech_elevenlabs(input_text=doctor_response, output_filepath="final.mp3")
    voice_of_doctor = text_to_speech_with_gtts(input_text=doctor_response, output_filepath="final.mp3")
    


    return speech_to_text_output, doctor_response, voice_of_doctor



# Create the interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
    gr.Textbox(label="Speech to Text"),
    gr.Textbox(label="Doctor's Response"),
    gr.Audio(label="Doctor's Voice")
],

    title="AI Doctor with Vision and Voice"
    
)

iface.launch(debug=True, share=True)

