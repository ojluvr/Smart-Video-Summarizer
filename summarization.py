import os
import ffmpeg
from faster_whisper import WhisperModel
from transformers import pipeline

def extract_audio_from_video(video_path, audio_path):
    try:
        ffmpeg.input(video_path).output(audio_path).run(overwrite_output=True)
        print(f"[✓] Audio extracted to: {audio_path}")
    except ffmpeg.Error as e:
        print(f"[!] Error extracting audio: {e}")
        return None
    return audio_path

def transcribe_audio(audio_path):
    print("[…] Transcribing audio...")
    model = WhisperModel("base", device="cpu", compute_type="int8")  # Use device="cuda" if you have a GPU

    segments, _ = model.transcribe(audio_path)
    full_text = " ".join([segment.text for segment in segments])
    print("[✓] Transcription completed.")
    return full_text

def summarize_text(text, max_chunk_length=500):
    summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")
    chunks = [text[i:i+max_chunk_length] for i in range(0, len(text), max_chunk_length)]
    summaries = []

    for i, chunk in enumerate(chunks):
        print(f"[Chunk {i+1}/{len(chunks)}] Summarizing...")
        summary = summarizer(chunk, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
        summaries.append(summary)

    return "\n\n".join(summaries)

def transcribe_and_summarize_video(video_path):
    audio_path = video_path.rsplit(".", 1)[0] + ".wav"

    extracted_audio = extract_audio_from_video(video_path, audio_path)
    if extracted_audio is None:
        return None

    transcription = transcribe_audio(extracted_audio)

    os.remove(extracted_audio)

    summary = summarize_text(transcription)

    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    print("[✓] Summary saved to summary.txt")
    return summary

video_path = r"c:\Users\ishit\Downloads\What Is AI_ _ Artificial Intelligence _ What is Artificial Intelligence_ _ AI In 5 Mins _Simplilearn.mp4"
summary = transcribe_and_summarize_video(video_path)

if summary:
    print("\n=== FINAL SUMMARY ===\n")
    print(summary)
else:
    print("[!] Failed to process the video.")
