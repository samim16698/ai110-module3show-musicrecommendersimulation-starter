from src.recommender import load_songs, recommend_songs

songs = load_songs('data/songs.csv')
profiles = [
    ('conflicting_profile', {'genre': 'pop', 'mood': 'sad', 'energy': 0.9}),
    ('extreme_energy_profile', {'genre': 'lofi', 'mood': 'chill', 'energy': 1.0}),
    ('unknown_genre_profile', {'genre': 'classical', 'mood': 'calm', 'energy': 0.5}),
]

for name, prefs in profiles:
    print(f'\n=== {name} ===')
    results = recommend_songs(prefs, songs, k=5)
    for i, (song, score, explanation) in enumerate(results, 1):
        print(f'{i}. {song["title"]} | Score: {score:.2f} | {explanation}')
