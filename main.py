import asyncio
import aiohttp
import time
import json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class LoadTestRequest(BaseModel):
    url: str
    method: str
    headers: str
    body: str
    concurrent: int
    req_per_concurrent: int

# Modern, dark-themed some of test UI
HTML_UI = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guevara Load Benchmark</title>
    <style>
        :root {
            --bg-color: #0d0d12;
            --panel-bg: #15151e;
            --accent: #00ff88;
            --accent-dim: #00ff8833;
            --text-main: #e0e0e0;
            --text-muted: #8888a0;
        }
        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            font-family: 'Consolas', 'Courier New', monospace;
            margin: 0;
            padding: 2rem;
            display: flex;
            justify-content: center;
        }
        .container {
            width: 100%;
            max-width: 800px;
            background: var(--panel-bg);
            border: 1px solid var(--accent-dim);
            border-radius: 8px;
            padding: 2rem;
            box-shadow: 0 0 20px rgba(0, 255, 136, 0.05);
        }
        h1 {
            color: var(--accent);
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-top: 0;
            border-bottom: 1px solid var(--accent-dim);
            padding-bottom: 1rem;
        }
        .form-group {
            margin-bottom: 1.5rem;
        }
        label {
            display: block;
            margin-bottom: 0.5rem;
            color: var(--text-muted);
            text-transform: uppercase;
            font-size: 0.85rem;
        }
        input, select, textarea {
            width: 100%;
            background: rgba(0, 0, 0, 0.3);
            border: 1px solid #333;
            color: var(--text-main);
            padding: 0.75rem;
            font-family: inherit;
            border-radius: 4px;
            box-sizing: border-box;
        }
        input:focus, select:focus, textarea:focus {
            outline: none;
            border-color: var(--accent);
            background: rgba(0, 255, 136, 0.02);
        }
        .row {
            display: flex;
            gap: 1rem;
        }
        .row > .form-group {
            flex: 1;
        }
        button {
            width: 100%;
            background: var(--accent-dim);
            color: var(--accent);
            border: 1px solid var(--accent);
            padding: 1rem;
            font-size: 1rem;
            font-weight: bold;
            text-transform: uppercase;
            cursor: pointer;
            transition: all 0.2s ease;
            border-radius: 4px;
        }
        button:hover {
            background: var(--accent);
            color: #000;
        }
        #results {
            margin-top: 2rem;
            background: #000;
            border: 1px solid #333;
            padding: 1rem;
            border-radius: 4px;
            min-height: 100px;
            white-space: pre-wrap;
        }
        .status-badge {
            display: inline-block;
            padding: 0.25rem 0.5rem;
            background: #222;
            border-radius: 3px;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>[+] Benchmark Engine</h1>
        
        <div class="form-group">
            <label>Target URL</label>
            <input type="text" id="url" placeholder="https://api.example.com/v1/data" required>
        </div>

        <div class="row">
            <div class="form-group">
                <label>Method</label>
                <select id="method">
                    <option value="GET">GET</option>
                    <option value="POST">POST</option>
                </select>
            </div>
        </div>

        <div class="row">
            <div class="form-group">
                <label>Concurrency (Workers)</label>
                <input type="number" id="concurrent" value="10" min="1">
            </div>
            <div class="form-group">
                <label>Requests per Worker</label>
                <input type="number" id="req_per_concurrent" value="100" min="1">
            </div>
        </div>

        <div class="form-group">
            <label>Headers (JSON Format)</label>
            <textarea id="headers" rows="3" placeholder='{"Content-Type": "application/json"}'></textarea>
        </div>

        <div class="form-group">
            <label>Request Body (Optional)</label>
            <textarea id="body" rows="3" placeholder='{"key": "value"}'></textarea>
        </div>

        <button onclick="startTest()" id="runBtn">Initialize Attack Vector ... Just Kidding, Run Benchmark</button>

        <div id="results">> Awaiting execution parameters...</div>
    </div>

    <script>
        async function startTest() {
            const btn = document.getElementById('runBtn');
            const resultsDiv = document.getElementById('results');
            
            btn.innerText = 'EXECUTING BENCHMARK...';
            btn.style.pointerEvents = 'none';
            resultsDiv.innerText = '> Establishing async connections...';

            const payload = {
                url: document.getElementById('url').value,
                method: document.getElementById('method').value,
                headers: document.getElementById('headers').value || '{}',
                body: document.getElementById('body').value || '',
                concurrent: parseInt(document.getElementById('concurrent').value),
                req_per_concurrent: parseInt(document.getElementById('req_per_concurrent').value)
            };

            try {
                const response = await fetch('/api/benchmark', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                
                const data = await response.json();
                
                let output = `> BENCHMARK COMPLETE\n`;
                output += `----------------------------------------\n`;
                output += `Total Requests : ${data.total_requests}\n`;
                output += `Time Elapsed   : ${data.duration} seconds\n`;
                output += `Throughput     : ${data.requests_per_second} req/sec\n`;
                output += `----------------------------------------\n`;
                output += `> STATUS CODES:\n`;
                
                for (const [code, count] of Object.entries(data.status_codes)) {
                    output += `  [HTTP ${code}] : ${count} responses\n`;
                }
                
                resultsDiv.innerText = output;
            } catch (err) {
                resultsDiv.innerText = `> ERROR: ${err.message}`;
            } finally {
                btn.innerText = 'Run Benchmark';
                btn.style.pointerEvents = 'auto';
            }
        }
    </script>
</body>
</html>
"""

async def worker(session: aiohttp.ClientSession, url: str, method: str, headers: dict, body: str, req_count: int, results: dict):
    for _ in range(req_count):
        try:
            if method == "GET":
                async with session.get(url, headers=headers, ssl=False) as resp:
                    status = str(resp.status)
            else:
                async with session.post(url, headers=headers, data=body, ssl=False) as resp:
                    status = str(resp.status)
            
            results[status] = results.get(status, 0) + 1
        except Exception as e:
            results["Error"] = results.get("Error", 0) + 1

@app.get("/", response_class=HTMLResponse)
async def serve_ui():
    return HTML_UI

@app.post("/api/benchmark")
async def run_benchmark(config: LoadTestRequest):
    # Parse headers safely
    try:
        headers_dict = json.loads(config.headers) if config.headers.strip() else {}
    except json.JSONDecodeError:
        headers_dict = {}

    # Enforce Transparency
    header_keys = [k.lower() for k in headers_dict.keys()]
    if "user-agent" not in header_keys:
        headers_dict["User-Agent"] = "LocalBenchmarker/1.0 (Diagnostic Mode)"

    results = {}
    start_time = time.time()

    # Utilize aiohttp for high-speed concurrent event loops
    connector = aiohttp.TCPConnector(limit=config.concurrent)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for _ in range(config.concurrent):
            tasks.append(worker(session, config.url, config.method, headers_dict, config.body, config.req_per_concurrent, results))
        
        await asyncio.gather(*tasks)

    duration = time.time() - start_time
    total = config.concurrent * config.req_per_concurrent
    rps = total / duration if duration > 0 else 0

    return {
        "duration": round(duration, 2),
        "total_requests": total,
        "requests_per_second": round(rps, 2),
        "status_codes": results
    }

if __name__ == "__main__":
    # Start the application on localhost port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)