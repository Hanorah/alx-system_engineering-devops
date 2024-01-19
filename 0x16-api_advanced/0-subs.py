#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    try:
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        response.raise_for_status()

        # Parse JSON response
        data = response.json()

        # Check if the subreddit exists
        if 'data' not in data:
            return 0

        # Extract the number of subscribers
        subscribers = data['data']['subscribers']
        return subscribers

    except requests.exceptions.RequestException as e:
        # Handle general request errors
        print(f"Error: {e}")
        return 0

# Example usage:
if __name__ == "__main__":
    subreddit_name = "programming"
    subscribers_count = number_of_subscribers(subreddit_name)
    print(subscribers_count)

