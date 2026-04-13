# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 
Mid level energy users get the most songs from my algorithm.users who provide fewer numeric preference get a lower scoring ceiling. To fix this, one solution is to add more songs.
Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 
I used 8 profiles, high energy pop, chill lofi, deep intense rock, high energy sad, ghost genre(Bossa Nova), contradictory numerics(loud acoustic), dead average(all stats 0.5), categorical only. What suprise me was Empty chair was the number one song for High Energy Sad even though it had a terrible energy fit.

**Profiles tested:**

Three normal profiles were designed to match songs that clearly exist in the catalog: High-Energy Pop (pop, happy, energy 0.85), Chill Lofi (lofi, chill, energy 0.38), and Deep Intense Rock (rock, intense, energy 0.92). These confirmed the scoring rewarded obvious matches. Five adversarial profiles were then designed to stress-test the logic: High-Energy Sad (conflicting mood and energy), Ghost Genre (a genre not in the catalog), Contradictory Numerics (high energy and high acousticness at the same time), Dead Average (all features at 0.5), and Categorical Only (genre and mood with no numeric preferences at all).

**What was looked for:**

For normal profiles, the expectation was that the closest-matching song would rank first with a high score, and that scores would drop meaningfully for songs outside the genre. For adversarial profiles, the goal was to find places where the scoring produced results that felt wrong even though the math was technically correct.

**What was surprising:**

The most unexpected result came from the High-Energy Sad profile. The system recommended a quiet soul song (Empty Chairs, energy 0.48) as the top result for a user who asked for energy 0.92. It ranked first not because it sounded right, but because genre and mood labels gave it 0.40 points before energy was even calculated. High-energy songs the user would likely have preferred scored lower because they had no mood match. The system was following its own rules correctly, but the recommendation felt wrong.

The Categorical Only profile also revealed something unexpected: positions 3 through 5 all scored exactly 0.00 with the label "general recommendation." Once the genre and mood bonuses were exhausted, the system had no way to distinguish between the remaining 17 songs. In a real product those slots would be essentially random.

The Ghost Genre test (bossa nova) was a more reassuring surprise: even without a single genre match, the system still surfaced Golden Hour as a reasonable result because its energy, tempo, and valence were close to the user's preferences. The system degrades gracefully when the catalog does not contain the requested genre.

**Profile pair comparisons:**

*High-Energy Pop vs Chill Lofi* — These are opposite ends of the energy spectrum. High-Energy Pop pulled up-tempo, bright songs (Sunrise City 0.88, Gym Hero 0.73) while Chill Lofi pulled slow, acoustic-heavy songs (Library Rain 0.91, Midnight Coding 0.90). The swap makes sense: energy and tempo dominate the numeric scoring, so the two profiles push the Gaussian decay in completely opposite directions. No song appeared in both top-5 lists.

*High-Energy Pop vs Deep Intense Rock* — Both profiles want high energy (0.85 and 0.92), but they differ in genre and mood. Pop wanted happy songs; rock wanted intense ones. The overlap is Gym Hero, which ranked #2 for Pop and #2 for Rock — it is a pop song with intense energy, so it caught both. But Sunrise City (happy pop) ranked #1 for Pop and dropped off entirely for Rock, while Storm Runner (intense rock) ranked #1 for Rock and dropped off for Pop. This shows the genre and mood weights doing their job: same energy request, different catalog destinations.

*Deep Intense Rock vs High-Energy Sad* — Both profiles ask for high energy (~0.92), but Deep Intense Rock also matches genre and mood against songs that actually sound intense. High-Energy Sad asks for energy 0.92 but mood "sad," and only one sad song exists — the quiet Empty Chairs. The result is that High-Energy Sad's #1 pick (Empty Chairs, score 0.42) scored lower than Deep Intense Rock's #5 pick (Sunrise City, score 0.33 — wait, Storm Runner scored 0.94). The mood label dragged the sad profile toward a song that sounds nothing like what the energy preference implied.

*Ghost Genre (Bossa Nova) vs Categorical Only* — Both profiles fail to earn the full genre bonus, but for different reasons. Ghost Genre gets zero genre points because bossa nova is not in the catalog, yet it still produces a meaningful ranked list because numeric features (energy, tempo, valence) fill in the gap — top score was 0.53. Categorical Only specifies genre and mood but no numeric preferences, so after the first two matches the system has nothing left to differentiate songs — positions 3–5 all scored 0.00. Ghost Genre degrades gracefully; Categorical Only hits a hard floor.

*Dead Average vs Categorical Only* — Both profiles produce weak top scores compared to the normal profiles, but for opposite reasons. Dead Average (all features at 0.5) actually generates a spread of scores from 0.44 to 0.63 because the numeric features are all active and the Gaussian rewards songs close to the middle of the catalog. Categorical Only caps at 0.40 and then scores nothing. Dead Average is actually more informative to the user even though the preferences feel less specific, because having numeric values — even mediocre ones — gives the scoring more signal to work with.

*Chill Lofi vs Contradictory Numerics (Loud Acoustic)* — Both profiles include acousticness as a preference, but Chill Lofi pairs it with low energy (0.38) while Contradictory Numerics pairs it with very high energy (0.95). Chill Lofi found songs that genuinely fit both (Library Rain, acousticness 0.86, energy 0.35) and scored 0.91. Contradictory Numerics found no such song — the highest-scoring results were loud, low-acoustic songs like Storm Runner (0.34) that satisfied energy but not acousticness. The acoustic similarity column showed +0.00 for every top result, meaning the acousticness preference was effectively ignored by the catalog.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
