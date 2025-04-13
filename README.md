# Smart-Video-Summarizer

This project is a simple but powerful tool that automates transcription and summarization of video content. It extracts audio from a video file, transcribes it using OpenAI's Whisper, and summarizes the transcription using a Hugging Face transformer model.

## Features

- Extracts audio from video using ffmpeg
- Transcribes audio using Whisper (base model)
- Summarizes transcription using the distilBART model
- Outputs both the transcript and summary

## Why This Exists

Long videos often contain valuable insights, but going through them manually can be inefficient. This tool makes it easy to get the core message of any video in minutes. Ideal for lectures, interviews, meetings, and online tutorials.

## How It Works

1. **Audio Extraction**: Converts video to WAV audio using `ffmpeg`.
2. **Transcription**: Uses OpenAI Whisper to transcribe the audio.
3. **Summarization**: Uses Hugging Face's `distilbart-cnn-12-6` model to generate concise summaries.
4. **Output**: Saves the summary to `summary.txt` and prints it in the terminal.

## Example Usage

Edit the script and replace the `video_path` with your local file:

```python
video_path = r"path\\to\\your\\video.mp4"
summary = transcribe_and_summarize_video(video_path)

