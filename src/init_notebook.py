# Databricks notebook source
# MAGIC %md
# MAGIC # Data Platform Initialization Framework
# MAGIC **Author:** Platform Architecture Team  
# MAGIC **Environment:** Enterprise Data Pipeline Base Initialization  
# MAGIC 
# MAGIC This notebook sets up global session configurations, dynamic parameter widgets, logging contexts, and validates connections to storage infrastructure layers.

# COMMAND ----------
# MAGIC %md
# MAGIC ### Step 1: Define Runtime Parameters & Widgets

# COMMAND ----------
import logging
from datetime import datetime

# Initialize text widgets for control-flow parameters
dbutils.widgets.text("environment", "dev", "Target Environment (dev/test/prod)")
dbutils.widgets.text("run_date", datetime.utcnow().strftime("%Y-%m-%d"), "Data Run Date (YYYY-MM-DD)")

# Retrieve values into native Python variables
env = dbutils.widgets.get("environment").strip().lower()
run_date_str = dbutils.widgets.get("run_date").strip()

# COMMAND ----------
# MAGIC %md
# MAGIC ### Step 2: Configure System Logging & Governance Metadata

# COMMAND ----------
# Set up standard platform-wide structured logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("platform_init")

# Build a global metadata payload for downstream table heritage/lineage tracking
platform_metadata = {
    "environment": env,
    "execution_date": run_date_str,
    "initialized_at": datetime.utcnow().isoformat(),
    "spark_version": spark.conf.get("spark.databricks.clusterUsageTags.sparkVersion", "unknown"),
    "cluster_id": spark.conf.get("spark.databricks.clusterUsageTags.clusterId", "unknown")
}

logger.info(f"Successfully initialized platform metadata registry for environment: {env.upper()}")
print(f"Platform Run Metadata:\n{platform_metadata}")

# COMMAND ----------
# MAGIC %md
# MAGIC ### Step 3: Global Spark Session Optimizations

# COMMAND ----------
# Inject base optimizations for Delta Lake performance and structural governance
spark.conf.set("spark.sql.shuffle.partitions", "auto")
spark.conf.set("spark.databricks.delta.preview.enabled", "true")
spark.conf.set("spark.sql.sources.default", "delta")

# Enforce strict layout constraints for enterprise storage schema tracking
spark.conf.set("spark.databricks.delta.schema.autoMerge.enabled", "false") 

logger.info("Spark session optimizations and Delta engine constraints applied.")

# COMMAND ----------
# MAGIC %md
# MAGIC ### Step 4: Storage Landing Zone Connectivity Validation

# COMMAND ----------
try:
    logger.info("Validating access constraints against platform storage architecture...")
    
    # Testing access to Unity Catalog or native DBFS mounts
    # Replace '/' with your specific Unity Catalog catalog pathway if using UC (e.g., f
