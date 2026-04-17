# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Name: MusiRecreation
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

My recommender would put out a ranking of songs from first to last base on the user's profile, such as their favorite genres or mood
Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

The scoring mechanic of this recommention would range from 0-1, the closer to 1 the better. To get that number it would match stats such as genres, mood, energy, vibe and if those stats are within the preference of the user, more points would be added to the score.
Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

The dataset is just a list of songs (10 songs as for now), and each songs would have details like title, artist, genre, mood, energy, tempo_bpm, valence,danceability, and acousticness. Title, artist, genre, mood, and energy would be a description for them. Tempo_bpm, valence,danceability, and acousticness would be a number.
Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Overall I think the system work well, it has a basic equation uses to determine the score of each song. When I was testing it using 8 different profiles, I gives a pretty reasonable results, although the list of songs is very short with only 10 songs
Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 


Mid level energy users get the most songs from my algorithm.users who provide fewer numeric preference get a lower scoring ceiling. To fix this, one solution is to add more songs. Prompts:

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

 I used 8 profiles, high energy pop, chill lofi, deep intense rock, high energy sad, ghost genre(Bossa Nova), contradictory numerics(loud acoustic), dead average(all stats 0.5), categorical only. What suprise me was Empty chair was the number one song for High Energy Sad even though it had a terrible energy fit.

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  


I think to further improve the model, I would need more users and data to have more information to work with. Since content based filtering only recommend the user songs they already listen to, it means the users would have a limitation in term of discovery, I think that adding a mixture of Collaborative Filtering would be a nice way to expand what the user is listening to.

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Overall, I think this is a pretty fun project, since the concepts and abstractions are not too hard to understand, I can put all my effort into the implementation part of this. A recommender system is something that I already know fairly well because of my interest in computer science, so I didn't really learn anything new except the implementation for it.

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  



What was your biggest learning moment during this project?

My biggest learning moment for this project was having to use claud and copilot at the same time. For the task that required copilot I would use copilot and I would have to rewrite and filter the output and use it as the input for claud.

How did using AI tools help you, and when did you need to double-check them?

I used AI to make summarizes the code base and creates some skeleton code for me to implement them myself. The way that I double check the code is to use sanity check and run the code after every major changes.

What surprised you about how simple algorithms can still "feel" like recommendations?

It is not that suprising to me that a simple algorithms can feel like a recommendations mostly because I already know how it work.

What would you try next if you extended this project?

I would try to add more songs, maybe from some api or public dataset or even the youtube api. Then I would definitly change the algorithms to add Collaborative Filtering when I have enough user's data.