from uuid import UUID
from pydantic import BaseModel, PositiveInt, HttpUrl, conint, conlist


class GameModel(BaseModel):
    id: PositiveInt
    category: conint(ge=0)
    created_at: PositiveInt
    name: str
    slug: str
    updated_at: PositiveInt
    url: HttpUrl
    checksum: UUID

    age_ratings: conlist(int, min_items=1) = None
    aggregated_rating: float = None
    aggregated_rating_count: int = None
    artworks: conlist(int, min_items=1) = None
    collection: int = None
    cover: int = None
    external_games: conlist(int, min_items=1) = None
    first_release_date: int = None
    follows: int = None
    game_engines: conlist(int, min_items=1) = None
    game_modes: conlist(int, min_items=1) = None
    genres: conlist(int, min_items=1) = None
    involved_companies: conlist(int, min_items=1) = None
    keywords: conlist(int, min_items=1) = None
    platforms: conlist(int, min_items=1) = None
    player_perspectives: conlist(int, min_items=1) = None
    rating: float = None
    rating_count: int = None
    release_dates: conlist(int, min_items=1) = None
    screenshots: conlist(int, min_items=1) = None
    similar_games: conlist(int, min_items=1) = None
    storyline: str = None
    summary: str = None
    tags: conlist(int, min_items=1) = None
    themes: conlist(int, min_items=1) = None
    total_rating: float = None
    total_rating_count: int = None
    videos: conlist(int, min_items=1) = None
    websites: conlist(int, min_items=1) = None
    remakes: conlist(int, min_items=1) = None
