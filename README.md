# AnimeSearchEngine

AnimeSearchEngine is a prototype vertical search engine developed to provide a specialized search platform for anime-related content. It leverages ElasticSearch for powerful information retrieval capabilities, ensuring effective document indexing, ranking, and querying.

## Project Overview

This project was created to explore the implementation aspects of information retrieval systems, specifically focusing on the anime domain. It encompasses several key components:
- **Document Collection**: Data is sourced from Anime News Network via their public API.
- **Document Processing**: Extracted data is converted from XML to JSON format for easier manipulation and indexing.
- **Indexing and Ranking**: Uses ElasticSearch with customized ranking parameters to enhance search relevance.
- **Search Interface**: Provides a user-friendly interface for querying the search engine.

## Features

- **Customized Search Queries**: Supports complex query structures including one-word, multi-word, and partial match searches.
- **Ranking Algorithms**: Utilizes TF-IDF and BM25 algorithms for document ranking, with field weights adjusted for title, summary, genres, and themes.
- **Data Visualization and Management**: Integrated with Kibana for analytics and management of the search indices.

## Prerequisites

- Python 3.x
- ElasticSearch
- Flask (for the web interface)
- Access to the Anime News Network API

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/AnimeSearchEngine.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd AnimeSearchEngine
   ```

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Set up ElasticSearch**:
   - Ensure ElasticSearch is running on your system.
   - Configure the connection settings in your project configuration file.

## Running the Application

1. Start the Flask application:
   ```bash
   python app.py
   ```
2. Access the web interface at `http://localhost:5000` to start searching for anime content.

## How to Use

- **Search**: Enter your query in the search box and hit enter. The system supports various types of queries for flexibility.
- **View Details**: Click on the results to view more detailed information about each anime.

## Contributions

Contributions are welcome! Please fork the repository and submit pull requests with your suggested changes.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Contact Information

For further inquiries or issues, please contact us through our GitHub repository or email the project maintainers directly.

