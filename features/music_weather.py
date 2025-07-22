def get_song(weather: str) -> str:
    # Very basic weather-to-song mapping
    songs = {
        "sunny": "Walking on Sunshine – Katrina & The Waves",
        "rainy": "Set Fire to the Rain – Adele",
        "cloudy": "Cloudy – Simon & Garfunkel",
        "snowy": "Let It Go – Idina Menzel",
        "storm": "Thunder – Imagine Dragons"
    }
    return songs.get(weather.lower(), "Here Comes the Sun – The Beatles")