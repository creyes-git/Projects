from deepgram import DeepgramClient, SpeakOptions
import replicate
import os


api_key = str(os.getenv("DEEPGRAM_API_KEY"))


def deepgram_text_to_speech(text : str, filename : str):
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

    try:
        deepgram = DeepgramClient(api_key = api_key)

        options = SpeakOptions(model = "model=aura-zeus-en")

        response = deepgram.speak.v("1").save(filename, text, options)
        
        print(response.to_json(indent=4))

    except Exception as e:
        print(f"Exception: {e}")