# Initialize the VideoCapture object to read from the webcam.
camera_video = cv2.VideoCapture(0)
 
# Set width of the frames in the video stream.
camera_video.set(3, 1280)
 
# Set height of the frames in the video stream.
camera_video.set(4, 720)
 
# Initialize the VideoCapture object to read from the background video stored in the disk.
background_video = cv2.VideoCapture('media/backgroundvideos/1.mp4')
 
# Set the background video frame counter to zero.
background_frame_counter = 0
 
# Initialize a variable to store the time of the previous frame.
time1 = 0
 
# Iterate until the webcam is accessed successfully.
while camera_video.isOpened():
    
    # Read a frame.
    ok, frame = camera_video.read()
    
    # Check if frame is not read properly.
    if not ok:
        
        # Continue to the next iteration to read the next frame.
        continue
        
    # Read a frame from background video
    _, background_frame = background_video.read()
    
    # Increment the background video frame counter.
    background_frame_counter = background_frame_counter + 1
    
    # Check if the current frame is the last frame of the background video.
    if background_frame_counter == background_video.get(cv2.CAP_PROP_FRAME_COUNT):     
        
        # Set the current frame position to first frame to restart the video.
        background_video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        
        # Set the background video frame counter to zero.
        background_frame_counter = 0
 
    # Flip the frame horizontally for natural (selfie-view) visualization.
    frame = cv2.flip(frame, 1)
    
    # Change the background of the frame.
    output_frame,_ = modifyBackground(frame, background_image=background_frame, threshold=0.3,
                                      display=False, method='changeBackground')
    
    # Set the time for this frame to the current time.
    time2 = time()
    
    # Check if the difference between the previous and this frame time &gt; 0 to avoid division by zero.
    if (time2 - time1) &gt; 0:
    
        # Calculate the number of frames per second.
        frames_per_second = 1.0 / (time2 - time1)
        
        # Write the calculated number of frames per second on the frame. 
        cv2.putText(output_frame, 'fps: {}'.format(int(frames_per_second)), (10, 30),cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
    
    # Update the previous frame time to this frame time.
    # As this frame will become previous frame in next iteration.
    time1 = time2
    
    
    # Display the frame with changed background.
    cv2.imshow('Video', output_frame)
    
    # Wait until a key is pressed.
    # Retreive the ASCII code of the key pressed
    k = cv2.waitKey(1) &amp; 0xFF
    
    # Check if 'ESC' is pressed.
    if (k == 27):
        
        # Break the loop.
        break      
 
# Release the VideoCapture Object.
camera_video.release()
 
# Close the windows.
cv2.destroyAllWindows()
