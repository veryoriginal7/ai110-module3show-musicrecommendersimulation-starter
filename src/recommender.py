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
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Read songs.csv and return a list of dicts with numeric fields cast to float/int."""
    import csv
    songs = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)
    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Return a (score, reasons) tuple using categorical weights and Gaussian decay for numeric features."""
    import math
    score = 0.0
    reasons = []

    # --- Categorical scoring ---
    if 'genre' in user_prefs:
        if song.get('genre') == user_prefs['genre']:
            score += 0.30
            reasons.append("genre match (+0.30)")

    if 'mood' in user_prefs:
        if song.get('mood') == user_prefs['mood']:
            score += 0.10
            reasons.append("mood match (+0.10)")

    # --- Numeric scoring via Gaussian decay: exp(-(diff^2) / (2*sigma^2)) ---
    # sigma is tuned per feature: 0.2 for 0-1 features, 20.0 for tempo_bpm (~60-200)
    numeric_features = [
        ('energy',       0.20, 0.2),
        ('tempo_bpm',    0.15, 20.0),
        ('acousticness', 0.12, 0.2),
        ('valence',      0.08, 0.2),
        ('danceability', 0.05, 0.2),
    ]

    for feature, weight, sigma in numeric_features:
        if feature in user_prefs and feature in song:
            diff = user_prefs[feature] - song[feature]
            similarity = math.exp(-(diff ** 2) / (2 * sigma ** 2))
            feature_score = round(similarity * weight, 4)
            score += feature_score
            reasons.append(f"{feature} similarity (+{feature_score:.2f})")

    return round(score, 4), reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song, rank by score descending, and return the top k as (song, score, explanation) tuples."""
    # Step 1 & 2: score every song — most Pythonic with a list comprehension
    scored = [
        (song, *score_song(user_prefs, song))   # unpacks (score, reasons) inline
        for song in songs
    ]

    # Step 3: build final tuples with a joined explanation string, then rank
    # sorted() returns a NEW list; the original `scored` list is untouched.
    # (contrast with list.sort(), which sorts IN PLACE and returns None)
    ranked = sorted(
        ((song, score, ", ".join(reasons) if reasons else "general recommendation")
         for song, score, reasons in scored),
        key=lambda x: x[1],   # sort by score (index 1)
        reverse=True           # highest score first
    )

    # Step 4: slice the top k results
    return ranked[:k]
