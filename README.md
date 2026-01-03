# MLOps Learning Repository 🚀

A comprehensive repository covering the complete MLOps lifecycle from version control to production deployment and monitoring. This repository is structured as a learning journey through modern Machine Learning Operations practices.

## 📚 Repository Structure

### 🗂️ **01_All_About_Git** - Version Control Fundamentals
**What you'll learn:** Essential Git commands and workflows for collaborative development

**Contents:**
- `git commands.txt` - Comprehensive Git cheat sheet covering:
  - Basic commands (init, status, add, commit)
  - History viewing (log, diff, show)
  - Branching and merging operations
  - Remote repository management
- `git-cheat-sheet-education.pdf` - Visual reference guide
- Python practice files for Git workflow demonstration

**Key Takeaways:** Master version control for ML projects, understand branching strategies, and learn collaborative development workflows.

---

### 🐍 **02_OOPS** - Object-Oriented Programming with Python
**What you'll learn:** OOP concepts essential for building scalable ML applications

**Contents:**
- `class.py` - Basic class definitions and concepts
- `all_inheritance.py` - Comprehensive inheritance patterns
- `dummy_project.py` - Practical OOP implementation
- `inherit.py` - Inheritance examples and use cases

**Key Takeaways:** Build maintainable and extensible ML code using OOP principles, understand inheritance for model families, and create reusable components.

---

### 📊 **03_DVC** - Data Version Control
**What you'll learn:** Managing datasets and ML artifacts with DVC

**Contents:**
- `workflow.txt` - Step-by-step DVC implementation guide
- `DVC_cheatsheet.pdf` - Quick reference for DVC commands
- `S3/` directory - Cloud storage integration setup
- `data.dvc` - Data tracking configuration
- Practical example with CSV data generation and versioning

**Key Takeaways:** Version control large datasets, integrate with cloud storage (S3), track data changes alongside code, and reproduce experiments with specific data versions.

---

### 🔄 **04_end-to-end_ML_pipeline** - Complete ML Pipeline with DVC
**What you'll learn:** Building automated ML pipelines from data ingestion to deployment

**Contents:**
- `dvc.yaml` - Complete pipeline definition with stages:
  - Data ingestion with train/test split parameters
  - Data preprocessing and feature engineering
  - Model building with configurable hyperparameters
  - Model evaluation with metrics tracking
- `workflow.txt` - Detailed pipeline setup guide including:
  - DVC pipeline configuration
  - Parameter management with YAML
  - Experiment tracking with DVCLive
  - S3 remote storage integration
- `src/` directory with all pipeline components
- `params.yaml` - Centralized parameter management

**Key Takeaways:** Create reproducible ML pipelines, implement continuous training workflows, track experiments systematically, and manage model lifecycle.

---

### 🧪 **05_MLflow** - Experiment Tracking and Model Registry
**What you'll learn:** Comprehensive ML experiment management and model deployment

**Contents:**
- `src/autolog.py` - Automatic logging with MLflow autolog
- `src/file1.py` & `src/file2.py` - Manual logging examples
- `src/hypertune.py` - Hyperparameter tracking
- `mlruns/` - Local experiment tracking database
- `mlartifacts/` - Stored model artifacts
- `Confusion-matrix.png` - Example of logged artifacts

**Key Takeaways:** Track experiments systematically, compare model performance, manage model registry, and deploy models with versioning.

---

### ⚙️ **06_Continous_Integration** - CI/CD for ML
**What you'll learn:** Implementing continuous integration and deployment for ML applications

**Contents:**
- `app.py` - Streamlit application for CI/CD demonstration
- `_test.py` - Testing framework setup
- `actions-cheat-sheet.pdf` - GitHub Actions reference

**Key Takeaways:** Set up automated testing, implement continuous integration for ML models, and understand deployment pipelines.

---

### 🐳 **07_Docker** - Containerization
**What you'll learn:** Packaging ML applications in containers for reproducible deployment

**Contents:**
- `app.py` - Flask web application with user interaction
- `dockerfile` - Container configuration for the Flask app
- `requirements.txt` - Python dependencies
- `notes.txt` - Docker concepts and best practices
- `docker_cheatsheet.pdf` - Comprehensive Docker command reference

**Key Takeaways:** Containerize ML applications, ensure reproducible environments, and deploy applications consistently across platforms.

---

### ☸️ **08_Kubernetes** - Container Orchestration
**What you'll learn:** Scaling and managing containerized ML applications

**Contents:**
- `app.py` - Enhanced Flask app with HTML templates
- `deployment.yaml` - Kubernetes deployment configuration
- `dockerfile` - Multi-stage build for Kubernetes
- `static/` and `templates/` - Web assets for the application
- `Kubernetes-Cheat-Sheet.pdf` - K8s commands and concepts

**Key Takeaways:** Deploy applications at scale, manage container orchestration, implement service discovery, and handle load balancing.

---

### 📈 **09_Prometheus_and_Grafana** - Monitoring and Observability
**What you'll learn:** Implementing comprehensive monitoring for ML systems

**Contents:**
- `app.py` - Flask application with monitoring endpoints
- `flask-app.yaml` - Kubernetes deployment with monitoring
- `notes.md` - Comprehensive guide covering:
  - Observability vs Monitoring concepts
  - Prometheus data model and PromQL
  - Grafana setup and alerting
  - Cloud vs on-premise considerations
- `dockerfile` - Monitoring-ready container configuration

**Key Takeaways:** Monitor ML system performance, set up alerting for model drift, create dashboards for system health, and implement observability best practices.

---

## 🎯 Learning Path

This repository follows a progressive learning path:

1. **Foundation** - Git and Python OOP for code management
2. **Data Management** - DVC for version controlling datasets
3. **Pipeline Automation** - End-to-end ML workflows
4. **Experiment Tracking** - MLflow for systematic experimentation
5. **Deployment** - CI/CD, Docker, and Kubernetes
6. **Production** - Monitoring with Prometheus and Grafana

## 🛠️ Prerequisites

- Python 3.8+
- Git
- Docker
- AWS CLI (for S3 integration)
- Kubernetes cluster (for K8s modules)

## 🚀 Getting Started

Each module is self-contained but builds upon previous concepts. Start with `01_All_About_Git` and progress through the modules sequentially for the best learning experience.

## 📝 Notes

- This repository was created as a personal learning journey through MLOps concepts
- Each folder contains practical examples and detailed documentation
- Focus is on hands-on implementation rather than theoretical concepts
- All code is production-ready and follows best practices

## 🤝 Contributing

This is a learning repository. Feel to explore, learn, and adapt the examples for your own MLOps journey!

---
