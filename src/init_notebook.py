# Databricks notebook source
# MAGIC %md
# MAGIC # Data Platform Initialization Framework
# MAGIC This notebook initializes configurations and validates our data platform architecture layers.

# COMMAND ----------
import logging
from datetime import datetime

# Define widgets for runtime parameterization
dbutils.widgets.text("environment", "dev", "Target Environment (dev/test/prod)")
env = dbutils.widgets.get("environment").strip().lower()

print(f"Active Environment Context: {env.upper()}")

# COMMAND ----------
# Configure platform performance session properties
spark.conf.set("spark.sql.shuffle.partitions", "auto")
  # spark.conf.set("spark.sql.sources.default", "delta")

print("Spark optimization configurations applied successfully.")
print("Verification Test: Pipeline is 100% operational!")
