import requests

def get_random_dog_image():
    url = "https://api.thedogapi.com/v1/images/search"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[0]['url']
    else:
        return None

def update_readme(image_url):
    with open("README.md", "r") as file:
        readme_content = file.readlines()

    new_readme_content = []
    in_dog_image_section = False

    for line in readme_content:
        if "### Random Dog Image from The Dog API" in line:
            in_dog_image_section = True
            new_readme_content.append(line)
            new_readme_content.append(f"![Dog Image]({image_url})\n")
        elif in_dog_image_section and line.startswith("![Dog Image]"):
            continue
        else:
            in_dog_image_section = False
            new_readme_content.append(line)

    with open("README.md", "w") as file:
        file.writelines(new_readme_content)

if __name__ == "__main__":
    image_url = get_random_dog_image()
    if image_url:
        update_readme(image_url)
    else:
        print("Failed to retrieve a new dog image")
