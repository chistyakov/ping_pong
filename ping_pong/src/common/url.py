def build_url(base_url: str, path: str) -> str:
    return f"{base_url.strip('/')}/{path.strip('/')}"
