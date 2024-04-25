import cv2
import os
import dropbox
from twilio.rest import Client
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Replace 'your_twilio_account_sid' and 'your_twilio_auth_token' with your Twilio credentials
# account_sid = 'ACd9ec9e091bb4562a670c0e2d5741ac83'
# auth_token = 'dffda1157e9f03ae0bfd8f7e08fbe49b'

account_sid = 'ACd9ec9e091bb4562a670c0e2d5741ac83'
auth_token = '41f3b1eb53c2742602f4668411ecc3c7'

# Initialize the Twilio client
client = Client(account_sid, auth_token)
dropbox_access_token = 'slBz-32MJtfXRk6_AZ8tk1jOPTEAl3WTV6HCss4LGnYKHvNFpANNQJa-jtRXxNpcypiNp8uEWl8jixu8BQAAO-SjXIFyJ1yLGfLFwnWOEK_zMRKssNZfrFzD_pqQl_6pmWoZ5N1c8zf7jSgkwj7KxcLog'
# Function to initiate a voice call using Twilio
def initiate_voice_call():
    try:
        # Replace 'your_phone_number' with the recipient's phone number and '+1' with the appropriate country code
        call = client.calls.create(
            to='+917355578308',  # Recipient's phone number
            from_='+19136749959',  # Your Twilio phone number
            url='http://demo.twilio.com/docs/voice.xml'  # TwiML URL or call instructions
        )
        print(f"Voice call initiated successfully. Call SID: {call.sid}")
    except Exception as e:
        print(f"Error initiating voice call: {str(e)}")

# Function to send an SMS with a message
def send_sms_with_message():
    try:
        # Replace 'your_phone_number' with the recipient's phone number and '+1' with the appropriate country code
        message = client.messages.create(
            to='+917355578308',  # Recipient's phone number
            from_='+19136749959',  # Your Twilio phone number
            body='sPa-s MESSAGE NOTIFICATION : https://drive.google.com/drive/u/1/folders/1oQ5z-Pnlp9V0KKdi0wKIbvRJlFQ5vpwK',
            # SMS message body
        )
        print(f"SMS sent successfully. Message SID: {message.sid}")
    except Exception as e:
        print(f"Error sending SMS: {str(e)}")

# Checks and deletes the output file
# You can't have an existing file, or it will throw an error
FILE_OUTPUT = 'output.mp4'
if os.path.isfile(FILE_OUTPUT):
    os.remove(FILE_OUTPUT)

# Capture video from webcam
vid_capture = cv2.VideoCapture(0)
vid_cod = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(FILE_OUTPUT, vid_cod, 20.0, (640, 480))  # capture video into file....

while True:
    # Capture each frame of webcam video 
    ret, frame = vid_capture.read()
    cv2.imshow("My cam video", frame)
    output.write(frame)

    # Check if the camera just started recording and initiate a voice call and send an SMS
    if cv2.waitKey(1) & 0xFF == ord('x'):
        send_sms_with_message()  # Send SMS before or after the voice call
        initiate_voice_call()
        break

# Close the already opened camera
vid_capture.release()
# Close the already opened file
output.release()
# Close the window and de-allocate any associated memory usage
cv2.destroyAllWindows()


stored_output = cv2.VideoCapture(FILE_OUTPUT)
while stored_output.isOpened():
    ret, frame = stored_output.read()
    if not ret:
        break
    cv2.imshow('Recorded Video', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

stored_output.release()
cv2.destroyAllWindows()

# # Initialize Dropbox client
# dbx = dropbox.Dropbox(dropbox_access_token)

# # Shared folder link
# shared_folder_link = 'https://www.dropbox.com/scl/fo/uwe1hif3redm2u0c1dt8d/AK0Erdiqj_v2wM2RXt_BUfY?rlkey=vn8f93wwuaa8bva03und3l6fb&st=ljqb7qh6&dl=0'

# # Get folder metadata from shared link
# shared_link_metadata = dbx.sharing_get_shared_link_metadata(shared_folder_link)

# # Extract folder ID or path from metadata
# folder_path = shared_link_metadata.path_display

# # Path to the file you want to upload
# file_path = 'output.mp4'

# # Destination path for the upload
# destination_path = f"{folder_path}/output.mp4"

# # Upload the file to the specified folder
# with open(file_path, 'rb') as f:
#     dbx.files_upload(f.read(), destination_path)

# # Delete the local recorded video file
# os.remove(file_path)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
