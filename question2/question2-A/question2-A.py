from moviepy import editor
video=editor.VideoFileClip('queen.mp4')
video.audio.write_audiofile('queen.mp3')