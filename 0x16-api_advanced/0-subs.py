#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check for a successful response (status code 200)
        response.raise_for_status()

        # Check for invalid subreddit (status code 404)
        if response.status_code == 404:
            return 0

        # Extract the number of subscribers from the JSON response
        results = response.json().get("data")
        return results.get("subscribers")

    except requests.exceptions.HTTPError as e:
        # Handle HTTP errors
        print("Error:", e)
        return 0

    except requests.exceptions.RequestException as e:
        # Handle general request errors
        print("Error:", e)
        return 0

# Example usage:
if __name__ == "__main__":
    subreddit_name = "programming"
    subscribers_count = number_of_subscribers(subreddit_name)
    print(subscribers_count)
