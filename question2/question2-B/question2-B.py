import pytube
link='https://www.youtube.com/watch?v=1G-1_R2g5bU'
first_stream=pytube.YouTube(link).streams.get_highest_resolution()
first_stream.download(output_path='E:\Python\Assignment\Assignment 7\question2\question2-B',filename='Sia - Unstoppable.mp4')