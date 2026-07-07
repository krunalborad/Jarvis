import cv2
import os


video_path = 'video2.mp4'  
output_folder = 'frames2'  


if not os.path.exists(output_folder):
    os.makedirs(output_folder)


video = cv2.VideoCapture(video_path)


frame_count = 0

while True:
    
    success, frame = video.read()

    
    if not success:
        break

    
    frame_filename = f"{output_folder}/frame_{frame_count:04d}.jpg"  
    cv2.imwrite(frame_filename, frame)

    print(f"Saved {frame_filename}")

    
    frame_count += 1


video.release()

print(f"Extracted {frame_count} frames.")