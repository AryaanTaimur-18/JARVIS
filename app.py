from audio.recorder import AudioRecorder
from audio.transcriber import AudioTranscriber
from audio.speaker import Speaker


def main():

    recorder = AudioRecorder()

    transcriber = AudioTranscriber()

    speaker = Speaker()

    input("Press Enter to record...")

    audio_file = recorder.record(duration=5)

    print("\nTranscribing...\n")

    text = transcriber.transcribe(audio_file)

    print(f"You said: {text}")

    speaker.speak(text)


if __name__ == "__main__":
    main()