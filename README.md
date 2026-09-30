# video-processor
A website that lets you upload videos and transcode them. The idea is to not focus on the looks of the UI but to build a functional full-stack application.

**Features:**
- Users can sign in/out using their Google account
- Users can upload videos while signed in
- Videos should be transcoded to multiple formats (e.g. 360p, 720p)
- Users can view a list of uploaded videos (signed in or not)
- Users can view individual videos (signed in or not)

**Architecture:**
- Cloud Storage will store the raw and processed videos uploaded by users.
- Pub/Sub will send messages to the video processing service.
- Cloud Run will host a non-public video processing service. After it transcodes videos, they will be uploaded to Cloud Storage.
- Cloud Firestore will store the metadata for the videos.
- Cloud Run will host a Next.js app, which will serve as the Video web client.
- The Next.js app will make API calls to Firebase Functions.
- Firebase Functions will fetch videos from Cloud Firestore and return them.

![image](https://github.com/LakshmiMaddipati/video-processing/assets/82107355/28eb945a-bcf0-44cf-bf94-172fc769f89b)



