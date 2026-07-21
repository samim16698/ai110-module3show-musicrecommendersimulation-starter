import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored_songs = []
        for song in self.songs:
            score, reasons = score_song(
                {
                    "genre": user.favorite_genre,
                    "mood": user.favorite_mood,
                    "energy": user.target_energy,
                },
                {
                    "genre": song.genre,
                    "mood": song.mood,
                    "energy": song.energy,
                },
            )
            scored_songs.append((song, score, reasons))

        ranked_songs = sorted(scored_songs, key=lambda item: item[1], reverse=True)
        return [song for song, _, _ in ranked_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        score, reasons = score_song(
            {
                "genre": user.favorite_genre,
                "mood": user.favorite_mood,
                "energy": user.target_energy,
            },
            {
                "genre": song.genre,
                "mood": song.mood,
                "energy": song.energy,
            },
        )
        return f"Score: {score:.2f}. " + "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of dictionaries."""
    songs: List[Dict] = []

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against user preferences and explain the result."""
    score = 0.0
    reasons: List[str] = []

    if song.get("genre") == user_prefs.get("genre"):
        score += 1.0
        reasons.append("matches preferred genre (+1.0)")

    if song.get("mood") == user_prefs.get("mood"):
        score += 2.0
        reasons.append("matches preferred mood (+2.0)")

    energy = song.get("energy", 0.0)
    target_energy = user_prefs.get("energy", 0.0)
    energy_diff = abs(energy - target_energy)
    energy_score = max(0.0, 1.0 - energy_diff)
    score += energy_score * 2.0
    reasons.append(f"energy proximity (+{energy_score * 2.0:.2f})")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top-k songs ranked by their compatibility score."""
    scored_songs = [
        (song, score, ", ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]

    return sorted(scored_songs, key=lambda item: item[1], reverse=True)[:k]
