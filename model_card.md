# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: Perfectpick

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

--- The reccomender is designed for music listeners who want to find music that is best suited to their taste and preference
- It makes assumptions of what users like based on the energy/genre/preference they like. 
- This is for real users.

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---
- The reccomender looks at a song's genre, mood and energy. 
- For each user, the reccomender looks at the user's most listened to genre, mood and energy and then reccomends songs that fit those prefenrences.
- The model turns this into a score by giving points when a song matches the user's preferences. The more it fits the user's criteria for example, same genre or mood as the user's preference, it gains points. The higher the scoring og the song, the more likely it is to be reccomended to the user.
- I changed the original starter logic by making energy matter moree and make genre matter less, so the user is reccomended different types of genres. 

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

--- There are 20 songs in the catalog. 
- Some genres include: pop, rock, jazz and then some moods include: relaxed, intense, happy.
- I added ten more songs. 
- No, the music dataset is very diverse and includes many different genres. 

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

--- It gave reasonable results for users who like pop genre. 
- The scoring captures pop users' preferences and reccomendations very fairly.

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

- Sometimes the model can put too much importance on energy and mostly reccomend pop songs. 
- Pop is overrepresented and other genres like rock are not represented enough. 
- The system overfits to pop preferences. 
- The system overly favors pop listeners. It always has pop as reccomendations but not so much reccomendations for other genres. 

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

--- Yes, the reccomender behaved as expected. I looked for whether the energy and mood was matching for a user's preferences and it did. I was not suprised by the results at all. 

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

--- I think I would make genre more important because pop is overreperesented in the model. The diversity would be massively improved if genre is given more importance and would handle complex user taste better. 

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

- I learned how systems reccomend music - I did not know that a scoring system was used for reccomendatons. 
- I understand now how much data research/coding is involved behind reccomenders. 