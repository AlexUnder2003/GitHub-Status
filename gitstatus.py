from flask import Flask, render_template
import requests

app = Flask(__name__)


def get_github_status():
    url = "https://www.githubstatus.com/api/v2/components.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


@app.route("/")
def home():
    status_data = get_github_status()
    if status_data:
        components = status_data.get("components", [])
        print(components)
        return render_template("index.html", components=components)
    else:
        return "Error retrieving data from GitHub Status API."


if __name__ == "__main__":
    app.run(debug=True)
