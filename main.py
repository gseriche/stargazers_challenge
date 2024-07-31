import requests
import yaml
import sys

def get_repo_stars(repo_list):
    base_url = "https://api.github.com/repos/"
    stars_dict = {}

    for repo in repo_list:
        url = base_url + repo
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            stars = data['stargazers_count']
            repo_name = repo.split('/')[-1]  # Extract repo name from full path
            stars_dict[repo_name] = stars
        else:
            print(f"Failed to fetch data for {repo}. Status code: {response.status_code}", file=sys.stderr)

    return stars_dict

def save_to_yaml(data, filename):
    with open(filename, 'w') as file:
        file.write("---\n")
        yaml.dump(data, file, default_flow_style=False)

def print_yaml(data):
    print("---")
    print(yaml.dump(data, default_flow_style=False))

if __name__ == "__main__":
    # Example usage
    repo_list = [
        "freeCodeCamp/freeCodeCamp",
        "996icu/996.ICU",
        "EbookFoundation/free-programming-books"
    ]

    stars_data = get_repo_stars(repo_list)
    
    # Print the output
    print("GitHub Repository Stars:")
    print_yaml(stars_data)
    
    # Save to file
    output_file = 'github_stars.yaml'
    save_to_yaml(stars_data, output_file)
    print(f"\nData has been saved to {output_file}")