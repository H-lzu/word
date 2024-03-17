# Re-import the pandas library and redefine the schema for each table after code execution state reset
import pandas as pd

# Define the schema for each table again
tables_schema = {
    "CrownDetections": [
        {"Field": "DetectionID", "Type": "INT", "Description": "主键，树冠检测记录的唯一标识"},
        {"Field": "PointCloudID", "Type": "INT", "Description": "点云数据的唯一标识"},
        {"Field": "Position", "Type": "GEOMETRY", "Description": "树冠的空间位置（如使用GIS坐标）"},
        {"Field": "Area", "Type": "FLOAT", "Description": "树冠面积"},
        {"Field": "Height", "Type": "FLOAT", "Description": "树冠高度"},
        {"Field": "DetectionTime", "Type": "DATETIME", "Description": "检测时间"}
    ],
    "TreeBoundaries": [
        {"Field": "BoundaryID", "Type": "INT", "Description": "主键，树木边界记录的唯一标识"},
        {"Field": "DetectionID", "Type": "INT", "Description": "对应的树冠检测记录ID"},
        {"Field": "Boundary", "Type": "GEOMETRY", "Description": "树木边界的空间表示（如多边形）"},
        {"Field": "ExtractionTime", "Type": "DATETIME", "Description": "边界提取时间"}
    ],
    "PointCloudClusters": [
        {"Field": "ClusterID", "Type": "INT", "Description": "主键，点云聚类结果的唯一标识"},
        {"Field": "BoundaryID", "Type": "INT", "Description": "对应的树木边界记录ID"},
        {"Field": "PointCloud", "Type": "TEXT", "Description": "分割出的树木点云数据"},
        {"Field": "ClusterTime", "Type": "DATETIME", "Description": "聚类时间"}
    ],
    "SingleTreeModels": [
        {"Field": "ModelID", "Type": "INT", "Description": "主键，单木模型的唯一标识"},
        {"Field": "ClusterID", "Type": "INT", "Description": "对应的点云聚类结果ID"},
        {"Field": "ModelData", "Type": "TEXT", "Description": "三维模型数据"},
        {"Field": "ReconstructionTime", "Type": "DATETIME", "Description": "模型重建时间"}
    ],
    "TreeAttributes": [
        {"Field": "AttributeID", "Type": "INT", "Description": "主键，树木属性记录的唯一标识"},
        {"Field": "ModelID", "Type": "INT", "Description": "对应的单木模型ID"},
        {"Field": "Height", "Type": "FLOAT", "Description": "树高"},
        {"Field": "CrownWidth", "Type": "FLOAT", "Description": "冠幅"},
        {"Field": "TrunkDiameter", "Type": "FLOAT", "Description": "树干直径"},
        {"Field": "CalculationTime", "Type": "DATETIME", "Description": "属性计算时间"}
    ]
}

# Prepare the data for each table to create an Excel document with detailed schemas for all tables
with pd.ExcelWriter("单木分割数据库表.xlsx", engine="xlsxwriter") as writer:
    for table_name, fields in tables_schema.items():
        df = pd.DataFrame(fields)
        df.to_excel(writer, sheet_name=table_name, index=False)

