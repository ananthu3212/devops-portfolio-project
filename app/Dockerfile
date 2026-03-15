# ===== STAGE 1: What base image to use =====
FROM python:3.11-slim

# ===== STAGE 2: Who is maintaining this =====
LABEL maintainer="ananthu@example.com"
LABEL description="DevOps Portfolio Application for Junior DevOps Role"

# ===== STAGE 3: Set working directory inside container =====
WORKDIR /app

# ===== STAGE 4: Copy requirements first (for caching) =====
COPY requirements.txt .

# ===== STAGE 5: Install dependencies =====
RUN pip install --no-cache-dir -r requirements.txt

# ===== STAGE 6: Copy the rest of the application =====
COPY . .

# ===== STAGE 7: Expose port 5000 =====
EXPOSE 8080

# ===== STAGE 8: Command to run when container starts =====
CMD ["python", "app.py"]