# Observability Stack: Netdata & Dozzle (Containerized)

Real-time monitoring of hardware vitals (VRAM, CPU heat, RAM bandwidth) is critical for managing a multi-agent swarm on 512GB of RAM.

## 1. Dozzle (Log Viewer)
Dozzle provides a lightweight, web-based interface to monitor the output of all agent and inference containers.

### `docker-compose.yml` Entry
```yaml
  dozzle:
    image: amir20/dozzle:latest
    container_name: sovereign-dozzle
    ports:
      - "8888:8080"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    restart: always
```
- **Access**: `http://localhost:8888` on the Host.

## 2. Netdata (Hardware Vitals)
Netdata monitors the Intel 8358P cores and the Nvidia A6000 VRAM in real-time.

### `docker-compose.yml` Entry
```yaml
  netdata:
    image: netdata/netdata:latest
    container_name: sovereign-netdata
    ports:
      - "19999:19999"
    cap_add:
      - SYS_PTRACE
    security_opt:
      - apparmor:unconfined
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /var/run/docker.sock:/var/run/docker.sock:ro
    restart: always
```
- **Access**: `http://localhost:19999` on the Host.

## 3. Agent Integration
The agent (Eliezer) can query the Netdata API to assess its own "Environmental Stress" (e.g., thermal throttling or VRAM saturation) and adjust the `intelligence-dispatcher` routing accordingly.
