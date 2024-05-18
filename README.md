Django project skeleton to simplify project setup and help maintain a consistent project layout between projects

Example structure of a django project using this template:

```
└── git-repo/
    ├── .gitignore
    ├── poetry.lock
    ├── pyproject.toml
    ├── README.md
    └── src/
        ├── .env
        ├── manage.py
        ├── app/
        │   ├── <app-files>
        │   ├── api/
        │   │   ├── v1/
        │   │   └── v2/
        │   ├── migrations/
        │   ├── static/
        │   │   └── app/
        │   ├── templates/
        │   │   └── app/
        │   └── test/
        ├── <additional-apps>/
        └── config/
            ├── __init__.py
            ├── asgi.py
            ├── settings/
            │   ├── __init__.py
            │   ├── general.py
            │   ├── local.py
            │   └── <additional-settings-files>
            ├── urls.py
            └── wsgi.py
```
