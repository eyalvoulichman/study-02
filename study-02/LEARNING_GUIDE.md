# DevOps Learning Journey: Phase 1 (The Fundamentals)

This guide documents the step-by-step process we followed to build a professional GitOps-driven microservice architecture.

---

## 🏗️ Step 1: Application Development (The "What")
We started with a simple Python script using the **Flask** framework and a **Redis** database.
*   **The Goal**: Create a "Hit Counter" app.
*   **DevOps Concept**: **Microservices Architecture**. Instead of one giant program, we have two separate pieces: a Web API and a Database. They talk to each other over the network.
*   **Files**: `study-02/app.py`, `study-02/requirements.txt`.

## 📦 Step 2: Containerization (The "Package")
We wrote a `Dockerfile` to turn your code into a portable "Container Image."
*   **The Goal**: Ensure the app runs exactly the same on your laptop as it does on a server in the cloud.
*   **DevOps Concept**: **Multi-Stage Builds**. We used a "builder" stage to install tools and a "runtime" stage for the final app. This makes images smaller and more secure.
*   **Files**: `study-02/Dockerfile`.

## 🧪 Step 3: Local Orchestration (The "Test")
We used **Docker Compose** to run both the API and Redis together.
*   **The Goal**: Test the communication between services before going to the complex world of Kubernetes.
*   **DevOps Concept**: **Service Discovery**. We named the database `redis` in the compose file, and the Python app used that name to find it.
*   **Files**: `study-02/docker-compose.yaml`.

## ☸️ Step 4: Kubernetes Manifests (The "Instructions")
We moved from Docker to **Kubernetes (K8s)**, the industry standard for running containers at scale.
*   **The Goal**: Define exactly how many copies of the app we want and how to handle failures.
*   **DevOps Concepts**:
    *   **Deployments**: Manages the life of your containers (Self-healing).
    *   **Services**: Acts as a Load Balancer (NodePort for the API, ClusterIP for Redis).
    *   **ConfigMaps**: Keeps your settings (Ports, DB names) separate from your code.
*   **Files**: `study-02/k8s/api.yaml`, `study-02/k8s/redis.yaml`, `study-02/k8s/configmap.yaml`.

## 🤖 Step 5: GitOps with Argo CD (The "Autopilot")
We automated the deployment process using **Argo CD**.
*   **The Goal**: Make the cluster synchronize itself with GitHub automatically.
*   **DevOps Concept**: **GitOps (Truth in Git)**. Your GitHub repository is now the "Source of Truth." If you change a file in Git, Argo CD changes the cluster for you.
*   **Installation**: `study-02/install_argocd.sh`.

## 🏛️ Step 6: The "App of Apps" Pattern (The "Professional Way")
We organized the project into two separate repositories for better security and organization.
*   **The Goal**: Separate the "Application Code" from the "Deployment Config."
*   **DevOps Concept**: **Declarative Infrastructure**. We created a "Master App" that manages other apps. 
*   **Architecture**:
    *   **Repo 1 (`study-02`)**: The developers' repo (Code + K8s).
    *   **Repo 2 (`argocd`)**: The DevOps repo (Argo CD definitions).
*   **Files**: `argocd/root-app.yaml`, `argocd/apps/hit-counter-app.yaml`.

---

### 🛠 Summary of Commands Learned:

| Category | Command |
| :--- | :--- |
| **Docker Build** | `docker build -t hit-counter-api:latest .` |
| **Docker Compose** | `docker-compose up --build` |
| **K8s Pods** | `kubectl get pods` |
| **K8s Services** | `kubectl get svc api-service` |
| **Git Push** | `git add .`, `git commit -m "..."`, `git push` |
| **Argo Password**| `kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath='{.data.password}' \| base64 -d; echo` |

---

## 🚀 Phase 2 Preview: Continuous Integration (CI)
Our next goal is to automate the image building process using **GitHub Actions** or **GitLab CI**. Instead of building the image on your laptop, the Git platform will do it for you every time you push code!

