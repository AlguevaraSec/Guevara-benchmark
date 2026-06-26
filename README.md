<div align="center">

# ⚡ Guevara Benchmark

<img src="https://i.ibb.co/sJccxL0k/79644a17-c546-461a-a913-35da0f3b2e68.png" width="100%" alt="Guevara Benchmark">

<br>

**High-performance asynchronous HTTP load testing & benchmarking tool**

Built with **FastAPI**, **aiohttp**, and **asyncio** for developers who need fast, lightweight, and modern API benchmarking.

<p>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Modern-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![aiohttp](https://img.shields.io/badge/aiohttp-Async-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

</p>

</div>

---

# ✨ Features

<table>
<tr>
<td width="50%">

- ⚡ High-performance asynchronous requests
- 🚀 Configurable concurrency
- 📊 Live Requests Per Second (RPS)
- 📈 HTTP status statistics
- 🖥️ Modern responsive Web UI

</td>
<td width="50%">

- 📝 Custom HTTP headers
- 📦 GET & POST support
- 🔒 Transparent User-Agent by default
- 🐍 Pure Python
- 💨 Lightweight & easy to deploy

</td>
</tr>
</table>

---

# 📸 Screenshots

## Dashboard

<p align="center">
<img src="https://i.ibb.co/pvLF45J7/Screenshot-2026-06-26-032830.png" width="95%">
</p>

---

## Benchmark Result

<p align="center">
<img src="https://i.ibb.co/qYDVrQyG/Screenshot-2026-06-26-034142.png" width="95%">
</p>

---

# 🚀 Installation

<details open>

<summary><b>Quick Start</b></summary>

```bash
git clone https://github.com/AlguevaraSec/Guevara-benchmark.git

cd Guevara-benchmark

pip install -r requirements.txt

python main.py

# or

uvicorn main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000
```

</details>

---

# 📊 Example Result

```text
BENCHMARK COMPLETE

----------------------------------------
Total Requests : 5000
Time Elapsed   : 4.72 seconds
Throughput     : 1059.3 req/sec
----------------------------------------

HTTP 200 : 4987
HTTP 522 : 13
```

---

# ⚙️ Built With

| Technology | Purpose |
|------------|---------|
| FastAPI | Backend Framework |
| aiohttp | Async HTTP Client |
| asyncio | Concurrency |
| Uvicorn | ASGI Server |
| HTML / CSS / JavaScript | Frontend |

---

# 🛡️ Protect Your Server

Benchmarking is useful—but every public service should also be protected.

## ✅ Rate Limiting

Implement request limits at your application or reverse proxy.

Recommended options:

- FastAPI Rate Limiting Middleware
- Nginx Rate Limiting
- Traefik Rate Limiting

---

## ☁️ Cloudflare

Cloudflare's free plan provides excellent protection for most applications.

### Benefits

- 🛡️ Layer 4 & Layer 7 DDoS Protection
- 🔥 Web Application Firewall (WAF)
- 🤖 Bot Protection
- ⚡ Global CDN
- 🚦 Rate Limiting *(advanced features depend on plan)*
- 🔒 Recommended to hide your origin server IP behind Cloudflare

For small and medium-sized websites, Cloudflare is one of the easiest ways to improve availability and resilience.

---

# ⚠️ Educational & Authorized Use Only

This project is intended **only** for:

- ✅ Performance testing
- ✅ Load benchmarking
- ✅ Capacity planning
- ✅ Educational purposes
- ✅ Testing systems you own or are explicitly authorized to test

> **Do not use this software against systems without permission.**

The author assumes **no responsibility** for misuse or any damage caused by this software.

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve Guevara Benchmark:

- 🐞 Open an Issue
- 💡 Suggest a Feature
- 🔧 Submit a Pull Request

Every contribution is appreciated.

---

# 📄 License

Distributed under the **MIT License**.

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a Star!

Made with 💨 by **Guevara**

</div>
