# 🚀 整合式服務專案 (Flask & C# 微服務架構)

本專案包含兩個主要服務：負責檔案與圖片處理的 Python 服務 (`uploadimg`)，以及負責核心業務邏輯的 C# 服務。兩者皆整合了 GitLab CI/CD 自動化流水線，並支援透過 Kubernetes (K8s) 進行現代化叢集部署。



## 🛠️ 服務說明 (Services Overview)

### 1. 🖼️ uploadimg 專案 (Python)
* **核心功能**：基於 Python/Flask 開發，主要處理前端檔案與圖片上傳。
* **CI/CD 整合**：代碼推送至 GitLab 後，自動執行 Docker 鏡像建置並推送到 Registry。

### 2. ⚡ C# 專案
* **核心功能**：主要業務邏輯基於 C# 開發，並在內部的 `python/` 目錄中內嵌了 Python 腳本，用以執行特定的 Python 相關任務與數據功能。
* **CI/CD 整合**：擁有獨立的 GitLab CI/CD 流程，支援自動化編譯、打包 Docker 鏡像與版本更新。

---

## 🔄 GitLab CI/CD 自動化流程

兩個專案各自的 `.gitlab-ci.yml` 設定檔中，均包含以下核心階段 (Stages)：

1. **Build (建置階段)**：
   * 自動讀取 `Dockerfile`。
   * 封裝應用程式並建置成 Docker Image（例如：`docker build -t <registry_url>/<image_name>:$CI_COMMIT_SHA .`）。
2. **Push (推送階段)**：
   * 將建置完成的 Image 推送至專屬的 Docker Registry。
3. **Deploy / Update (更新階段)**：
   * 透過指令自動更新 K8s 叢集中的鏡像版本，實現無縫滾動更新 (Rolling Update)。

---

## ☸️ Kubernetes (K8s) 部署說明

專案內提供的 `deployment.yaml`（測試用 YAML）用於將打包好的服務部署至 K8s 叢集。

### 部署步驟：

1. **確保已連接至 K8s 叢集**（確認 `kubectl` 環境已就緒）。
2. **執行部署指令**：
   ```bash
   kubectl apply -f k8s/deployment.yaml
   ```
3. **檢查部署狀態**：
   ```bash
   kubectl get deployment
   kubectl get pods
   ```

---

## 🌐 Nginx 反向代理進入點設定

若需透過外層 Nginx 將流量分流至 K8s 服務或本機 Container，請在 `/etc/nginx/conf.d/default.conf` 中配置：

```nginx
server {
    listen       80;
    server_name  localhost;

    # 轉發至 Python 圖片上傳服務
    location ^~/upload/ {
        proxy_pass http://127.0.0;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
```
*修改完成後請執行 `nginx -s reload` 重新載入設定。*

