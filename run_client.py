import argparse
from whisper_live.client import TranscriptionClient


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default="localhost", help="Server ip address")
    parser.add_argument('--port', type=str, default="59003", help="Server port")
    parser.add_argument('--lang', type=str, default="en", help="language")
    args = parser.parse_args()

    client = TranscriptionClient(
        host=args.host,
        port=args.port,
        lang=args.lang,
        translate=False,
        model="large-v2"
    )

    # client(audio="azure_chinese_YunyangNeural.mp3")
    # client(audio="azure_female_chat_resampled.wav")
    client()