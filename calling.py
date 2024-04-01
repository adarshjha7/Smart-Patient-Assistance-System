import cv2
import os
from twilio.rest import Client

#THESE BELOW 2 LINES HAVE BEEN COMMENTED BECAUSE THEY WERE VIOLATING GITHUB'S RULES THAT WE CANT PUSH CONTENT WITH SECRET CREDEMTIALS OVER GITHUB,
#SO  KINDLY UNCOMMENT THEM 


# account_sid = 'ACd9ec9e091bb4562a670c0e2d5741ac83'
# auth_token = 'dffda1157e9f03ae0bfd8f7e08fbe49b'

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# Function to initiate a voice call using Twilio
def initiate_voice_call():
    try:
        # Replace 'your_phone_number' with the recipient's phone number and '+1' with the appropriate country code
        call = client.calls.create(
            to='+917355578308',  # Recipient's phone number
            from_='+19183763907',  # Your Twilio phone number
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
            from_='+19183763907',  # Your Twilio phone number
            body='S2AS2 MESSAGE NOTIFICATION : https://drive.google.com/drive/folders/19VPnbmldmFoj8jQyML9GTFqCrxqdqTz2?usp=sharing',  # SMS message body
            # media_url='https://drive.google.com/drive/folders/19VPnbmldmFoj8jQyML9GTFqCrxqdqTz2?usp=sharing'
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
