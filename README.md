# AI-Powered Movie Recommendations

This project is an AI-based recommendation system that suggests movies to users based on their preferences. It uses machine learning and content-based filtering to generate recommendations.

## Features
- Recommend movies based on genres, ratings, and descriptions
- Content-based recommendation using TF-IDF
- Simple web interface via Flask

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-movie-recommender.git
   cd ai-movie-recommender
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Open the browser at `http://localhost:5000`

## Dataset

The project uses a sample `movies.csv` file that contains movie titles, genres, and descriptions.

## Example

Input: `"I liked Inception and Interstellar"`

Output: 
- "The Matrix"
- "Arrival"
- "Tenet"

## License

MIT License
