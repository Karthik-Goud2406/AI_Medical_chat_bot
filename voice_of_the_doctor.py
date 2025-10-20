# #Step :1a Setup Text to Speech—TTS—model old  gTTS 

# from http import client
# import os
# import time 


# from gtts import gTTS
# import pygame

# def text_to_speech_with_gtts(input_text, output_filepath):

#         language="en"
        
#         audioobj=gTTS(
#             text=input_text,
#             lang=language,
#             slow=False    

#         )
        
#         audioobj.save(output_filepath) 


# input_text="hey im karthik Ai"

# #text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing.mp3")



# #Step :1b Setup Text to Speech—TTS—model with  & ElevenLabs

# import os
# import uuid
# from dotenv import load_dotenv
# from elevenlabs import VoiceSettings, save
# from elevenlabs.client import ElevenLabs

# load_dotenv()

# ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
# elevenlabs = ElevenLabs(api_key=ELEVENLABS_API_KEY)

# def text_to_speech_elevenlabs(text: str) -> str:
#     audio= elevenlabs.text_to_speech.convert(
#         voice_id="pNInz6obpgDQGcFmaJgB",  
#         output_format="mp3_22050_32",
#         text=text,
#         model_id="eleven_turbo_v2_5", 
        
#         # Simple voice settings with default values
#         voice_settings = VoiceSettings(),

#     )

#     #Save audio to a single file
#     save_file_path = "elevenlabs_testing.mp3"

#     with open(save_file_path, "wb") as f:
#      f.write(b''.join(filter(None, audio)))  # Combine all chunks and write

#     print(f"{save_file_path}: Audio file saved successfully!")
#     return save_file_path 


# # Example usage
# # if __name__ == "__main__":
    
# #  file_path = text_to_speech_file("Hello! This is a Karthik Ai doctor.")
# # print("Generated file:", file_path)


# #2B   Use Model for Text output to Voice

# import subprocess
# import platform

# #Step :2a Setup Text to Speech—TTS—model New  gTTS 

# import os
# import platform


# def text_to_speech_with_gtts(input_text, output_filepath):
#     language = "en"
    
#     audioobj = gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
    
#     audioobj.save(output_filepath)

#     #for autoplay
#     # Initialize pygame mixer
#     pygame.mixer.init()
#     pygame.mixer.music.load(output_filepath)
#     pygame.mixer.music.play()

#     # Wait until playback is finished
#     while pygame.mixer.music.get_busy():
#         time.sleep(0.5)

# input_text = "hey im karthik Ai auto play testing "
# #text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")





# #Step :2b Setup Text to Speech—TTS—model with  & ElevenLabs
# import os
# from dotenv import load_dotenv
# from elevenlabs import VoiceSettings, save
# from elevenlabs.client import ElevenLabs

# load_dotenv()

# ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
# elevenlabs = ElevenLabs(api_key=ELEVENLABS_API_KEY)

# def text_to_speech_elevenlabs(text: str) -> str:
#     audio= elevenlabs.text_to_speech.convert(
#         voice_id="pNInz6obpgDQGcFmaJgB",  
#         output_format="mp3_22050_32",
#         text=text,
#         model_id="eleven_turbo_v2_5", 
        
#         # Simple voice settings with default values
#         voice_settings = VoiceSettings(),

#     )

#     #Save audio to a single file
#     save_file_path = "elevenlabs_testing_autoplay.mp3"

#     with open(save_file_path, "wb") as f:
#      f.write(b''.join(filter(None, audio)))  # Combine all chunks and write
     
#      #for autoplay
#     # Initialize pygame mixer
#     pygame.mixer.init()
#     pygame.mixer.music.load(save_file_path)
#     pygame.mixer.music.play()

#     # Wait until playback is finished
#     while pygame.mixer.music.get_busy():
#         time.sleep(0.5)


#     print(f"{save_file_path}: Audio file saved successfully!")
#     return save_file_path 


#  # Example usage
# # if __name__ == "__main__":
    
# #   file_path = text_to_speech_elevenlabs("Hello! This is a Karthik Ai doctor autoplay.")
# # print("Generated file:", file_path)

# def text_to_speech_elevenlabs(input_text, output_filepath):
#     from elevenlabs import ElevenLabs, VoiceSettings
#     import os

#     client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

#     audio = client.text_to_speech.convert(
#         voice_id="pNInz6obpgDQGcFmaJgB",  # you can replace with your chosen voice
#         model_id="eleven_multilingual_v2",
#         text=input_text,
#         voice_settings=VoiceSettings(stability=0.5, similarity_boost=0.8)
#     )

#     with open(output_filepath, "wb") as f:
#         for chunk in audio:
#             f.write(chunk)

#     return output_filepath

# voice_of_the_doctor.py

import os
import time
from gtts import gTTS
import pygame
from dotenv import load_dotenv
from elevenlabs import ElevenLabs, VoiceSettings

# Load environment variables (for ElevenLabs API)
load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Create ElevenLabs client if key exists
elevenlabs_client = None
if ELEVENLABS_API_KEY:
    elevenlabs_client = ElevenLabs(api_key=ELEVENLABS_API_KEY)


# ✅ 1️⃣ Text-to-Speech using Google gTTS
def text_to_speech_with_gtts(input_text, output_filepath="outputs/gtts_output.mp3", autoplay=False):
    os.makedirs("outputs", exist_ok=True)
    language = "en"
    
    try:
        audioobj = gTTS(text=input_text, lang=language, slow=False)
        audioobj.save(output_filepath)
        print(f"[gTTS] Audio saved: {output_filepath}")

        if autoplay:
            pygame.mixer.init()
            pygame.mixer.music.load(output_filepath)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.5)

        return output_filepath

    except Exception as e:
        print(f"[gTTS] Error: {e}")
        return None


# ✅ 2️⃣ Text-to-Speech using ElevenLabs API
def text_to_speech_elevenlabs(input_text, output_filepath="outputs/elevenlabs_output.mp3", autoplay=False):
    if not elevenlabs_client:
        raise ValueError("ELEVENLABS_API_KEY not found. Please set it in your .env file.")

    os.makedirs("outputs", exist_ok=True)

    try:
        audio = elevenlabs_client.text_to_speech.convert(
            voice_id="pNInz6obpgDQGcFmaJgB",  # You can change this
            model_id="eleven_turbo_v2_5",
            text=input_text,
            voice_settings=VoiceSettings(stability=0.5, similarity_boost=0.8)
        )

        with open(output_filepath, "wb") as f:
            for chunk in audio:
                f.write(chunk)

        print(f"[ElevenLabs] Audio saved: {output_filepath}")

        if autoplay:
            pygame.mixer.init()
            pygame.mixer.music.load(output_filepath)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.5)

        return output_filepath

    except Exception as e:
        print(f"[ElevenLabs] Error: {e}")
        return None


# ✅ Example test (run this file directly)
if __name__ == "__main__":
    print("Testing both TTS models...\n")

    text1 = "Hello! This is Karthik AI Doctor using gTTS."
    text2 = "Hello! This is Karthik AI Doctor using ElevenLabs."

    print("🎤 Running gTTS test...")
    text_to_speech_with_gtts(text1, autoplay=True)

    print("\n🎙️ Running ElevenLabs test...")
    text_to_speech_elevenlabs(text2, autoplay=True)
