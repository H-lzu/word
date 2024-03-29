import pandas as pd

# 1. RegionFeatureLayers表
region_feature_layers = {
    "字段名": ["LayerID", "RegionID", "FeatureType", "RasterData", "CreationDate"],
    "数据类型": ["int", "int", "str", "str", "date"],
    "字段描述": ["唯一标识一个特征图层的ID","区域标识符","特征类型(例如:植被指数、土壤湿度等)","图层的栅格数据位置","数据创建日期"]
}
rf_df = pd.DataFrame(region_feature_layers)
rf_df.to_csv("RegionFeatureLayers.csv", index=False, encoding="utf-8")

# 2. CarbonStorageEstimations表
carbon_storage_estimations = {
    "字段名": ["EstimationID", "RegionID", "StorageDataLocation", "EstimationDate", "ModelVersion"],
    "数据类型": ["int", "int", "str", "date", "str"],
    "字段描述": ["唯一标识一个碳储量估算结果","区域标识符,与RegionFeatureLayers的RegionID关联","估算的碳储量结果文件(TIF)的位置","估算日期","使用的模型版本"]
}
cse_df = pd.DataFrame(carbon_storage_estimations)
cse_df.to_csv("CarbonStorageEstimations.csv", index=False, encoding="utf-8")

# 3. CarbonStorageServices表
carbon_storage_services = {
    "字段名": ["ServiceID", "EstimationID", "WMSURL", "AccessType", "CreationDate"],
    "数据类型": ["int", "int", "str", "str", "date"],
    "字段描述": ["唯一标识一个共享服务","碳储量估算结果的标识符,与CarbonStorageEstimations的EstimationID关联","提供碳储量估算结果的WMS服务URL","访问类型(例如:公开、私有)","服务创建日期"]
}
css_df = pd.DataFrame(carbon_storage_services)
css_df.to_csv("CarbonStorageServices.csv", index=False, encoding="utf-8")