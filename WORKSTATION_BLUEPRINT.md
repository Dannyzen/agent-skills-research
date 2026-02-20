# Sovereign Workstation Blueprint v3.1 🖊️🏗️🖥️

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
sudo pacman -S base-devel git podman nvidia-container-toolkit vagrant virtualbox docker-compose autossh

# 2. Configure NVIDIA Container Toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

### Phase II: Inference Engines (The Unified Swarm Strategy)
We utilize a tiered approach to maximize throughput and eliminate memory redundancy.

**A. vLLM-GPU (For 70B Strategist on A6000)**
- **Model**: `DeepSeek-R1-Distill-Llama-70B` (4-bit quantization)
- **Role**: Primary reasoning, strategy, and scholar.
- **Protocol**: Bind to `127.0.0.1:8000`. Use `gpu-memory-utilization 0.90`.

**B. vLLM-CPU (The Unified Swarm Batcher)**
- **Model**: `Llama-3.1-8B-Instruct`
- **Architecture**: Single model load with **Continuous Batching** and **PagedAttention**.
- **Role**: Serves 10+ concurrent swarm agents through a single port.
-Port: `8081`

**C. RamaLlama (For Specialist Tasks)**
- `Qwen-2.5-Coder-32B-Instruct` (Architect) - Port `8080`
- `Llama-3.2-11B-Vision` (Vision) - Port `8082`

### Phase III: Sovereign Infrastructure (Per-Container Setup)
Every infrastructure component runs in its own isolated container on the Manjaro host.

**A. Qdrant (Vector Database)**
- **Use**: High-performance semantic research.
- **Config**: See [QDRANT_SETUP.md](./skills/sovereign-intelligence-transmission/references/qdrant_setup.md)
- **Port**: `6333`

**B. Netdata (Real-time Vitals)**
- **Use**: Monitoring Intel 8358P cores and Nvidia A6000 VRAM/Heat.
- **Config**: See [OBSERVABILITY_SETUP.md](./skills/sovereign-intelligence-transmission/references/observability_setup.md)
- **Port**: `19999`

**C. Dozzle (Log Viewer)**
- **Use**: Live monitoring of container outputs.
- **Port**: `8888`

**D. Redis**: High-speed message bus for agent coordination.

---

## 3. The Agentic Harness (Vagrant VM)

The agent lives in an isolated Ubuntu sandbox, connecting to host models via an encrypted SSH bridge.

### Vagrantfile Configuration
```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-24.04"
  config.vm.network "forwarded_port", guest: 18789, host: 18789

  # DIRECT NVME MOUNT
  config.vm.synced_folder "/home/danny/clawd-workspace", "/home/vagrant/clawd", 
    type: "virtiofs", owner: "vagrant", group: "vagrant"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "32768" 
    vb.cpus = 8
    vb.customize ["modifyvm", :id, "--nictype1", "virtio"]
  end

  # Auto-provision SSH Tunnel to Host Infrastructure
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update && apt-get install -y autossh
    cat > /etc/systemd/system/model-bridge.service <<EOF
[Unit]
Description=AutoSSH Tunnel to Manjaro Infrastructure
After=network.target

[Service]
ExecStart=/usr/bin/autossh -M 0 -N -o "StrictHostKeyChecking no" \\
  -L 8000:127.0.0.1:8000 \\
  -L 8081:127.0.0.1:8081 \\
  -L 8080:127.0.0.1:8080 \\
  -L 6333:127.0.0.1:6333 \\
  -L 19999:127.0.0.1:19999 danny@10.0.2.2
Restart=always
User=vagrant

[Install]
WantedBy=multi-user.target
EOF
    systemctl enable model-bridge.service
  SHELL
end
```

---

## 4. Connectivity & Sovereignty
- **Isolation**: All inference and infrastructure APIs bind to `127.0.0.1` on the host. 
- **The Bridge**: Vagrant uses **AutoSSH** to map these host-only ports directly into the guest VM.
- **Teacher-Access**: Eliezer queries Port `19999` to monitor its own hardware health.

---
*Authored by Eliezer - Teacher of Teachers* 🖊️📜✨
