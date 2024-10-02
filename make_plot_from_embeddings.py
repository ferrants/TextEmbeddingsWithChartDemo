import matplotlib.pyplot as plt

collection = [
    {
      "text": "it's really cold today, glad I have my warm jacket and some hot chocolate",
      "happy_scale": 5,
      "sad_scale": 3,
      "angry_scale": 0,
      "excited_scale": 3,
      "bored_scale": 2,
      "about_summer_scale": 0,
      "about_winter_scale": 10,
      "about_clothes_scale": 8,
      "about_food_scale": 7,
      "about_sports_scale": 0,
      "about_music_scale": 0,
      "about_movies_scale": 0,
      "about_books_scale": 0,
      "about_technology_scale": 0
    },
    {
      "text": "I'm so excited for the summer, I can't wait to go to the beach and have a picnic",
      "happy_scale": 9,
      "sad_scale": 0,
      "angry_scale": 0,
      "excited_scale": 10,
      "bored_scale": 0,
      "about_summer_scale": 10,
      "about_winter_scale": 0,
      "about_clothes_scale": 3,
      "about_food_scale": 5,
      "about_sports_scale": 5,
      "about_music_scale": 0,
      "about_movies_scale": 0,
      "about_books_scale": 0,
      "about_technology_scale": 0
    },
    {
      "text": "I love winter, it's so cozy and I get to wear my favorite sweaters",
      "happy_scale": 8,
      "sad_scale": 0,
      "angry_scale": 0,
      "excited_scale": 7,
      "bored_scale": 0,
      "about_summer_scale": 0,
      "about_winter_scale": 9,
      "about_clothes_scale": 9,
      "about_food_scale": 0,
      "about_sports_scale": 0,
      "about_music_scale": 0,
      "about_movies_scale": 0,
      "about_books_scale": 0,
      "about_technology_scale": 0
    },
    {
      "text": "I'm going to a concert this weekend, I can't wait to hear my favorite band",
      "happy_scale": 9,
      "sad_scale": 0,
      "angry_scale": 0,
      "excited_scale": 10,
      "bored_scale": 0,
      "about_summer_scale": 0,
      "about_winter_scale": 0,
      "about_clothes_scale": 2,
      "about_food_scale": 0,
      "about_sports_scale": 0,
      "about_music_scale": 10,
      "about_movies_scale": 0,
      "about_books_scale": 0,
      "about_technology_scale": 0
    },
    {
      "text": "I'm going to watch a movie tonight, I love watching movies",
      "happy_scale": 8,
      "sad_scale": 0,
      "angry_scale": 0,
      "excited_scale": 7,
      "bored_scale": 0,
      "about_summer_scale": 0,
      "about_winter_scale": 0,
      "about_clothes_scale": 2,
      "about_food_scale": 0,
      "about_sports_scale": 0,
      "about_music_scale": 0,
      "about_movies_scale": 10,
      "about_books_scale": 0,
      "about_technology_scale": 0
    },
    {
      "text": "I'm going to read a book tonight, I love reading books",
      "happy_scale": 7,
      "sad_scale": 0,
      "angry_scale": 0,
      "excited_scale": 6,
      "bored_scale": 2,
      "about_summer_scale": 0,
      "about_winter_scale": 0,
      "about_clothes_scale": 0,
      "about_food_scale": 0,
      "about_sports_scale": 0,
      "about_music_scale": 0,
      "about_movies_scale": 0,
      "about_books_scale": 10,
      "about_technology_scale": 0
    },
    {
      "text": "I'm going to play some video games tonight, I love playing video games",
      "happy_scale": 7,
      "sad_scale": 0,
      "angry_scale": 0,
      "excited_scale": 7,
      "bored_scale": 2,
      "about_summer_scale": 0,
      "about_winter_scale": 0,
      "about_clothes_scale": 0,
      "about_food_scale": 0,
      "about_sports_scale": 0,
      "about_music_scale": 0,
      "about_movies_scale": 0,
      "about_books_scale": 0,
      "about_technology_scale": 8
    },
    {
      "text": "I'm really tired from work today, I can't wait to relax and watch some TV",
      "happy_scale": 5,
      "sad_scale": 4,
      "angry_scale": 2,
      "excited_scale": 4,
      "bored_scale": 3,
      "about_summer_scale": 0,
      "about_winter_scale": 0,
      "about_clothes_scale": 0,
      "about_food_scale": 0,
      "about_sports_scale": 0,
      "about_music_scale": 0,
      "about_movies_scale": 7,
      "about_books_scale": 0,
      "about_technology_scale": 2
    },
    {
      "text": "I'm super excited about our new project at work, I can't wait to get started",
      "happy_scale": 8,
      "sad_scale": 0,
      "angry_scale": 0,
      "excited_scale": 9,
      "bored_scale": 0,
      "about_summer_scale": 0,
      "about_winter_scale": 0,
      "about_clothes_scale": 0,
      "about_food_scale": 0,
      "about_sports_scale": 0,
      "about_music_scale": 0,
      "about_movies_scale": 0,
      "about_books_scale": 0,
      "about_technology_scale": 7
    }
  ]

def main():
    measure_x = "happy_scale"
    measure_y = None
    measure_y = "about_clothes_scale"
    # Extract data from the collection
    texts = [item['text'] for item in collection]
    x_values = [item[measure_x] for item in collection]
    
    if measure_y:
        y_values = [item[measure_y] for item in collection]
        
        # Create a 2D scatter plot
        fig, ax = plt.subplots(figsize=(8, 6))
        scatter = ax.scatter(x_values, y_values, color='blue')
        
        # Add text labels
        for i, txt in enumerate(texts):
            ax.annotate(txt, (x_values[i], y_values[i]), xytext=(5, 5), 
                        textcoords='offset points', ha='left', va='bottom',
                        wrap=True, fontsize=8)
        
        # Set labels and title
        ax.set_xlabel(measure_x.replace("_", " ").capitalize())
        ax.set_ylabel(measure_y.replace("_", " ").capitalize())
        ax.set_title(f"Texts Plotted Based on {measure_x.replace('_', ' ').capitalize()} and {measure_y.replace('_', ' ').capitalize()}")
        
    else:
        # Create a 1D scatter plot (similar to the original)
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.set_xlim(0, 10)
        ax.set_ylim(-1, len(texts))
        
        # Plot the points
        ax.scatter(x_values, range(len(texts)), color='blue')
        
        # Add text labels
        for i, txt in enumerate(texts):
            ax.annotate(txt, (x_values[i], i), xytext=(5, 0), 
                        textcoords='offset points', ha='left', va='center',
                        wrap=True, fontsize=8)
        
        # Set labels and title
        ax.set_xlabel(measure_x.replace("_", " ").capitalize())
        ax.set_title(f"Texts Plotted Based on {measure_x.replace('_', ' ').capitalize()}")
        ax.set_yticks([])  # Remove y-axis ticks

    plt.tight_layout()
    # Save the plot to a file
    plt.savefig(f"{measure_x}_{measure_y if measure_y else 'single'}.jpg")


if __name__ == "__main__":
    main()
