import shutil
import os
ffmpeg_path = shutil.which('ffmpeg')
ffprobe_path = shutil.which('ffprobe')
if ffmpeg_path and ffprobe_path:
    ffmpeg_dir = os.path.dirname(ffmpeg_path)
    ffprobe_dir = os.path.dirname(ffprobe_path)
    print(f"✅ ffmpeg available at: {ffmpeg_path}")
    print(f"✅ ffprobe available at: {ffprobe_path}")
else:
    print("ffmpeg or ffprobe not available")
    raise ImportError("ffmpeg or ffprobe is required to process YouTube videos. Install both in your system!")

print("\n=== PATH Analysis ===")
print(f"Current PATH: {os.environ.get('PATH', 'NOT SET')}")