# Mood Based Playlist API

This is a project that provides a simple API for recommending playlist based on a user's mood and a song limit. It also includes a frontend that provides easy interaction with the API which will allow users to fetch playlists, add songs, and explore available moods.

---

## Features

1. **Mood-Based Playlist Recommendation**

   - GET playlists based on the selected mood and a limit on the number of songs.

2. **Mood List**

   - GET a list of all available moods for selecting playlists.

3. **Add New Songs**

   - POST new songs to the database, including all the neccessary details like title, artist, album, mood, and duration.

4. **Frontend**
   - A HTML interface to interact with the API.

---

## Installation and Setup

1. **Install Python on your machine**

   - Download and install Python from [python.org](https://www.python.org/).
   - During installation, ensure you check the box for "Add Python to PATH." (If Applicable)

2. **Clone this repository**

   ````git clone https://github.com/aaryavbehl/mood-based-playlist-api.git
   cd mood-based-playlist-api/```

   ````

3. **Install Dependencies**
   `pip install -r requirements.txt`

4. **Run the API**
   `python app.py`

   - The server will start on http://127.0.0.1:5000.

5. **Open the Frontend**
   - Open your browser and go to the IP Address mentioned above.

---

## Basic API Endpoints

1. **Fetch Playlist**

   - URL: `/playlist`
   - Method: `GET`

   ### Query Parameters:

   - `mood`: Mood of the playlist (e.g., "happy", "sad").
   - `limit`: Maximum number of songs to fetch.

   #### Example Request done from Browser:

   `http://127.0.0.1:5000/playlist?mood=happy&limit=5`

   #### Response:

   ```{
        "songs": [
          {
            "title": "Song Title",
            "artist": "Artist Name",
            "album": "Album Name",
            "duration": "3:30",
          }
        ]
    }
   ```

2. **Fetch Moods**

   - URL: `/moods`
   - Method: `GET`

   #### Example Request done from Browser:

   `http://127.0.0.1:5000/moods`

   #### Response:

   ```{
        "moods": ["happy", "sad", "chill", "energetic"]
      }
   ```

3. **Add a New Song**

   - URL: `add_song`
   - Method: `POST`

   #### Payload (JSON)

   ```{
        "title": "Song Title",
        "artist": "Artist Name",
        "album": "Album Name",
        "mood": "mood",
        "duration": "3:30"
      }
   ```

   #### Example Request using cURL

   ```curl -X POST http://127.0.0.1:5000/add_song \
   -H "Content-type: application/json"
   -d '{
        "title": "Song Title",
        "artist": "Artist Name",
        "album": "Album Name",
        "mood": "mood",
        "duration": "3:30"
       }'
   ```
