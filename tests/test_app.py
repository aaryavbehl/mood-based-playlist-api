import unittest
from app import app

class TestPlaylistAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_get_playlist(self):
        response = self.client.get('/playlist?mood=happy&limit=1')
        self.assertEqual(response.status_code, 200)

    def test_get_moods(self):
        response = self.client.get('/moods')

    def test_add_song(self):
        response = self.client.post('/add_song', json={
            "title": "New Song",
            "artist": "New Artist",
            "album": "New Album",
            "mood": "happy",
            "duration": "3:30"
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()