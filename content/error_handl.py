def handle_error(response):
    if response.status_code == 404:
        return "Resource not found"
    elif response.status_code == 401:
        return "Unauthorized access"
    elif response.status_code == 403:
        return "Forbidden access"
    else:
        return f"Unknown error: {response.status_code}"
