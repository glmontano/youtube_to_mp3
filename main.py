from pytube import YouTube, exceptions # Used to stream YT
from pydub import AudioSegment # Used for audio conversion
from io import BytesIO # Used for memory storage

# Example: Lion King's 'Remember Who You Are'
YOUTUBE_URL = 'https://www.youtube.com/watch?v=FNBAmsriyY8'

try:
  # Stream and download audio
  yt = YouTube(YOUTUBE_URL)
  audio = yt.streams.filter(only_audio=True).first() # Stream audio
  audio_bytes = BytesIO() # Create 
  audio.stream_to_buffer(audio_bytes)
  audio_bytes.seek(0)

  # Convert audio to MP3 and write to given file
  sound = AudioSegment.from_file(file=audio_bytes).export(BytesIO(), 'mp3')
  with open('path/to/file', 'wb') as f:
    f.write(sound.getbuffer())
    
# Exception for inappropriate URL
except exceptions.RegexMatchError:
  print("Inappropriate URL")
  
  
