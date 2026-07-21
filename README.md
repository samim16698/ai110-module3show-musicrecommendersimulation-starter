# 🎵 Music Recommender Simulation

## Step 4 Phase 1: Sample Outputs

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend


Answer: Each Song uses features like genre, mood, energy, tempo, danceability, keywords, and acousticness.
The UserProfile stores the user’s favorite genre, favorite mood, preferred energy level, preferred tempo, preferred danceability, favorite keywords, and likes.
The Recommender scores each song by comparing it to the user profile and adding points for matching genre, mood, energy, tempo, danceability, and keywords.
It recommends the songs with the highest scores, sorted from best to worst, and returns the top ones.

You can include a simple diagram or bullet list if helpful.

How the system works
What features does each Song use in your system

genre
mood
energy
tempo
danceability
keywords / descriptive tags
acousticness is also available in the song data
What information does your UserProfile store

favorite_genre
favorite_mood
energy_level
tempo
danceability
keywords
likes
How does your Recommender compute a score for each song

It compares each song to the user profile
Adds points for:
genre match
mood match
energy similarity
tempo similarity
danceability similarity
keyword or liked descriptor matches
Example scoring:
+2.0 for genre match
+1.0 for mood match
up to +1.0 for energy similarity
up to +1.0 for tempo similarity
up to +1.0 for danceability similarity
a small bonus for keywords
How do you choose which songs to recommend

Score every song in songs.csv
Sort songs by total score from highest to lowest
Return the top songs as recommendations

A possible bias is that the recommender may favor songs that match the user’s current preferences too strongly, which could reduce variety and make the system feel repetitive. 

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Here is a sample of the recommender output for the default pop/happy profile:

```text
Loaded songs: 20

Top recommendations:

1. Sunrise City
   Score: 4.98
   Reasons: matches preferred genre (+2.0), matches preferred mood (+2.0), energy proximity (+0.98)
   ----------------------------------------
2. Rooftop Lights
   Score: 2.96
   Reasons: matches preferred mood (+2.0), energy proximity (+0.96)
   ----------------------------------------
3. Midnight Mirage
   Score: 2.96
   Reasons: matches preferred genre (+2.0), energy proximity (+0.96)
   ----------------------------------------
4. Gym Hero
   Score: 2.87
   Reasons: matches preferred genre (+2.0), energy proximity (+0.87)
   ----------------------------------------
5. Broken Halo
   Score: 2.78
   Reasons: matches preferred genre (+2.0), energy proximity (+0.78)
   ----------------------------------------
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

### Edge-Case Profiles

```text
=== conflicting_profile ===
1. Gym Hero | Score: 2.97 | matches preferred genre (+2.0), energy proximity (+0.97)
2. Midnight Mirage | Score: 2.94 | matches preferred genre (+2.0), energy proximity (+0.94)
3. Sunrise City | Score: 2.92 | matches preferred genre (+2.0), energy proximity (+0.92)
4. Broken Halo | Score: 2.68 | matches preferred genre (+2.0), energy proximity (+0.68)
5. Storm Runner | Score: 0.99 | energy proximity (+0.99)
```

```text
=== extreme_energy_profile ===
1. Midnight Coding | Score: 4.42 | matches preferred genre (+2.0), matches preferred mood (+2.0), energy proximity (+0.42)
2. Library Rain | Score: 4.35 | matches preferred genre (+2.0), matches preferred mood (+2.0), energy proximity (+0.35)
3. Focus Flow | Score: 2.40 | matches preferred genre (+2.0), energy proximity (+0.40)
4. Spacewalk Thoughts | Score: 2.28 | matches preferred mood (+2.0), energy proximity (+0.28)
5. Gym Hero | Score: 0.93 | energy proximity (+0.93)
```

```text
=== unknown_genre_profile ===
1. Heartland Road | Score: 0.96 | energy proximity (+0.96)
2. Broken Halo | Score: 0.92 | energy proximity (+0.92)
3. Midnight Coding | Score: 0.92 | energy proximity (+0.92)
4. Focus Flow | Score: 0.90 | energy proximity (+0.90)
5. Glow in the Dark | Score: 0.90 | energy proximity (+0.90)
```

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


# Personal Reflection
What was your biggest learning moment during this project?
How did using AI tools help you, and when did you need to double-check them?
What surprised you about how simple algorithms can still "feel" like recommendations?
What would you try next if you extended this project?

- My biggest learning moment is how scoring systems are used in order rank reccomendatiosn for users. 
- AI tool helped to refactor the codes. 
- I was surprised how much work goes into something that looks simple from the outside. 
- I would try and give more importance to mood for reccomendations. 

