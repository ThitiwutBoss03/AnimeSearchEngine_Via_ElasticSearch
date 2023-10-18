import requests
import xml.etree.ElementTree as ET
import json

def search_anime(animeID):
    api_url = f"https://cdn.animenewsnetwork.com/encyclopedia/api.xml?anime={animeID}"

    response = requests.get(api_url)
    if response.status_code == 200:
        xml_data = response.text
        root = ET.fromstring(xml_data)

        # Initialize variables with default values
        title = None
        plot_summary = None
        genres = []
        themes = []

        # Extract data (title, plot summary, genres, themes)
        title_element = root.find(".//info[@type='Main title']")
        if title_element is not None:
            title = title_element.text

        plot_summary_element = root.find(".//info[@type='Plot Summary']")
        if plot_summary_element is not None:
            plot_summary = plot_summary_element.text

        genre_elements = root.findall(".//info[@type='Genres']")
        genres = [genre.text for genre in genre_elements]

        theme_elements = root.findall(".//info[@type='Themes']")
        themes = [theme.text for theme in theme_elements]

        # Check if at least the title and plot summary have values
        if title is not None and plot_summary is not None:
            # Create a JSON object
            anime_data = {
                "animeID": animeID,
                "title": title,
                "plot_summary": plot_summary,
                "genres": genres,
                "themes": themes
            }

            return json.dumps(anime_data, separators=(',', ':'))  # NDJSON format

    return None

def main():
    output_path = r"C:\Users\Thitiwut\Documents\GitHub\AnimeSearchEngine_Via_ElasticSearch\Web app\elastic_code\anime_data.json"

    with open(output_path, 'w') as json_file:
        for animeID in range(1, 1000):
            anime_data = search_anime(animeID)
            if anime_data:
                json_file.write(anime_data + '\n')  # Add a newline after each JSON object
                print(f"Processed animeID: {animeID}")

    print(f"Data saved to {output_path}")

if __name__ == '__main__':
    main()
