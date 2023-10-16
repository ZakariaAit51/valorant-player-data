# Valorant Player Data Retrieval

This Python script allows you to retrieve Valorant player data using the [HenrikDev API](https://api.henrikdev.xyz/valorant).

## Usage

1. Make sure you have Python installed on your system.

2. Clone this repository:
   ```
   git clone https://github.com/ZakariaAit51/valorant-player-data.git
   ```

3. Navigate to the project directory:
   ```
   cd valorant-player-data
   ```

4. Run the script and follow the prompts to input the number of players and their names:
   ```
   python main.py
   ```

The script will fetch player data from the HenrikDev API and display their name, level, and rank.

## Dependencies

- `requests`: HTTP library for making API requests.
- `json`: Library for working with JSON data.

## Sample Output

```
Number of players
2
Enter the name#tag of the player
example#123
name: example, level: 10, rank: Diamond 3
```

## Disclaimer

This script uses the HenrikDev API to fetch player data and MMR information. Please ensure you have appropriate permissions and follow the API usage policy.

---

Replace `"yourusername"` with your GitHub username and `"valorant-player-data"` with the appropriate repository name.
