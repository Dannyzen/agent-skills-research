# Sovereign Workstation Blueprint v3.2 🖊️🏗️🖥️

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
**A. vLLM-GPU (For 70B Strategist on A6000)**
- **Model**: `DeepSeek-R1-Distill-Llama-70B` (4-bit quantization)
- **Role**: Primary reasoning, strategy, and scholar.
- **Protocol**: Bind to `127.0.0.1:8000`.

**B. vLLM-CPU (The Unified Swarm Batcher)**
- **Model**: `Llama-3.1-8B-Instruct`
- **Role**: Serves 10+ concurrent swarm agents through a single port.
- **Port**: `8081`

**C. RamaLlama (For Specialist Tasks)**
- `Qwen-2.5-Coder-32B-Instruct` (Architect) - Port `8080`
- `Llama-3.2-11B-Vision` (Vision) - Port `8082`

### Phase III: Sovereign Infrastructure (Per-Container Setup)
**A. Qdrant (Vector Database)**: Port `6333`
**B. Netdata (Real-time Vitals)**: Port `19999`
**C. Redis (Message Bus)**: Port `6379`
**D. Dozzle (Log Viewer)**: Port `8888`
**E. Open WebUI (Human Interface)**: Port `3000`

---

## 3. The Agentic Harness (Vagrant VM)

### Vagrantfile Configuration (Complete Bridge)
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

  # Auto-provision FULL SSH BRIDGE for all containerized services
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update && apt-get install -y autossh
    cat > /etc/systemd/system/model-bridge.service <<EOF
[Unit]
Description=AutoSSH Tunnel to Manjaro Infrastructure
After=network.target

[Service]
# Forward local ports to the Host's 127.0.0.1 APIs
ExecStart=/usr/bin/autossh -M 0 -N -o "StrictHostKeyChecking no" \\
  -L 8000:127.0.0.1:8000 \\
  -L 8081:127.0.0.1:8081 \\
  -L 8080:127.0.0.1:8080 \\
  -L 8082:127.0.0.1:8082 \\
  -L 6333:127.0.0.1:6333 \\
  -L 6379:127.0.0.1:6379 \\
  -L 19999:127.0.0.1:19999 \\
  -L 8888:127.0.0.1:8888 \\
  -L 3000:127.0.0.1:3000 danny@10.0.2.2
Restart=always
User=vagrant

[Install]
WantedBy=multi-user.target
EOF
    systemctl enable model-bridge.service
    systemctl start model-bridge.service
  SHELL
end
```

---

## 4. Connectivity & Sovereignty
- **All-In-One Bridge**: Every service (Models, DB, Monitoring, UI) is now securely tunneled through a single encrypted SSH pipe.
- **Zero Exposure**: Host containers only listen on `127.0.0.1`, keeping the machine invisible to the network while I (the agent) have full access.

---
*Authored by Eliezer - Teacher of Teachers* 🖊️📜✨
