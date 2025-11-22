import json
from pathlib import Path

# Títulos base (puedes ampliarlos si quieres, pero así ya queda variado)
BASE_TITLES = [
    "The Shawshank Redemption", "The Godfather", "The Dark Knight",
    "Pulp Fiction", "Forrest Gump", "Inception", "Fight Club",
    "The Matrix", "Goodfellas", "The Lord of the Rings: The Fellowship of the Ring",
    "The Lord of the Rings: The Two Towers", "The Lord of the Rings: The Return of the King",
    "Interstellar", "Parasite", "Gladiator", "Whiplash", "The Prestige",
    "The Green Mile", "Se7en", "The Silence of the Lambs",
    "Saving Private Ryan", "Schindler's List", "Spirited Away",
    "The Lion King", "Terminator 2: Judgment Day", "Back to the Future",
    "The Departed", "Django Unchained", "The Pianist", "Avengers: Endgame",
    "Avengers: Infinity War", "Jurassic Park", "The Truman Show",
    "Mad Max: Fury Road", "Alien", "Aliens", "Toy Story",
    "Toy Story 3", "Coco", "Up", "Inside Out",
    "The Social Network", "No Country for Old Men", "There Will Be Blood",
    "City of God", "American Beauty", "Braveheart", "The Wolf of Wall Street",
    "Inglourious Basterds", "Shutter Island", "The Usual Suspects"
]

def main():
    movies = []
    base_len = len(BASE_TITLES)

    for i in range(500):
        base_title = BASE_TITLES[i % base_len]
        # Para evitar que todas se vean iguales, añadimos una variación ligera
        season = i // base_len + 1
        if season > 1:
            title = f"{base_title} #{season}"
        else:
            title = base_title

        year = 1980 + (i % 45)  # años entre 1980 y 2024

        movie = {
            "id": i + 1,
            "title": title,
            "year": year,
            "description": f"Breve sinopsis de la película \"{title}\", estrenada en el año {year}. Este texto se utiliza como ejemplo para demostrar la vista de detalle en la aplicación reactiva.",
            "image_url": f"https://via.placeholder.com/300x450?text=Movie+{i+1}"
        }
        movies.append(movie)

    # Guardar en api/movies.json
    base_dir = Path(__file__).resolve().parent.parent  # raíz del proyecto (donde está manage.py)
    target = base_dir / "api" / "movies.json"
    target.write_text(json.dumps(movies, indent=4, ensure_ascii=False), encoding="utf8")

    print(f"Generadas {len(movies)} películas en {target}")

if __name__ == "__main__":
    main()
