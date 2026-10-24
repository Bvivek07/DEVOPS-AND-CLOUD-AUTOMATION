# FlowOps — DevOps Control Center

A new local Flask dashboard for demonstrating DevOps concepts. Sidebar navigation and dashboard controls are clickable. It opens the default browser automatically when started.

## Run in VS Code (Windows)

1. Extract this folder and open it in VS Code.
2. Open **Terminal → New Terminal**.
3. Run these commands:

```cmd
py -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py
```

4. The browser opens at `http://127.0.0.1:5000/`. If it does not, open that address manually.
5. Keep the terminal open while using the website. Press `Ctrl+C` in the terminal to stop it.

Docker is not required. Charts and pipeline statistics are illustrative sample data; the `/health` endpoint is live and served by Flask.
