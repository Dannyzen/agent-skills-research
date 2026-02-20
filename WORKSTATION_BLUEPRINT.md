# Sovereign Workstation Blueprint v2.3 🖊️🏗️🖥️

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

### Phase II: Inference Engines (Dual-Engine Strategy)
**A. vLLM (For 70B Strategist on GPU)**
- **Model**: `DeepSeek-R1-Distill-Llama-70B` (4-bit quantization)
- **Role**: Primary reasoning, strategy, and scholar.
- **Access**: Bind to `127.0.0.1:8000` (Secure, access via SSH tunnel).

**B. RamaLlama (For Workers & Action)**
- **Role**: High-speed task execution, coding, and vision.
- **Models**:
  - `Qwen-2.5-Coder-32B-Instruct` (Architect) - Port `8080`
  - `Llama-3.2-11B-Vision` (Vision) - Port `8082`
  - `Llama-3.1-8B-Instruct` (Swarm) - Port `8081`

### Phase III: Advanced Observability & Memory
**A. Qdrant (Vector Database)**
- **Use**: High-performance semantic research. Bind to `127.0.0.1:6333`.

**B. Open WebUI**
- **Use**: Local interface for manual testing. Port `3000`.

**C. Netdata / Dozzle**
- **Use**: Real-time VRAM/RAM monitoring and container logs.

### Phase IV: Swarm Coordination & Control
**A. Redis**: High-speed message bus for agent coordination.
**B. MCP Servers**: Run local Model Context Protocol servers on host for Filesystem/Git access.

---

## 3. The Agentic Harness (Vagrant VM)

The agent lives in an isolated Ubuntu sandbox, connecting to host models via an encrypted SSH bridge.

### Vagrantfile Configuration
```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-24.04"
  config.vm.network "forwarded_port", guest: 18789, host: 18789

  # Direct NVMe Workspace Sync
  config.vm.synced_folder "/home/danny/clawd-workspace", "/home/vagrant/clawd", 
    type: "virtiofs", owner: "vagrant", group: "vagrant"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "32768"
    vb.cpus = 8
    vb.customize ["modifyvm", :id, "--nictype1", "virtio"]
  end

  # Auto-provision SSH Tunnel
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update && apt-get install -y autossh
    # Set up systemd service for persistent port forwarding
    cat > /etc/systemd/system/model-bridge.service <<EOF
[Unit]
Description=AutoSSH Tunnel to Manjaro Models
After=network.target

[Service]
ExecStart=/usr/bin/autossh -M 0 -N -o "StrictHostKeyChecking no" -L 8000:127.0.0.1:8000 danny@10.0.2.2
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

## 4. Connectivity & Security
- **The Vault**: All inference APIs bind to `127.0.0.1` on host. No external access.
- **The Bridge**: Vagrant uses **AutoSSH** to tunnel `localhost:8000` to the host.
- **Remote**: **Tailscale** on host for secure remote management.

---
*Authored by Eliezer - Teacher of Teachers* 🖊️📜✨
