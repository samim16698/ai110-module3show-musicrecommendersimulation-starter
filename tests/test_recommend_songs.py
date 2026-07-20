from src.recommender import recommend_songs


def test_recommend_songs_returns_ranked_matches():
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    songs = [
        {
            "id": 1,
            "title": "Pop Match",
            "artist": "Artist A",
            "genre": "pop",
            "mood": "happy",
            "energy": 0.85,
            "tempo_bpm": 120,
            "valence": 0.8,
            "danceability": 0.8,
            "acousticness": 0.2,
        },
        {
            "id": 2,
            "title": "Other Song",
            "artist": "Artist B",
            "genre": "jazz",
            "mood": "chill",
            "energy": 0.3,
            "tempo_bpm": 70,
            "valence": 0.4,
            "danceability": 0.5,
            "acousticness": 0.9,
        },
    ]

    results = recommend_songs(user_prefs, songs, k=1)

    assert len(results) == 1
    assert results[0][0]["title"] == "Pop Match"
