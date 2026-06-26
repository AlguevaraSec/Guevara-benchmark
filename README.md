# ⚡ Guevara Benchmark

<p align="center">
  <img src="[https://your-image-url-here.com/banner.png](https://i.ibb.co/sJccxL0k/79644a17-c546-461a-a913-35da0f3b2e68.png)" alt="Guevara Benchmark Banner" width="100%">
</p>

<p align="center">

**A modern asynchronous HTTP load testing & benchmarking tool built with FastAPI and aiohttp.**

Designed for developers to evaluate the performance of their own web applications and APIs.

</p>

---

## ✨ Features

* ⚡ High-performance asynchronous requests
* 🚀 Configurable concurrency
* 📊 Requests per second (RPS) calculation
* 📈 HTTP status code statistics
* 🖥️ Modern web interface
* 📝 Custom headers support
* 📦 GET & POST requests
* 🔒 Transparent User-Agent by default
* 🐍 Pure Python

---

## 📸 Screenshot



![Guevara UI](https://i.ibb.co/pvLF45J7/Screenshot-2026-06-26-032830.png)
some Result with 5 sec test (https://i.ibb.co/qYDVrQyG/Screenshot-2026-06-26-034142.png)
---

## 🚀 Installation

```bash
git clone https://github.com/AlguevaraSec/Guevara-benchmark.git
cd Guevara-benchmark

pip install -r requirements.txt

python main.py

or uvicorn main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000
```

---

## 📊 Example Result

```
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

## ⚙️ Technologies

* FastAPI
* aiohttp
* asyncio
* Uvicorn
* HTML/CSS/JavaScript

---

# 🛡️ Protect Your Server

If your application is exposed to the Internet, you should protect it against excessive traffic.

### ✅ Use a Rate Limiter

Implement request rate limiting on your application or reverse proxy.

Examples:

* FastAPI rate limiting middleware
* Nginx rate limiting
* Traefik rate limiting

---

### ☁️ Use Cloudflare

Cloudflare's free plan is easy to set up and provides:

* DDoS protection L4 & L7 (with powerfull rules)
* Recommended changing your main server ip when use cloudflare.
* Web Application Firewall (WAF)
* Bot protection
* Rate limiting (advanced features vary by plan)
* Global CDN

For most small and medium websites, enabling Cloudflare is one of the quickest ways to improve resilience.

---

## ⚠️ Educational & Authorized Use Only

This project is intended **only** for:

* Performance testing
* Load benchmarking
* Capacity planning
* Educational purposes
* Testing systems that **you own or are explicitly authorized to test**

Do **not** use this software against systems without permission.

I assume **no responsibility** for misuse or damage caused by this project.

---

## 🤝 Contributing

Contributions, improvements, and bug reports are welcome.

Feel free to open an Issue or submit a Pull Request.

---

## 📄 License

MIT License

---

<p align="center">

Made with smoke by **Guevara**

</p>
