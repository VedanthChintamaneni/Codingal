import sys
import json
import urllib.request
import urllib.error

try:
	import requests
except ImportError:
	requests = None

def getPokemondata():
	pokemonName = input("[Write 'exit' to leave program] Enter pokemon name: ").strip()
	if pokemonName.lower() == "exit":
		sys.exit()
	if pokemonName == "":
		print("Please enter a pokemon name or 'exit'.")
		return None

	name = pokemonName.lower()
	stat_url = f"https://pokeapi.co/api/v2/pokemon/{name}"
	lore_url = f"https://pokeapi.co/api/v2/pokemon-species/{name}"

	def fetch(url):
		if requests:
			try:
				r = requests.get(url, timeout=10)
				return r.status_code, r.json()
			except requests.RequestException as e:
				return None, str(e)
		else:
			# Try to use certifi for SSL verification when available
			context = None
			try:
				import ssl
				import certifi
				context = ssl.create_default_context(cafile=certifi.where())
			except Exception:
				context = None

			try:
				if context:
					with urllib.request.urlopen(url, timeout=10, context=context) as resp:
						data = resp.read().decode('utf-8')
						return resp.getcode(), json.loads(data)
				else:
					with urllib.request.urlopen(url, timeout=10) as resp:
						data = resp.read().decode('utf-8')
						return resp.getcode(), json.loads(data)
			except urllib.error.HTTPError as e:
				return e.code, None
			except Exception as e:
				return None, repr(e)

	stat_status, stat_json = fetch(stat_url)
	lore_status, lore_json = fetch(lore_url)

	if stat_status == 200 and lore_status == 200:
		Sdata = stat_json
		Ldata = lore_json
		print()
		print(f"Name: {Sdata.get('name','N/A').capitalize()}")
		types = [t['type']['name'].capitalize() for t in Sdata.get('types', [])]
		print(f"Type: {', '.join(types) if types else 'N/A'}")

		# Print basic stats
		stats = {s['stat']['name']: s['base_stat'] for s in Sdata.get('stats', [])}
		if stats:
			stats_str = ', '.join(f"{k}: {v}" for k, v in stats.items())
			print(f"Base stats: {stats_str}")
		print(f"Height: {Sdata.get('height', 'N/A')}  Weight: {Sdata.get('weight', 'N/A')}")

		description = None
		for entry in Ldata.get('flavor_text_entries', []):
			if entry.get('language', {}).get('name') == 'en':
				description = entry.get('flavor_text', '')
				break

		if description:
			description = description.replace('\n', ' ').replace('\f', ' ')
			print(f"Description: {description}")
		else:
			print("Description: N/A")
	else:
		if stat_status == 404 or lore_status == 404:
			print("Pokemon not found. Check the name.")
		else:
			print(f"Error: status codes {repr(stat_status)}, {repr(lore_status)}")
			if stat_status is None or lore_status is None:
				if stat_status is None:
					print("Stat fetch error:", stat_json)
				if lore_status is None:
					print("Lore fetch error:", lore_json)
				print("If you're on macOS, install Python certificates or install the 'requests' package:")
				print("  pip install requests")
				print("or")
				print("  pip install certifi")

	return pokemonName


if __name__ == "__main__":
	try:
		while True:
			getPokemondata()
	except KeyboardInterrupt:
		print('\nExiting. Goodbye!')
		sys.exit(0)