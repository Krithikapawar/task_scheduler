# Beautiful Efficient Task Scheduler

## Overview
A visually appealing web-based task scheduler that allows users to input tasks dynamically, showing their execution order with priority-based Gantt bars.

## Setup
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open browser: http://127.0.0.1:8000

## Features
- Add tasks with priority, deadline, and dependencies
- Dynamic task table
- Color-coded Gantt chart visualization
