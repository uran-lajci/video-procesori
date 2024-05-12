import os
import shutil
import tempfile

from moviepy.editor import VideoFileClip, concatenate_videoclips


def save_clip(file, start_time, end_time, output_path):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmpfile:
        tmpfile.write(file.read())
        clip = VideoFileClip(tmpfile.name)

    subclip = clip.subclip(start_time, end_time)
    subclip.write_videofile(output_path, codec='libx264', audio_codec='aac')


def convert_time(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s


def merge_videos(clips, output_path):
    temp_dir = tempfile.mkdtemp()

    temp_paths = []
    for clip in clips:
        temp_path = os.path.join(temp_dir, clip.name)
        with open(temp_path, 'wb') as f:
            shutil.copyfileobj(clip, f)
        temp_paths.append(temp_path)

    video_clips = [VideoFileClip(temp_path) for temp_path in temp_paths]
    final_clip = concatenate_videoclips(video_clips)
    final_clip.write_videofile(output_path, codec="libx264")

    for clip in video_clips:
        clip.close()

    shutil.rmtree(temp_dir)
