# Study 02: Multi-Service Architecture & DevOps Basics

Welcome to your second study module! Now that you've explored basic Docker and Kubernetes deployments, we're going to level up.

## Project Goal
Build a **Hit Counter Application** that uses a Python API (Flask) and a Redis database. This will teach you how to handle:
1.  **Service-to-Service Communication**: How the API talks to Redis.
2.  **Configuration Management**: Using `ConfigMaps` for environment variables.
3.  **Secrets Management**: Safely handling database credentials (even if Redis is simple).
4.  **Health Checks**: Refining `Liveness` and `Readiness` probes.
5.  **Persistence**: Learning why databases need `StatefulSets` or `PersistentVolumes`.

## Roadmap
- [ ] **Step 1: Application Development** - Write a Flask app that connects to Redis.
- [ ] **Step 2: Containerization** - Create a multi-stage Dockerfile for the API.
- [ ] **Step 3: Local Orchestration** - Use `docker-compose` to test the stack locally.
- [ ] **Step 4: Kubernetes Deployment** - Deploy the stack to a K8s cluster (Minikube/Kind).
- [ ] **Step 5: GitOps with Argo CD** - Install Argo CD and automate deployments from a Git repo.
- [ ] **Step 6: Automation** - Write a Bash script to handle the build, tag, and deploy flow.

---

## Technical Stack
- **Language**: Python 3.11 (Flask)
- **Database**: Redis
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Scripting**: Bash

