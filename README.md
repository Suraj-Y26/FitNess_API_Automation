# FitNesse + Python API Automation Framework

A professional, object-oriented API test automation framework integrating the **FitNesse Wiki Server** with a **Python 3.12+** backend via the **SLIM protocol** (`waferslim`). 

This framework demonstrates automated integration tests against the standard user CRUD endpoints of **[ReqRes.in](https://reqres.in)**.

---

## 1. Project Architecture

The system operates in a clean, decoupled layered design matching enterprise test automation standards:

```
FitNesse Wiki (Web UI)
      └── High-level test tables using SLIM syntax
              │
              ▼
Python Fixture Layer (fixtures/)
      └── UserFixture (extends BaseFixture)
      └── Receives Wiki arguments, delegates to services, exposes results
              │
              ▼
Service Layer (services/)
      └── UserService (extends BaseService)
      └── Invokes REST API calls using 'requests', manages exceptions
              │
              ▼
Utilities & Config (utils/)
      └── Structured logging, rotating log files, environmental config
              │
              ▼
Target REST API (https://reqres.in)
```

---

## 2. Directory Structure

```text
FitNessePythonFramework/
├── fitnesse-standalone.jar     # Pre-loaded FitNesse standalone server
├── FitNesseRoot/               # Wiki root directory
│   └── UserTests/              # Suite containing all user tests
│       ├── content.txt         # Suite configurations (imports, paths, patterns)
│       ├── properties.xml      # Suite metadata (Suite flag)
│       ├── GetUser/            # GET /users/2 test page
│       ├── CreateUser/         # POST /users test page
│       ├── UpdateUser/         # PUT /users/2 test page
│       └── DeleteUser/         # DELETE /users/2 test page
├── fixtures/                   # Fixture Layer (bridge to FitNesse)
│   ├── base_fixture.py         # Response and status tracking base class
│   └── user_fixture.py         # Maps Wiki script tables to service methods
├── services/                   # Service Layer (Business logic & API client)
│   ├── base_service.py         # HTTP client wrapper, error handling, logging
│   └── user_service.py         # User-specific CRUD operations
├── utils/                      # Helper modules
│   ├── config.py               # Centralized configuration (timeouts, endpoints)
│   └── logger.py               # Rotating file and console logger
├── testdata/                   # Test data storage
│   └── users.json              # Static test profiles
├── tests/                      # Python unit tests
│   └── test_user_service.py    # Local pytest suite to verify services
├── logs/                       # Log directory
│   └── framework.log           # Rotation log output
├── requirements.txt            # Python dependencies
├── README.md                   # Project overview (this file)
└── run_fitnesse.md             # Execution and integration explanation
```

---

## 3. Implemented Endpoints & Features

This framework covers the 4 main HTTP CRUD operations:

| HTTP Method | Endpoint | Description | Expected Status |
| :--- | :--- | :--- | :--- |
| **GET** | `/api/users/2` | Retrieve user details | `200` |
| **POST** | `/api/users` | Create a new user record | `201` |
| **PUT** | `/api/users/2` | Update user properties | `200` |
| **DELETE** | `/api/users/2` | Remove user record | `204` |

### Key Code Patterns Included:
*   **Object-Oriented Programming (OOP)**: Clear separation of concerns with `BaseService`, `UserService`, `BaseFixture`, and `UserFixture`.
*   **Robust Exception Handling**: Prevents abrupt server crashes by handling connection errors and timeouts natively.
*   **Type Hints & Docstrings**: Comprehensive typing annotations and inline code documentation following PEP 8.
*   **Centralized Logging**: Automatic request-response logger tracking HTTP headers, verbs, and payload contents.
*   **Mock/Free Fallback Support**: Centralized endpoint switching inside `utils/config.py` using `API_PREFIX` so tests can run without paid keys against the free open sandbox.

---

## 4. Quick Start

### Step 4.1: Installation
Ensure you have **Python 3.12+** and **Java 8+** (for FitNesse) installed on your system.

```powershell
# 1. Create a virtual environment
python -m venv .venv

# 2. Activate virtual environment
.venv\Scripts\Activate.ps1

# 3. Install required packages
pip install -r requirements.txt
```

### Step 4.2: Running Local Unit Tests (Optional)
Ensure the Python backend is communicating successfully with ReqRes:
```powershell
# Configure Python Path
$env:PYTHONPATH="C:\FitNessePythonFramework"

# Run pytest (If you do not have an API key, tests will fail with 401. Set REQRES_API_KEY env var)
.venv\Scripts\pytest.exe
```

### Step 4.3: Running FitNesse
Launch the server effortlessly on Windows by running our automated batch script:
```powershell
.\start_server.bat
```
Please see [run_fitnesse.md](./run_fitnesse.md) for full details on running the FitNesse suite, understanding the SLIM socket execution mechanism, and configuring your free ReqRes API Key.
