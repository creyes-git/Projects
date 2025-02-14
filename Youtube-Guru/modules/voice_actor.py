from deepgram import DeepgramClient, SpeakOptions
import replicate
import os


deepgram_api_key = str(os.getenv("DEEPGRAM_API_KEY"))
replicate_api_key = str(os.getenv("REPLICATE_API_TOKEN"))


def deepgram_text_to_speech(text : str):
    """
    AVAILABLE ONLY IN ENGLISH!!!
    Converts the given text to speech and saves it to a specified file.

    This function uses the Deepgram API to synthesize speech from text.
    The audio is saved in the specified filename using the given model options.

    Args:
        text (str): The text to convert to speech.
        filename (str): The name of the file to save the synthesized audio.

    Raises:
        Exception: If an error occurs during the text-to-speech conversion process,
                   an exception is raised with a message about the error.
    """
    
    
    "model=aura-orpheus-en"
    
    
    try:
        deepgram = DeepgramClient(api_key = deepgram_api_key)

        options = SpeakOptions(model = "model=aura-orion-en")

        response = deepgram.speak.v("1").save(filename = "audio.mp3", source = {"text" : text}, options = options)

    except Exception as e:
        print(f"Exception: {e}")
        
        
def replicate_text_to_speech(filename : str, text : str, voice : str, prompt : str, temp : float):    
    """
    Converts the given text to speech and saves it to a specified file.

    This function uses the Replicate API to synthesize speech from text.
    The audio is saved in the specified filename using the given model options.

    Args:
        text (str): The text to convert to speech.
        filename (str): The name of the file to save the synthesized audio.
        voice (str): The voice to use for the synthesis. See the list of available voices below.
        prompt (str): The prompt to use for the synthesis.
        temp (float): The temperature of the synthesis.

    Raises:
        Exception: If an error occurs during the text-to-speech conversion process,
                   an exception is raised with a message about the error.

    Available voices:

    * Dexter (Middle-aged male US conversational voice)
    * Miles (Young male US African American conversational voice)
    * Briggs (Elderly male US Southern (Oklahoma) conversational voice)
    * Casper (Middle-aged male US narrative voice)
    * Mitch (Middle-aged male Australian narrative voice)
    """
    voices_list = ["Dexter (Middle-aged male US conversational voice)",
                   "Miles (Young male US African American conversational voice)",
                   "Briggs (Elderly male US Southern (Oklahoma) conversational voice)",
                   "Casper (Middle-aged male US narrative voice)",
                   "Mitch (Middle-aged male Australian narrative voice)"]
    
    response = replicate.run("playht/play-dialog",
                             input={
                                    "text": text,
                                    "voice": voice,
                                    "prompt": prompt,
                                    "prompt2": "",
                                    "voice_2": "None",
                                    "language": "english",
                                    "turnPrefix": "Voice 1:",
                                    "temperature": temp,
                                    "turnPrefix2": "Voice 2:",
                                    "voice_conditioning_seconds": 20,
                                    "voice_conditioning_seconds_2": 20
                                    })
    
    
    return response




