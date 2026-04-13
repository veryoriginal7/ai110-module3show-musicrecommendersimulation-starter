"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


# --- Normal user profiles ---
PROFILES = {
    "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.85,
        "tempo_bpm": 120,
        "valence": 0.85,
        "danceability": 0.80,
    },
    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.38,
        "tempo_bpm": 76,
        "acousticness": 0.80,
        "danceability": 0.55,
    },
    "Deep Intense Rock": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.92,
        "tempo_bpm": 150,
        "valence": 0.40,
        "acousticness": 0.08,
    },
}


# --- Adversarial / edge-case profiles ---
ADVERSARIAL_PROFILES = {
    # Conflict: energy and mood point at completely different songs.
    # Only one sad song exists (Empty Chairs, energy=0.48).
    # Does mood (+0.10) rescue it, or does energy bury it?
    "High-Energy Sad": {
        "genre": "soul",
        "mood": "sad",
        "energy": 0.92,
        "tempo_bpm": 150,
        "danceability": 0.85,
    },

    # Ghost genre: "bossa nova" is not in the catalog.
    # The +0.30 genre bonus never fires — pure numeric scoring only.
    # Exposes how far numeric features alone can carry a result.
    "Ghost Genre (Bossa Nova)": {
        "genre": "bossa nova",
        "mood": "romantic",
        "energy": 0.55,
        "tempo_bpm": 95,
        "valence": 0.75,
    },

    # Contradiction: no song in the catalog has both high energy AND
    # high acousticness. Forces the Gaussian to split its reward.
    # Which weight wins — energy (×0.20) or acousticness (×0.12)?
    "Contradictory Numerics (Loud Acoustic)": {
        "energy": 0.95,
        "acousticness": 0.95,
        "tempo_bpm": 155,
    },

    # Dead average: every feature sits at 0.5.
    # Tests whether the scoring produces meaningful spread or a flat cluster.
    "Dead Average": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.5,
        "tempo_bpm": 100,
        "valence": 0.5,
        "danceability": 0.5,
        "acousticness": 0.5,
    },

    # Categorical only: no numeric keys at all.
    # Max possible score is 0.30 (genre) + 0.10 (mood) = 0.40.
    # Everything below the top match should score identically at 0.0.
    "Categorical Only (No Numerics)": {
        "genre": "pop",
        "mood": "happy",
    },
}


def main() -> None:
    songs = load_songs("data/songs.csv")

    for label, profile_set in [("NORMAL PROFILES", PROFILES), ("ADVERSARIAL PROFILES", ADVERSARIAL_PROFILES)]:
        print(f"\n{'#'*50}")
        print(f"  {label}")
        print(f"{'#'*50}")

        for profile_name, user_prefs in profile_set.items():
            print(f"\n{'='*50}")
            print(f"Profile: {profile_name}")
            print(f"Prefs:   {user_prefs}")
            print(f"{'='*50}")

            recommendations = recommend_songs(user_prefs, songs, k=5)

            for song, score, explanation in recommendations:
                print(f"{song['title']} by {song['artist']} - Score: {score:.2f}")
                print(f"  Because: {explanation}")


if __name__ == "__main__":
    main()
