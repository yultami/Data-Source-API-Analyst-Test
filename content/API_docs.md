# API Documentation

## Introduction
This document contains information about the API endpoints used in this project.

## Endpoints

### Searching Repositories
- **URL**: `https://api.github.com/search/repositories`
- **Method**: GET
- **Parameters**:
- `q`: Query String
- `sort`: Sort by (e.g. stars, forks)
- `order`: Order by (e.g. desc, asc)

### Fetching Commits
- **URL**: `https://api.github.com/repos/{owner}/{repo}/commits`
- **Method**: GET
- **Parameters**:
- `sha`: SHA of the commit
- `path`: Path to the file