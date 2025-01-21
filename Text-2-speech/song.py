import os
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import yt_dlp

# Function to download a song from YouTube
def download_song(url, output_file):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_file,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Function to generate a song using new lyrics and the instrumental of the original song
def generate_song_from_web(lyrics, song_url, output_file):
    # Step 1: Download the song from YouTube
    original_song_file = "original_song.mp3"
    download_song(song_url, original_song_file)

    # Step 2: Use spleeter to separate vocals and instrumental (assuming spleeter is installed)
    os.system(f"spleeter separate -i {original_song_file} -o output/")

    # Step 3: Convert lyrics to speech
    tts = gTTS(lyrics, lang='en')
    speech_file = "speech.mp3"
    tts.save(speech_file)

    # Step 4: Load the instrumental version and the speech file
    instrumental = AudioSegment.from_file("output/original_song/accompaniment.wav")
    speech = AudioSegment.from_mp3(speech_file)

    # Step 5: Adjust volumes and overlay speech on instrumental
    speech = speech + 6  # Increase speech volume
    instrumental = instrumental - 6  # Decrease instrumental volume
    combined = instrumental.overlay(speech, position=0)

    # Step 6: Export the final song
    combined.export(output_file, format='mp3')

    # Optional: Play the final audio
    play(combined)

    # Cleanup
    os.remove(speech_file)
    os.remove(original_song_file)

# Example usage
lyrics = "These are the new lyrics to be sung."
song_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with your song URL
output_file = "final_song.mp3"

generate_song_from_web(lyrics, song_url, output_file)
