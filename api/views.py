import json
from django.http import JsonResponse, Http404
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Cargar todas las películas en memoria
with open(BASE_DIR / "movies.json", "r", encoding="utf8") as f:
    MOVIES = json.load(f)


@csrf_exempt
@require_GET
def search_movies(request):
    """
    Endpoint de búsqueda reactiva:
    /api/movies?search=texto
    """
    query = request.GET.get("search", "").lower().strip()

    if len(query) < 2:
        return JsonResponse([], safe=False)

    results = [
        m for m in MOVIES
        if query in m["title"].lower()
    ][:50]  # devolvemos hasta 50 para tener más variedad

    return JsonResponse(results, safe=False)


@csrf_exempt
@require_GET
def movie_detail(request, movie_id: int):
    """
    Detalle de una película por id:
    /api/movies/<id>
    """
    for m in MOVIES:
        if m["id"] == movie_id:
            detail = {
                "id": m["id"],
                "title": m["title"],
                "year": m.get("year"),
                "description": m.get(
                    "description",
                    "Sinopsis no disponible para este título."
                ),
                "image_url": m.get(
                    "image_url",
                    f"https://via.placeholder.com/300x450?text={m['title'].replace(' ', '+')}"
                )
            }
            return JsonResponse(detail, safe=False)

    raise Http404("Película no encontrada")
