## University of West London
<!-- .slide: data-background="#09091e" data-transition="fade" -->

<img src="images/coding%20club%20logo.png" width="50%" />

### Coding Club by ATAL Society

Hands-On Local AI Workshop <!-- .element: class="fragment r-fit-text" -->

---
---

## House Keeping
<!-- .slide: data-transition="fade" -->

- Ask questions anytime <!-- .element: class="fragment" -->
- Pair up if needed <!-- .element: class="fragment" -->
- Use your own laptop or follow the main demo <!-- .element: class="fragment" -->



---
---


## Session Roadmap
<!-- .slide: data-transition="fade" -->

1. Why local and open source AI?
2. Setup and tools
3. Ollama core workflow (5 key commands)
4. Add a simple UI
5. Prompt engineering resources

---
---

## Why this matters
<!-- .slide: data-transition="fade" -->

![](images/00-poster-transparent.png)

---
---


## Working definition: Open Source AI
<!-- .slide: data-transition="fade" -->

<small>An Open Source AI system should grant users the freedom to:</small>

- Use <!-- .element: class="fragment" -->
- Study <!-- .element: class="fragment" -->
- Modify <!-- .element: class="fragment" -->
- Share <!-- .element: class="fragment" -->

---

### Use

![](images/04-osi-ai-a.png)

---

### Study

![](images/04-osi-ai-b.png)

---

### Modify

![](images/04-osi-ai-c.png)

---

### Share

![](images/04-osi-ai-d.png)

---
---

## Primary use cases for local AI
<!-- .slide: data-transition="fade" -->

- Avoid ongoing hosted API costs <!-- .element: class="fragment" -->
- Work fully offline <!-- .element: class="fragment" -->
- Keep sensitive data private <!-- .element: class="fragment" -->
- Reduce latency for frequent inference <!-- .element: class="fragment" -->
- Keep behavior more stable over time <!-- .element: class="fragment" -->
- Customise model and workflow <!-- .element: class="fragment" -->

---

---

## Setup: tools for local LLMs
<!-- .slide: data-transition="fade" -->

| Name            | Link                         |
|-----------------|------------------------------|
| Ollama          | https://ollama.com           |
| LM Studio       | https://lmstudio.ai          |
| vLLM            | https://blog.vllm.ai         |
| Others (Nomic?) | https://www.nomic.ai/gpt4all |

---
---

## Tool focus for today: Ollama
<!-- .slide: data-transition="fade" -->

![](images/05-ollama-ascii.png)

---

### What Ollama gives you

**Ollama** lets you run LLMs locally and manage model files from terminal:

- pull
- list
- run
- ps
- serve

---
---

## Step 0: check installation
<!-- .slide: data-transition="fade" -->

```shell [1|2]
ollama --version
ollama version is 0.9.6
```

---

### Install quick guide (Mac / Win / Linux)

