<!-- ───────────────────────────── HEADER ───────────────────────────── -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=210&color=0:0b0a09,55:1F3A93,100:5B75E3&text=Bhargav%20Adepu&fontColor=ffffff&fontSize=58&fontAlignY=36&desc=I%20train%20models%20and%20ship%20the%20software%20around%20them.&descAlignY=58&descSize=17&animation=fadeIn" width="100%" alt="Bhargav Adepu — I train models and ship the software around them." />

<a href="https://bhargav.adepu.co.in">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=18&duration=3200&pause=900&color=5B75E3&center=true&vCenter=true&width=640&lines=AI%2FML+Engineer+%C2%B7+Full-Stack+Developer;Google+Summer+of+Code+2025+%40+VideoLAN+(VLC);IEEE+author+%C2%B7+AI+Intern+%40+Infosys;C%2FC%2B%2B+%C2%B7+Python+%C2%B7+Java+%C2%B7+TypeScript+%C2%B7+Dart" alt="AI/ML Engineer · Full-Stack Developer · GSoC 2025 @ VideoLAN · IEEE author" />
</a>

<p>
  <a href="https://bhargav.adepu.co.in"><img src="https://img.shields.io/badge/Portfolio-bhargav.adepu.co.in-1F3A93?style=flat-square&logo=astro&logoColor=white" alt="Portfolio" /></a>
  <a href="https://linkedin.com/in/bhargavvz"><img src="https://img.shields.io/badge/LinkedIn-bhargavvz-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://huggingface.co/bhargavvz"><img src="https://img.shields.io/badge/Hugging%20Face-bhargavvz-FFD21E?style=flat-square&logo=huggingface&logoColor=black" alt="Hugging Face" /></a>
  <a href="mailto:bhargavadepu@outlook.com"><img src="https://img.shields.io/badge/Email-bhargavadepu%40outlook.com-0b0a09?style=flat-square&logo=microsoftoutlook&logoColor=white" alt="Email" /></a>
  <a href="https://bhargav.adepu.co.in/Bhargav_Resume.pdf"><img src="https://img.shields.io/badge/Résumé-PDF-5B75E3?style=flat-square&logo=readdotcv&logoColor=white" alt="Résumé" /></a>
</p>

</div>

<!-- ───────────────────────────── ABOUT ───────────────────────────── -->

Most of my work sits at the same junction: **a model that has to survive contact with a real deployment** — behind an API, inside an app somebody actually opens, on a machine that costs money to keep running.

I spent summer 2025 inside **VLC's C/C++ and Qt codebase** as a Google Summer of Code contributor, I've published at **IEEE**, and I'm currently an **AI Intern at Infosys**. Every number below is the number the repository reports — including the unflattering ones.

<table>
<tr>
<td valign="top" width="50%">

**Now**
- 🧪 AI Intern · **Infosys** · Oct 2026 →
- 🎓 B.Tech CSE · CMR College of Engg. & Tech. · 2022 – 2026
- 📍 Warangal · Hyderabad · Remote

</td>
<td valign="top" width="50%">

**Previously**
- 🟠 **GSoC 2025 · VideoLAN** — AI media recommender for VLC
- 📄 **IEEE IC-SIT 2026** — published paper on disease-risk ML
- 🏆 2nd Runner-Up · HackByte, VIT-AP (300+ teams)

</td>
</tr>
</table>

<!-- ───────────────────────────── WORK ───────────────────────────── -->

## Selected work

<table>
<tr>
<td valign="top" width="50%">

### 🟠 [VLC AI Recommender](https://github.com/bhargavvz/GSoc-VLC)
<sub>Google Summer of Code 2025 · VideoLAN</sub>

A native module inside VLC — media feature extraction, metadata analysis and playback-based preference profiling feeding multiple recommendation algorithms, wired into VLC's CMake build.

`C` `C++` `Qt/QML` `CMake` `GitLab CI`

