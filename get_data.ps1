Invoke-WebRequest https://zenodo.org/record/1161203/files/data.tar.gz -o data.tar.gz
tar -xzf data.tar.gz
uv sync 
uv run process.py