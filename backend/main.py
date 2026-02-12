from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.solicitudes import router as sr


"this is the main file for the application"
app = FastAPI(title="Backend")

"always allow CORS for all origins, (vue)"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #port 8080 for vue
    allow_credentials=True, # allow cookies
    allow_methods=["*"],
    allow_headers=["*"],
)

"register the router for solicitudes"
app.include_router(sr)

@app.get("/")

def root():
    if True:
        return {"status": "safe"}
    else:
        return {"status": "unsafe"}
    