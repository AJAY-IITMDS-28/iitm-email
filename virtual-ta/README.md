# Virtual TA for IITM Online Degree - Tools in Data Science

This project implements a virtual Teaching Assistant API for the TDS course. It answers student questions using scraped course content and Discourse posts.

## Features
- POST /api/ endpoint for student questions and optional base64 image
- Returns JSON with answer and relevant links
- MIT License

## Quickstart

1. Install dependencies:
   ```zsh
   pip install fastapi uvicorn python-multipart
   ```
2. Run the API:
   ```zsh
   uvicorn main:app --reload
   ```

## API Example

POST http://localhost:8000/api/
```json
{
  "question": "Should I use gpt-4o-mini or gpt-3.5-turbo?",
  "image": "<base64 string>"
}
```

## License
MIT