<small>Official docs: [github.com/ollama/ollama](https://github.com/ollama/ollama)</small>

```sh
# macOS (app download)
https://ollama.com/download/Ollama-darwin.zip
https://ollama.com/download/Ollama.dmg

# Windows
https://ollama.com/download/OllamaSetup.exe

# Linux
curl -fsSL https://ollama.com/install.sh | sh
```

---
---

## Step 1: discover commands
<!-- .slide: data-transition="fade" -->

```txt [1:1|7-18]
> ollama
Usage:
  ollama [flags]
  ollama [command]

Available Commands:
  serve       Start ollama
  create      Create a model from a Modelfile
  show        Show information for a model
  run         Run a model
  stop        Stop a running model
  pull        Pull a model from a registry
  push        Push a model to a registry
  list        List models
  ps          List running models
  cp          Copy a model
  rm          Remove a model
  help        Help about any command
```

---
---

## Step 2: pull a model
<!-- .slide: data-transition="fade" -->

```sh [1]
ollama pull ModelName[:size]
```

[https://ollama.com/search](https://ollama.com/search)

---

### Model size matters

![](images/07-weight.png)

---

### Bigger model != always better for your machine

![](images/08-mnist-2-layer-system.gif)

---

### Pick based on RAM/VRAM and speed needs

![](images/09-mnist-anim.gif)

---
---

## Step 3: list local models
<!-- .slide: data-transition="fade" -->

```text
ollama list
NAME                                  ID              SIZE      MODIFIED
qwen3                                 500a1f067a9f    5.2 GB    6 seconds ago
qwen3:30b-a3b                         0b28110b7a33    18 GB     6 weeks ago
qwen3:8b                              500a1f067a9f    5.2 GB    6 weeks ago
qwen3:14b                             bdbd181c33f2    9.3 GB    6 weeks ago
qwen3:30b                             0b28110b7a33    18 GB     6 weeks ago
qwen2.5:7b                            845dbda0ea48    4.7 GB    6 weeks ago
deepseek-r1:1.5b                      e0979632db5a    1.1 GB    7 weeks ago
qwen3:0.6b                            7df6b6e09427    522 MB    7 weeks ago
qwen2.5-coder:0.5b                    4ff64a7f502a    397 MB    7 weeks ago
phi4-reasoning:latest                 47e2630ccbcd    11 GB     7 weeks ago
devstral:24b                          c4b2fa0c33d7    14 GB     7 weeks ago
devstral:latest                       c4b2fa0c33d7    14 GB     7 weeks ago
devstral:24b-small-2505-q4_K_M        c4b2fa0c33d7    14 GB     7 weeks ago
llama3.1:latest                       46e0c10c039e    4.9 GB    3 months ago
llama3.1:8b                           46e0c10c039e    4.9 GB    3 months ago
deepseek-coder-v2:latest              63fb193b3a9b    8.9 GB    3 months ago
gemma3:12b                            f4031aab637d    8.1 GB    3 months ago
gemma3:4b                             a2af6cc3eb7f    3.3 GB    3 months ago
llama2-uncensored:latest              44040b922233    3.8 GB    3 months ago
llama2-uncensored:7b                  44040b922233    3.8 GB    3 months ago
```

```sh [1]
ollama list | grep mini
```

---
---

## Step 4: run inference
<!-- .slide: data-transition="fade" -->

```sh [1|3]
ollama run qwen3 "What is the colour of the sky? Keep it short!"
# OR interactive mode
ollama run qwen3
```

---

### Advanced: remote host

Environment Variables:
      OLLAMA_HOST                IP Address for the ollama server (default 127.0.0.1:11434)
      OLLAMA_NOHISTORY           Do not preserve readline history ( ~/.ollama/history )
```

---
---

## Step 5: monitor process + serve API
<!-- .slide: data-transition="fade" -->

```sh [1-3|1]
ollama ps
NAME            ID              SIZE      PROCESSOR    UNTIL
qwen3:latest    500a1f067a9f    7.6 GB    100% GPU     4 minutes from now
```

```sh [1-4]
ollama serve # after closing the desktop app if needed
```

---
---


## Extra CLI essentials
<!-- .slide: data-transition="fade" -->

```sh [1|2|3]
ollama run llama2
/bye
ollama list
```

<small>`ollama run - ` auto-downloads missing models, </br> `bye - ` exits chat, </br> `ollama list - ` shows installed models.</small>

---
---

## Local API endpoint
<!-- .slide: data-transition="fade" -->

`http://localhost:11434`

- Used by local apps and scripts <!-- .element: class="fragment" -->
- Start manually with "ollama serve" if backend is not running <!-- .element: class="fragment" -->

---

### API quick test with curl

```sh
curl http://localhost:11434/api/generate \
  -d '{
    "model": "qwen3",
    "prompt": "Give me 3 coding club project ideas",
    "stream": false
  }'
```

---
---

## Python integration
<!-- .slide: data-transition="fade" -->

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install ollama

Then verify:
python -c "import ollama; print('ok')"


```

```python
from ollama import chat

response = chat(
    model="qwen3",
    messages=[{"role": "user", "content": "Explain local LLMs in one sentence."}],
)
print(response["message"]["content"])
```

<small>
`model` chooses which local model to run (here: `qwen3`).
`role` tells who is speaking (`user`, `system`, `assistant`) and `content` is the prompt text.
</small>

---
---


## Add a UI: Chatbox AI app
<!-- .slide: data-transition="fade" data-background="#d5d772" -->

**[https://chatboxai.app](https://chatboxai.app)**

---

### UI walkthrough

<small>Live demo order: connect model -> test web search -> tune generation settings.</small>


![](images/10-gui.png)

---

![](images/11-gui-settings.png)

---

![](images/12-gui-add.png)

---

![](images/13-gui-models.png)

---

![](images/14-gui-search-api.png)

---

![](images/15-gui-kno.png)

---

![](images/16-gui-auto-up.png)

---

![](images/17-gui-last.png)


---

## Web feature ideas (Chatbox AI)
<!-- .slide: data-transition="fade" -->

- Use web mode for time-sensitive questions (news, releases, API changes) <!-- .element: class="fragment" -->
- Ask for sources: "Give links and a 1-line summary for each source" <!-- .element: class="fragment" -->
- Compare local-only vs web-enabled answers to show differences <!-- .element: class="fragment" -->
- Verify at least one source manually before sharing <!-- .element: class="fragment" -->

```txt
Prompt idea:
"Find 3 recent AI news and summarise each in 2 bullets."
```

---

## Parameter playground (temperature + top_p)
<!-- .slide: data-transition="fade" -->

| Goal | Temperature | top_p |
|---|---:|---:|
| Stable factual answers | 0.1 - 0.3 | 0.7 - 0.9 |
| Balanced tutor mode | 0.4 - 0.7 | 0.9 |
| Brainstorm / creative mode | 0.8 - 1.2 | 0.95 - 1.0 |

<small>Exercise: keep one prompt fixed, change one parameter at a time, compare clarity vs creativity.</small>

---
---

## Troubleshooting quick tips
<!-- .slide: data-transition="fade" -->

| Issue | Fix |
|---|---|
| `ollama: command not found` | Restart terminal and verify install path |
| Download too slow | Use a smaller model first |
| Model crashes machine | Try lower parameter size (e.g. `:0.6b`, `:1b`, `:4b`) |
| API client cannot connect | Verify `OLLAMA_HOST` and that `ollama serve` is running |

---
---

## Prompt security challenge
<!-- .slide: data-transition="fade" -->

Try the Gandalf prompt injection game:

**[https://gandalf.lakera.ai/baseline](https://gandalf.lakera.ai/baseline)**

---
---

## Wrap-up
<!-- .slide: data-transition="fade" -->

- You now have a local-first AI workflow
- You can run private experiments offline
- Next session: build your own local AI mini-project

### University of West London x Coding Club by ATAL Society

<img src="images/coding%20club%20logo.png" width="50%" />

---
---
