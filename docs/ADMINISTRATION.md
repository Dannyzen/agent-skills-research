# Clawd Workspace Administration

This document outlines the administration, management, and troubleshooting patterns for the Clawd ecosystem running on your machine. This workspace acts as the unified "Brain" and "Soul" for whichever agent framework (Openclaw or Microclaw) is currently active.

## 1. Ecosystem Overview

The workspace connects a Vagrant-isolated agent to a suite of tools and language models operating on the host machine. 

### Core Components
- `/backup/clawd-workspace`: The unified state directory containing memories, active skills, configuration arrays, and context.
- `/backup/clawd/vagrant/microclaw`: The modern Rust-based agent operating system.
- `/backup/clawd/vagrant/openclaw`: The legacy Node.js-based agent operating system.

---

## 2. Managing the Agent VM (Microclaw)

The primary agent runs inside an isolated Vagrant Virtual Machine (Ubuntu 24.04). All commands interacting with the agent's core processes must be executed from the `microclaw` Vagrant directory.

**Standard Operating Commands:**
```bash
# Navigate to the Vagrant context
cd /backup/clawd/vagrant/microclaw

# Start the virtual machine
vagrant up

# Stop the virtual machine (Graceful Shutdown)
vagrant halt

# Access the isolated environment via SSH
vagrant ssh
```

### Checking Agent Health (Systemd)

Inside the VM, Microclaw is managed by systemd. You can inspect its real-time health using journalctl.

```bash
# SSH into the VM
cd /backup/clawd/vagrant/microclaw && vagrant ssh

# Check the real-time status of the gateway
systemctl status microclaw-gateway.service

# View the last 50 lines of logs for the LLM Gateway
journalctl -u microclaw-gateway.service -n 50 --no-pager

# Restart the Agent if it stops responding
sudo systemctl restart microclaw-gateway.service
```

### Configuration (microclaw.config.yaml)

Microclaw relies on a YAML configuration file to bypass its interactive setup and bind correctly to the host's models.

- **Path (Host):** `/backup/clawd/microclaw/microclaw.config.yaml`
- **Path (VM Linked):** `/home/vagrant/microclaw/microclaw.config.yaml`

To change the LLM Provider or API Key:
1. Open the file on your host machine.
2. Edit `llm_provider`, `api_key`, or `model`.
3. Restart the `microclaw-gateway.service` within the VM via `vagrant ssh`.

---

## 3. Network & Infrastructure Bridge

The agent VM relies heavily on an `autossh` tunnel (named `model-bridge.service`) to project its requests out to your local physical infrastructure (Manjaro) securely. 

### Checking the Tunnel
If Microclaw stops generating text or fails to hit embeddings, the bridge may have collapsed. 

```bash
# Check the tunnel status inside the VM
vagrant ssh -c 'systemctl status model-bridge.service'

# Restart the tunnel if it says 'FAILED'
vagrant ssh -c 'sudo systemctl restart model-bridge.service'
```

### Local Services (Docker Compose)
The actual LLMs, routers, and embedding vector databases run natively on your machine via Docker. 

**Working Directories:**
- `/backup/clawd-workspace/sovereign-lite-compose.yml` (Ollama & Orchestrator)
- `/backup/clawd-workspace/inference-compose.yml` (vLLM & RamaLlama)

**Commands to manage native models:**
```bash
# Navigate to the workspace
cd /backup/clawd-workspace

# Verify models are running
docker compose -f sovereign-lite-compose.yml ps

# Restart the entire sovereign network
docker compose -f sovereign-lite-compose.yml restart
```

---

## 4. Administration Quick Fixes

### Scenario: Gateway complains about SQLite / Directory Locks
If Microclaw fails to compile or start with an `os error 6 / No such device or address` related to the database:
- Ensure the Cargo Target Directory is strictly isolated from the Vagrant shared folder. (Check `Vagrantfile` for `CARGO_TARGET_DIR=/home/vagrant/cargo-target`).

### Scenario: SSH Port Forwarding Denied
If the VM cannot reach the `autossh` target:
- Verify that the host Machine (`10.0.2.2`) has the VM's SSH signature (`/home/vagrant/.ssh/id_rsa.pub`) mapped into your `~/.ssh/authorized_keys`.

### Scenario: Switching back to Openclaw
If you need to pivot back to the Node.js openclaw implementation:
1. Halt Microclaw: `cd /backup/clawd/vagrant/microclaw && vagrant halt`
2. Start Openclaw: `cd /backup/clawd/vagrant/openclaw && vagrant up`
*Note: They bind to the same host port (`18789`) and cannot run concurrently.*
