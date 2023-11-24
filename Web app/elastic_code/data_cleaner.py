import json

def filter_ndjson(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            entry = json.loads(line)
            themes = entry.get('themes', [])
            genres = entry.get('genres', [])

            if 'erotica' not in themes and 'erotica' not in genres:
                # If 'erotic' is not present in themes or genres, write the entry to the output file
                outfile.write(json.dumps(entry) + '\n')

# Replace the paths with your actual input and output file paths using double backslashes
input_path = 'C:\\Users\\Thitiwut\\Documents\\GitHub\\AnimeSearchEngine_Via_ElasticSearch\\Web app\\elastic_code\\anime_data4.json'
output_path = 'C:\\Users\\Thitiwut\\Documents\\GitHub\\AnimeSearchEngine_Via_ElasticSearch\\Web app\\elastic_code\\anime_data5.json'

filter_ndjson(input_path, output_path)
