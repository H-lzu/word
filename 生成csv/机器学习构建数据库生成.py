# Re-import pandas after execution state reset
import pandas as pd

# Redefine the schema for each table with descriptions for thesis writing, and create the Excel document again
tables_schema_with_descriptions = {
    "DatasetInfo": {
        "columns": ["字段名", "数据类型", "描述"],
        "data": [
            ["DatasetID", "INT", "主键，数据集的唯一标识"],
            ["DatasetName", "VARCHAR", "数据集名称"],
            ["Source", "VARCHAR", "数据来源（GEE）"],
            ["AcquisitionDate", "DATE", "数据获取日期"],
            ["Resolution", "FLOAT", "空间分辨率"],
            ["Coverage", "VARCHAR", "数据覆盖区域"],
            ["Description", "TEXT", "数据集描述"]
        ],
        "description": "数据集信息表用于记录和管理从Google Earth Engine（GEE）平台获取的遥感数据集的详细信息，为碳储量估算提供基础数据。"
    },
    "FeatureInfo": {
        "columns": ["字段名", "数据类型", "描述"],
        "data": [
            ["FeatureID", "INT", "主键，特征的唯一标识"],
            ["DatasetID", "INT", "外键，关联的数据集ID"],
            ["FeatureName", "VARCHAR", "特征名称"],
            ["FeatureType", "VARCHAR", "特征类型（如植被指数、地形特征等）"],
            ["CalculationMethod", "VARCHAR", "计算方法"],
            ["Description", "TEXT", "特征描述"]
        ],
        "description": "特征信息表记录了从遥感数据中提取的特征信息，包括特征名称、类型、提取方法及描述，为模型训练提供关键输入。"
    },
    "ModelTrainingRecords": {
        "columns": ["字段名", "数据类型", "描述"],
        "data": [
            ["TrainingID", "INT", "主键，训练记录的唯一标识"],
            ["ModelName", "VARCHAR", "模型名称"],
            ["FeaturesUsed", "TEXT", "使用的特征（JSON格式）"],
            ["Parameters", "TEXT", "模型参数（JSON格式）"],
            ["PerformanceMetrics", "TEXT", "性能指标（如R²、MSE，JSON格式）"],
            ["TrainingDate", "DATETIME", "训练日期"]
        ],
        "description": "模型训练记录表详细记录了模型的训练过程，包括使用的特征、参数配置、性能指标及训练时间，支持模型的评估和优化。"
    },
    "ModelEvaluationResults": {
        "columns": ["字段名", "数据类型", "描述"],
        "data": [
            ["EvaluationID", "INT", "主键，评估记录的唯一标识"],
            ["TrainingID", "INT", "外键，关联的模型训练记录ID"],
            ["TestDatasetID", "INT", "外键，使用的测试数据集ID"],
            ["Metrics", "TEXT", "评估指标结果（如R²、MSE，JSON格式）"],
            ["EvaluationDate", "DATETIME", "评估日期"]
        ],
        "description": "模型评估结果表为模型提供了一个客观的性能评价，记录了模型在独立测试集上的表现指标和评估时间，有助于判断模型的泛化能力。"
    }
}

# Create the Excel document with detailed schemas and descriptions for all tables
output_path = "ForestMLModel_TablesSchemaWithDescriptions.xlsx"
with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
    for table_name, info in tables_schema_with_descriptions.items():
        df = pd.DataFrame(info["data"], columns=info["columns"])
        df.to_excel(writer, sheet_name=table_name, index=False)
        # Adding a sheet for table description
        df_description = pd.DataFrame([info["description"]], columns=["Description"])
        df_description.to_excel(writer, sheet_name=f"{table_name}_Desc", index=False)


