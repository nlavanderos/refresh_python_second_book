#pip install -i https://test.pypi.org/simple/ pc-info-setxh==1.0.0
from pc_info_setxh.example import PC_DATA

print(PC_DATA().ip)
print(PC_DATA().pcname)
print(PC_DATA().system)