</td>
<td valign="top" width="50%">

### 🧠 [MedGPT](https://huggingface.co/bhargavvz/MedGPT)
<sub>Medical visual question answering</sub>

Qwen3-VL-8B fine-tuned with LoRA on 150K+ samples across X-ray, CT, MRI, ultrasound and pathology, with Grad-CAM showing where it looked.

**78.5%** overall · **87.1%** yes/no · **81.2%** token-F1

`PyTorch` `Transformers` `LoRA` `FastAPI` `Docker`

</td>
</tr>
<tr>
<td valign="top" width="50%">

### 💧 [AquaSafe](https://github.com/bhargavvz/aquasafe)
<sub>Waterborne-disease risk · published at IEEE IC-SIT 2026</sub>

Five models behind a JWT-secured Flask API and a 19-screen Flutter app. The first version scored 42.46% — [here's why that number stays](https://bhargav.adepu.co.in/writing/why-42-percent/).

**95.19%** disease · **99.25%** water safety · **AUC 0.9997** outbreak

`XGBoost` `LightGBM` `Flask` `Flutter` `PostgreSQL`

</td>
<td valign="top" width="50%">

### 📡 [PhotonQR](https://github.com/bhargavvz/PhotonQR)
<sub>File transfer across an air gap</sub>

One phone animates QR frames, another films them. No network, no pairing, no radio — and no network permission in the manifest at all.

**AES-256-GCM** per packet · **CRC-32** · loss-tolerant carousel · **~4 KB/s**

`Flutter` `Dart` `Cryptography` `GitHub Actions`

</td>
</tr>
<tr>
<td valign="top" width="50%">

### 🔬 [SkinGuard AI](https://huggingface.co/bhargavvz/SkinGuard-AI)
<sub>Dermoscopic lesion classification</sub>

Three-backbone ensemble (EVA-02 · ConvNeXt-V2 · Swin-V2) with learnable attention-weighted fusion, trained inside a 7-hour budget on a single H100.

**25,331** ISIC images · **8** classes · **589M** params

`PyTorch` `timm` `ONNX` `CUDA`

</td>
<td valign="top" width="50%">

### 🧭 [Meridian](https://github.com/bhargavvz/SCAM)
<sub>Supply-chain decision agent</sub>

Reads a free-text disruption report, recalls precedents from memory, checks records in SQLite, simulates each response and recommends one with cited evidence.

**14 / 14** holdout decisions matched

`FastAPI` `React` `TypeScript` `LLM agents` `Docker`

</td>
</tr>
<tr>
<td valign="top" width="50%">

### 🌍 [Communitfx](https://github.com/bhargavvz/Communitifx_v2)
<sub>Civic issue reporting · Honorable Mention, SDG 11, IIT Hyderabad</sub>

Geo-tagged reporting for potholes, garbage and broken streetlights — and a public trail of what happens next.

`Spring Boot` `React` `PostgreSQL` `Leaflet` `Mapbox GL`

</td>
<td valign="top" width="50%">

### 🔐 [VaultLock](https://bhargav.adepu.co.in/work/vaultlock/)
<sub>A password manager with nowhere to send your data</sub>

Zero-knowledge and offline-first, from one codebase on Android, iOS, Windows, macOS and Linux.

**AES-256-GCM** · **PBKDF2-SHA256** · **0** servers

`Flutter` `SQLite` `Cryptography`

</td>
</tr>
</table>

<div align="center">
<sub><a href="https://bhargav.adepu.co.in/#work">→ all twenty-one projects, with case studies</a></sub>
</div>

<!-- ───────────────────────────── STACK ───────────────────────────── -->

## What I reach for

<table>
<tr><td><b>AI / ML</b></td><td>

<img src="https://skillicons.dev/icons?i=pytorch,sklearn,opencv&perline=10" height="34" alt="AI/ML" /> &nbsp; <sub>Transformers · LoRA/PEFT · timm · XGBoost · LightGBM · Grad-CAM · ONNX</sub>

</td></tr>
<tr><td><b>Languages</b></td><td>

<img src="https://skillicons.dev/icons?i=py,c,cpp,java,ts,js,dart&perline=10" height="34" alt="Languages" />

</td></tr>
<tr><td><b>Web & mobile</b></td><td>

<img src="https://skillicons.dev/icons?i=react,nextjs,vue,spring,fastapi,flask,flutter,qt&perline=10" height="34" alt="Web and mobile" />

</td></tr>
<tr><td><b>Data</b></td><td>

<img src="https://skillicons.dev/icons?i=postgres,mysql,mongodb,redis,sqlite,supabase,firebase&perline=10" height="34" alt="Databases" />

</td></tr>
<tr><td><b>Cloud & DevOps</b></td><td>

<img src="https://skillicons.dev/icons?i=aws,docker,githubactions,jenkins,linux,git,cmake&perline=10" height="34" alt="Cloud and DevOps" />

</td></tr>
</table>

<!-- ───────────────────────────── WRITING + RECOGNITION ───────────────────────────── -->

<table>
<tr>
<td valign="top" width="50%">

## Writing

- [**Why 42% is the honest number**](https://bhargav.adepu.co.in/writing/why-42-percent/)<br><sub>The first model taught me more than the second.</sub>
- [**Fitting 589M parameters into seven hours**](https://bhargav.adepu.co.in/writing/seven-hours/)<br><sub>One H100, a hard stop, and the config it forced.</sub>
- [**Speaking Photon from a browser**](https://bhargav.adepu.co.in/writing/photon-from-a-browser/)<br><sub>A web page as a PhotonQR sender, judged by the app's own code.</sub>

</td>
<td valign="top" width="50%">

## Recognition

- 📄 [**IEEE IC-SIT 2026**](https://doi.org/10.1109/IC-SIT69723.2026.11735771) — ML framework for water-pollution disease-burden forecasting
- 🟠 **Google Summer of Code 2025** — VideoLAN
- 🥉 **2nd Runner-Up** — HackByte, VIT-AP · 300+ teams
- 🏅 **Honorable Mention, SDG 11** — Hack4SDG, IIT Hyderabad
- 🎯 **Finalist** — Specathon 2024, 36-hour hackathon
- 💡 **Intinta Innovator** — Government of Telangana

</td>
</tr>
</table>

<!-- ───────────────────────────── ACTIVITY ───────────────────────────── -->

## Activity

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=bhargavvz&theme=transparent&hide_border=true&ring=5B75E3&fire=5B75E3&currStreakLabel=5B75E3&stroke=30363d&background=00000000&sideNums=e6edf3&sideLabels=8b949e&dates=8b949e&currStreakNum=e6edf3" />
  <img src="https://streak-stats.demolab.com?user=bhargavvz&hide_border=true&ring=1F3A93&fire=1F3A93&currStreakLabel=1F3A93&background=00000000" alt="GitHub streak" />
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/bhargavvz/bhargavvz/output/github-contribution-grid-snake-dark.svg" />
  <img alt="Contribution graph being eaten by a snake" src="https://raw.githubusercontent.com/bhargavvz/bhargavvz/output/github-contribution-grid-snake.svg" />
</picture>

</div>

<!-- ───────────────────────────── FOOTER ───────────────────────────── -->

<div align="center">

**Open to software engineering roles in AI/ML, systems and full-stack.**<br>
<sub>The fastest way to reach me is <a href="mailto:bhargavadepu@outlook.com">bhargavadepu@outlook.com</a> — or try the lab on <a href="https://bhargav.adepu.co.in">my site</a>: draw a digit for a 40 KB CNN, or send me a message across an air gap.</sub>

<img src="https://capsule-render.vercel.app/api?type=waving&height=110&section=footer&color=0:5B75E3,45:1F3A93,100:0b0a09" width="100%" alt="" />

</div>
