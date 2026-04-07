import logging

# Create logger
logging.basicConfig(
    filename='python.log',   # file output
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Also print to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s')
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

logging.info("🚀 Python Automation Started")

for i in range(3):
    logging.info(f"Step {i+1} executed")

logging.info("✅ Python Automation Completed")
