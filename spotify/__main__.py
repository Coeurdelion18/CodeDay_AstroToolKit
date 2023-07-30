from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

@app.get("/{page_path:path}")
async def serve_static_page(page_path: str):
    page_file = Path(page_path)
    if page_file.is_file():
        return FileResponse(page_file)
    return {"message": "Page not found"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=3000)
