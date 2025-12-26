# Argo CD & GitOps Practice Guide

To practice GitOps with the `hit-counter` app, follow these steps:

## 1. Create a GitHub/GitLab Repository
Argo CD works by watching a Git repository. You need to push your code there.
1. Create a new repository on GitHub (e.g., `study-devops`).
2. Run these commands in your terminal:
   ```bash
   git add .
   git commit -m "Initial commit of hit-counter app"
   git remote add origin https://github.com/YOUR_USERNAME/study-devops.git
   git push -u origin main
   ```

## 2. Configure the Argo CD Application
I've created a file at `study-02/k8s/argocd-app.yaml`.
1. Open that file and replace `https://github.com/YOUR_USERNAME/study-devops.git` with your actual repo URL.
2. Apply the application manifest:
   ```bash
   kubectl apply -f study-02/k8s/argocd-app.yaml
   ```

## 3. The "Magic" of GitOps
Once applied, Argo CD will:
1. See the definition in Git.
2. Automatically deploy the `ConfigMap`, `Redis`, and `API` to your cluster.
3. **Practice this**: Change the `replicas` in `study-02/k8s/api.yaml` from `2` to `4`, commit, and push. 
   - Watch the Argo CD UI: it will detect the "Out of Sync" state and automatically scale your pods!

## 4. Troubleshooting
- If Argo CD can't see your repo, check if it's Private. If it is, you'll need to add "Repository Credentials" in the Argo CD Settings UI.

