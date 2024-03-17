
import pandas as pd

# 定义数据库表和它们的字段
table_data = {
    "UploadRecords": {
        "columns": ["字段名", "数据类型", "描述"],
        "data": [
            ["UploadID", "INT", "主键，上传记录的唯一标识"],
            ["UserID", "INT", "外键，上传用户的ID"],
            ["FileName", "VARCHAR", "上传文件名"],
            ["FilePath", "VARCHAR", "文件在服务器上的存储路径"],
            ["UploadTime", "DATETIME", "文件上传时间"],
            ["Status", "VARCHAR", "上传后的状态（如“待处理”、“处理中”、“完成”）"]
        ]
    },
    "ProcessingTasks": {
        "columns": ["字段名", "数据类型", "描述"],
        "data": [
            ["TaskID", "INT", "主键，任务的唯一标识"],
            ["UploadID", "INT", "外键，对应的上传记录ID"],
            ["TaskType", "VARCHAR", "任务类型（如“去噪”、“重采样”、“DEM生成”等）"],
            ["StartTime", "DATETIME", "任务开始时间"],
            ["EndTime", "DATETIME", "任务结束时间"],
            ["Status", "VARCHAR", "任务状态（如“进行中”、“完成”、“失败”）"],
            ["ResultPath", "VARCHAR", "处理结果存储路径"]
        ]
    },
    "DataProducts": {
        "columns": ["字段名", "数据类型", "描述"],
        "data": [
            ["ProductID", "INT", "主键，数据产品的唯一标识"],
            ["TaskID", "INT", "外键，生成该产品的任务ID"],
            ["Type", "VARCHAR", "数据产品类型（如“DEM”、“DSM”、“CHM”）"],
            ["FilePath", "VARCHAR", "数据文件存储路径"],
            ["CreationTime", "DATETIME", "数据产品生成时间"]
        ]
    },
    "UserFeedback": {
        "columns": ["字段名", "数据类型", "描述"],
        "data": [
            ["FeedbackID", "INT", "主键，反馈的唯一标识"],
            ["UserID", "INT", "外键，提供反馈的用户ID"],
            ["FeedbackType", "VARCHAR", "反馈类型（如“数据质量”、“系统建议”等）"],
            ["Content", "TEXT", "反馈内容"],
            ["SubmitTime", "DATETIME", "反馈提交时间"]
        ]
    },
    "Users": {
        "columns": ["字段名", "数据类型", "描述"],
        "data": [
            ["UserID", "INT", "主键，用户的唯一标识"],
            ["Username", "VARCHAR", "用户名"],
            ["Password", "VARCHAR", "密码，存储时加密处理"],
            ["Role", "VARCHAR", "用户角色（如“管理员”、“普通用户”等）"]
        ]
    },
    "AccessControl": {
        "columns": ["字段名", "数据类型", "描述"],
        "data": [
            ["AccessID", "INT", "主键，访问控制记录的唯一标识"],
            ["UserID", "INT", "外键，用户ID"],
            ["ProductID", "INT", "外键，数据产品ID"],
            ["Permission", "VARCHAR", "访问权限（如“读”、“写”、“无”）"]
        ]
    }
}

# 创建并写入Excel文件
output_path = "数据交互.xlsx"
with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
    for table_name, table_info in table_data.items():
        df = pd.DataFrame(table_info["data"], columns=table_info["columns"])
        df.to_excel(writer, sheet_name=table_name, index=False)

print(f"数据库表格架构已经保存到 '{output_path}'")
