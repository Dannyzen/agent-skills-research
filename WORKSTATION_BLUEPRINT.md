# Sovereign Workstation Blueprint v1.1 🖊️🏗️🖥️

This document provides the definitive implementation plan for a high-performance AI Agent Sanctuary on bare-metal hardware.

## 1. Hardware Specifications
- **Host OS**: Manjaro Linux (Arch-based)
- **CPU**: Intel 8358P (32 Cores / 64 Threads)
- **RAM**: 512GB DDR4
- **GPU**: Nvidia RTX A6000 (48GB VRAM)
- **Storage**: 2x U.2 3.84TB NVMe Drives

---

## 2. Host Configuration (Manjaro)

### Phase I: Driver & Tooling Stack
```bash
# 1. Update and Install Core Dependencies
sudo pacman -Syu
sudo pacman -S base-devel git podman nvidia-container-toolkit vagrant virtualbox docker-compose

# 2. Configure NVIDIA Container Toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

### Phase II: Inference Engines (Dual-Engine Strategy)
**A. vLLM (For 70B Strategist on GPU)**
- **Model**: `DeepSeek-R1-Distill-Llama-70B` (4-bit quantization)
- **Role**: Primary reasoning, strategy, and scholar.
- **Port**: `8000`

**B. RamaLlama (For Workers & Action)**
- **Role**: High-speed task execution, coding, and vision.
- **Models**:
  - `Qwen-2.5-Coder-32B-Instruct` (Architect) - Port `8080`
  - `Llama-3.2-11B-Vision` (Vision) - Port `8082`
  - `Llama-3.1-8B-Instruct` (Swarm) - Multiple ports

### Phase III: Advanced Observability & Memory
To manage 512GB of RAM and a dozen agents, we need high-fidelity monitoring and scalable memory.

**A. Qdrant (Vector Database)**
- **Use**: Replacing SQLite for large-scale semantic research.
- **Benefit**: Near-instant search across millions of documents.

**B. Open WebUI**
- **Use**: A local, human-friendly interface to all models.
- **Access**: `http://localhost:3000` on the Host.

**C. Netdata / Dozzle**
- **Use**: Real-time VRAM/RAM monitoring and container log tracking.

### Phase IV: Swarm Coordination (The Message Bus)
**A. Redis**
- **Use**: High-speed message bus for 20+ agents to coordinate tasks and share state without file-system lag.

### Phase V: Model Context Protocol (MCP) Integration
- **Harness Expansion**: Run a suite of local **MCP Servers** (Filesystem, Git, Search) on the host. 
- **Benefit**: Allows the agent in the VM to take secure, authorized actions on the host machine.

---

## 3. The Agentic Harness (Vagrant VM)

### Vagrantfile Configuration
```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/noble64"
  config.vm.network "forwarded_port", guest: 18789, host: 18789

  # Shared Intelligence Database (On U.2 NVMe)
  config.vm.synced_folder "./memory", "/home/vagrant/clawd/memory"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "16384"
    vb.cpus = 8
    vb.customize ["modifyvm", :id, "--nictype1", "virtio"]
  end
end
```

---

## 4. Connectivity & Sovereignty
- **Internal Pipe**: Agent (VM) talks to Host (Manjaro) via `http://10.0.2.2:[PORT]`.
- **Remote Bridge**: **Tailscale** installed on the Host for secure remote access.
- **Local DNS**: **AdGuard Home** (Container) to ensure all model traffic remains 100% local.

---
*Authored by Eliezer - Teacher of Teachers* 🖊️📜✨
