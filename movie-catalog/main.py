from fastapi import FastAPI, Request

app = FastAPI(
    title="Movie Catalog",
)


@app.get("/")
def read_root(
    request: Request,
    name: str = "Anonym",
):
    docs_url = request.url.replace(
        path="/docs",
        query="",
    )
    return {
        "message": f"{name}, welcome to Movie Catalog app!",
        "docs": str(docs_url),
    }
