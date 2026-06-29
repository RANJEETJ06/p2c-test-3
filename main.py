from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>Phone2Cloud Server</title>
        </head>
        <body style="font-family:Arial;text-align:center;padding-top:100px;">
            <h1>🚀 Server is Running</h1>
            <h2>Phone2Cloud Backend Online</h2>
            <p>Status: 🟢 Healthy</p>
        </body>
    </html>
    """


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "message": "Server is running"
    }
