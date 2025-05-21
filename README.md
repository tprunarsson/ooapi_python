# OOAPI Python Courses Example

This repo demonstrates a minimal FastAPI implementation of an OOAPI-style `/courses` endpoint using legacy-style data.

## Quickstart

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. (Optional) Create test data
python seed.py

# 3. Run the server
uvicorn main:app --reload

# 4. See docs
# Open http://127.0.0.1:8000/docs in your browser

