"""Utilities for extracting video metadata using OpenCV."""

from pathlib import Path


def get_video_metadata(video_path):
    """Return resolution, FPS, frame count, and duration."""
    try:
        import cv2
    except ImportError as exc:
        raise ImportError(
            "Install OpenCV with: pip install opencv-python"
        ) from exc

    path = Path(video_path)

    if not path.is_file():
        raise FileNotFoundError(f"Video not found: {path}")

    capture = cv2.VideoCapture(str(path))

    if not capture.isOpened():
        capture.release()
        raise ValueError(f"Unable to open video: {path}")

    try:
        width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = capture.get(cv2.CAP_PROP_FPS)
        frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

        duration = frame_count / fps if fps > 0 else None

        return {
            "filename": path.name,
            "width": width,
            "height": height,
            "fps": round(fps, 2),
            "frame_count": frame_count,
            "duration_seconds": (
                round(duration, 2) if duration is not None else None
            ),
        }
    finally:
        capture.release()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Display video file metadata."
    )
    parser.add_argument("video", help="Path to the video file")
    args = parser.parse_args()

    metadata = get_video_metadata(args.video)

    for key, value in metadata.items():
        print(f"{key}: {value}")
