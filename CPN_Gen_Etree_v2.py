import xml.etree.ElementTree as ET
import random

count_y1 = '250'

count_y2 = '224'

count_y3 = '277'

root = ET.Element("workspaceElements")
name = "wtitle"
type = "RG"

def update_y(y1, y2, y3):
  global count_y1
  global count_y2
  global count_y3
  count_y1 = int(y1) - 50
  count_y2 = int(y2) - 50
  count_y3 = int(y3) - 50

  count_y1 = str(count_y1)
  count_y2 = str(count_y2)
  count_y3 = str(count_y3)


def generate_place(name, type, id):

  p1 = ET.SubElement(b37, "place")
  p1.set('id', id)
  p2 = ET.SubElement(p1, "posattr")
  p2.set('x', '0.000000')
  p2.set('y', count_y1)
  p3 = ET.SubElement(p1, "fillattr")
  p3.set('colour', 'White')
  p3.set('pattern', '')
  p3.set('filled', 'false')
  p4 = ET.SubElement(p1, "lineattr")
  p4.set('colour', 'Black')
  p4.set('thick', '1')
  p4.set('type', 'solid')
  p5 = ET.SubElement(p1, "textattr")
  p5.set('colour', 'Black')
  p5.set('bold', 'false')
  p6 = ET.SubElement(p1, "text")
  p6.text = name
  p7 = ET.SubElement(p1, "ellipse")
  p7.set('w', '75.000000')
  p7.set('h', '40.000000')
  p8 = ET.SubElement(p1, "token")
  p8.set('x', '-10.000000')
  p8.set('y', '0.000000')
  p9 = ET.SubElement(p1, "marking")
  p9.set('x', '0.000000')
  p9.set('y', '0.000000')
  p9.set('hidden', 'true')
  p10 = ET.SubElement(p9, "snap")
  p10.set('snap_id', '0')
  p10.set('anchor.horizontal', '0')
  p10.set('anchor.vertical', '0')
  
  id = update_id(id)
  
  p11 = ET.SubElement(p1, "type")
  p11.set('id', id)
  p12 = ET.SubElement(p11, "posattr")
  p12.set('x', '32.500000')
  p12.set('y', count_y2)
  p13 = ET.SubElement(p11, "fillattr")
  p13.set('colour', 'White')
  p13.set('pattern', 'Solid')
  p13.set('filled', 'false')
  p14 = ET.SubElement(p11, "lineattr")
  p14.set('colour', 'Black')
  p14.set('thick', '0')
  p14.set('type', 'Solid')
  p15 = ET.SubElement(p11, "textattr")
  p15.set('colour', 'Black')
  p15.set('bold', 'false')
  p16 = ET.SubElement(p11, "text")
  p16.set('tool', 'CPN Tools')
  p16.set('version', '4.0.1')
  p16.text = type

  id = update_id(id)

  p17 = ET.SubElement(p1, "initmark")
  p17.set('id', id)
  p18 = ET.SubElement(p17, "posattr")
  p18.set('x', '56.000000')
  p18.set('y', count_y3)
  p19 = ET.SubElement(p17, "fillattr")
  p19.set('colour', 'White')
  p19.set('pattern', 'Solid')
  p19.set('filled', 'false')
  p20 = ET.SubElement(p17, "lineattr")
  p20.set('colour', 'Black')
  p20.set('thick', '0')
  p20.set('type', 'Solid')
  p21 = ET.SubElement(p17, "textattr")
  p21.set('colour', 'Black')
  p21.set('bold', 'false')
  p22 = ET.SubElement(p17, "text")
  p22.set('tool', 'CPN Tools')
  p22.set('version', '4.0.1')

  update_y(count_y1, count_y2, count_y3)

#----#

m1 = ET.Element("generator")
root.append(m1)
m1.set('tool', 'CPN Tools')
m1.set('version', '4.0.1')
m1.set('format', '6')

m2 = ET.Element("cpnet")
root.append(m2)
b1 = ET.SubElement(m2, "globbox")
b2 = ET.SubElement(b1, "block")
b2.set('id', 'ID1412310166')

b3 = ET.SubElement(b2, "id")
b3.text = "Standard priorities"

b4 = ET.SubElement(b2, "ml")
b4.set('id', 'ID1412310255')
b4.text = "val P_HIGH = 100;"
b5 = ET.SubElement(b4, "layout")
b5.text = "val P_HIGH = 100;"

b6 = ET.SubElement(b2, "ml")
b6.set('id', 'ID1412310292')
b6.text = "val P_NORMAL = 1000;"
b7 = ET.SubElement(b6, "layout")
b7.text = "val P_NORMAL = 1000;"

b8 = ET.SubElement(b2, "ml")
b8.set('id', 'ID1412310322')
b8.text = "val P_LOW = 10000;"
b9 = ET.SubElement(b8, "layout")
b9.text = "val P_LOW = 10000;"

b10 = ET.SubElement(b1, "block")
b10.set('id', 'ID1')

b11 = ET.SubElement(b10, "id")
b11.text = "Standard declarations"

b12 = ET.SubElement(b10, "color")
b12.set('id', 'ID85042')
b13 = ET.SubElement(b12, "id")
b13.text = "UNIT"
b14 = ET.SubElement(b12, "unit")
b15 = ET.SubElement(b12, "layout")
b15.text = "colset UNIT = unit;"

b16 = ET.SubElement(b10, "color")
b16.set('id', 'ID4')
b17 = ET.SubElement(b16, "id")
b17.text = "BOOL"
b18 = ET.SubElement(b16, "bool")

b19 = ET.SubElement(b10, "color")
b19.set('id', 'ID3')
b20 = ET.SubElement(b19, "id")
b20.text = "INT"
b21 = ET.SubElement(b19, "int")

b22 = ET.SubElement(b10, "color")
b22.set('id', 'ID1412312409')
b23 = ET.SubElement(b22, "id")
b23.text = "INTINF"
b24 = ET.SubElement(b22, "intinf")
b25 = ET.SubElement(b22, "layout")
b25.text = "colset INTINF = intinf;"

b26 = ET.SubElement(b10, "color")
b26.set('id', 'ID1412312425')
b27 = ET.SubElement(b26, "id")
b27.text = "TIME"
b28 = ET.SubElement(b26, "time")
b29 = ET.SubElement(b26, "layout")
b29.text = "colset TIME = time;"

b30 = ET.SubElement(b10, "color")
b30.set('id', 'ID1412322990')
b31 = ET.SubElement(b30, "id")
b31.text = "REAL"
b32 = ET.SubElement(b30, "real")
b33 = ET.SubElement(b30, "layout")
b33.text = "colset REAL = real;"

b34 = ET.SubElement(b10, "color")
b34.set('id', 'ID5')
b35 = ET.SubElement(b34, "id")
b35.text = "STRING"
b36 = ET.SubElement(b34, "string")

bcorrect = ET.SubElement(b10, "color")
bcorrect.set('id', 'ID1415410128')
bcorrect2 = ET.SubElement(bcorrect, "id")
bcorrect2.text = "RG"
bcorrect3 = ET.SubElement(bcorrect, "alias")
bcorrect4 = ET.SubElement(bcorrect3, "id")
bcorrect4.text = "INT"
bcorrect5 = ET.SubElement(bcorrect, "layout")
bcorrect5.text = "colset RG = INT;"

b37 = ET.SubElement(m2, "page")
b37.set('id', 'ID6')
b38 = ET.SubElement(b37, "pageattr")
b38.set('name', 'New Page')

#---#

b39 = ET.SubElement(m2, "instances")

b40 = ET.SubElement(b39, "instance")
b40.set('id', 'ID2149')
b40.set('page', 'ID6')

#---#

b41 = ET.SubElement(m2, "options")

#---#

b42 = ET.SubElement(b41, "option")
b42.set('name', 'realtimestamp')

b43 = ET.SubElement(b42, "value")

b44 = ET.SubElement(b43, "boolean")
b44.text = "false"

#---#

b45 = ET.SubElement(b41, "option")
b45.set('name', 'fair_be')

b46 = ET.SubElement(b45, "value")

b47 = ET.SubElement(b46, "boolean")
b47.text = "false"

#---#

b48 = ET.SubElement(b41, "option")
b48.set('name', 'global_fairness')

b49 = ET.SubElement(b48, "value")

b50 = ET.SubElement(b49, "boolean")
b50.text = "false"

#---#

b51 = ET.SubElement(b41, "option")
b51.set('name', 'outputdirectory')

b52 = ET.SubElement(b51, "value")

b53 = ET.SubElement(b52, "text")
b53.text = "&lt;same as model&gt;"

#---#

b54 = ET.SubElement(b41, "option")
b54.set('name', 'extensions.10002.enable')

b55 = ET.SubElement(b54, "value")

b56 = ET.SubElement(b55, "boolean")
b56.text = "true"

#---#

b57 = ET.SubElement(b41, "option")
b57.set('name', 'extensions.10005.enable')

b58 = ET.SubElement(b57, "value")

b59 = ET.SubElement(b58, "boolean")
b59.text = "true"

#---#

b60 = ET.SubElement(b41, "option")
b60.set('name', 'extensions.10003.enable')

b61 = ET.SubElement(b60, "value")

b62 = ET.SubElement(b61, "boolean")
b62.text = "true"

#---#

b63 = ET.SubElement(b41, "option")
b63.set('name', 'extensions.10006.enable')

b64 = ET.SubElement(b63, "value")

b65 = ET.SubElement(b64, "boolean")
b65.text = "true"

#---#

b66 = ET.SubElement(b41, "option")
b66.set('name', 'extensions.10001.enable')

b67 = ET.SubElement(b66, "value")

b68 = ET.SubElement(b67, "boolean")
b68.text = "true"

#---#

b69 = ET.SubElement(b41, "option")
b69.set('name', 'repavg')

b70 = ET.SubElement(b69, "value")

b71 = ET.SubElement(b70, "boolean")
b71.text = "true"

#---#

b72 = ET.SubElement(b41, "option")
b72.set('name', 'repciavg')

b73 = ET.SubElement(b72, "value")

b74 = ET.SubElement(b73, "boolean")
b74.text = "true"

#---#

b75 = ET.SubElement(b41, "option")
b75.set('name', 'repfirstval')

b76 = ET.SubElement(b75, "value")

b77 = ET.SubElement(b76, "boolean")
b77.text = "false"

#---#

b78 = ET.SubElement(b41, "option")
b78.set('name', 'replastval')

b79 = ET.SubElement(b78, "value")

b80 = ET.SubElement(b79, "boolean")
b80.text = "false"

#---#

b81 = ET.SubElement(b41, "option")
b81.set('name', 'repmax')

b82 = ET.SubElement(b81, "value")

b83 = ET.SubElement(b82, "boolean")
b83.text = "true"

#---#

b84 = ET.SubElement(b41, "option")
b84.set('name', 'repmin')

b85 = ET.SubElement(b84, "value")

b86 = ET.SubElement(b85, "boolean")
b86.text = "true"

#---#

b87 = ET.SubElement(b41, "option")
b87.set('name', 'repssquare')

b88 = ET.SubElement(b87, "value")

b89 = ET.SubElement(b88, "boolean")
b89.text = "false"

#---#

b90 = ET.SubElement(b41, "option")
b90.set('name', 'repsquare')

b91 = ET.SubElement(b90, "value")

b92 = ET.SubElement(b91, "boolean")
b92.text = "false"

#---#

b93 = ET.SubElement(b41, "option")
b93.set('name', 'repssqdev')

b94 = ET.SubElement(b93, "value")

b95 = ET.SubElement(b94, "boolean")
b95.text = "false"

#---#

b96 = ET.SubElement(b41, "option")
b96.set('name', 'repstddev')

b97 = ET.SubElement(b96, "value")

b98 = ET.SubElement(b97, "boolean")
b98.text = "true"

#---#

b99 = ET.SubElement(b41, "option")
b99.set('name', 'repsum')

b100 = ET.SubElement(b99, "value")

b101 = ET.SubElement(b100, "boolean")
b101.text = "false"

#---#

b102 = ET.SubElement(b41, "option")
b102.set('name', 'repvariance')

b103 = ET.SubElement(b102, "value")

b104 = ET.SubElement(b103, "boolean")
b104.text = "false"

#---#

b105 = ET.SubElement(b41, "option")
b105.set('name', 'avg')

b106 = ET.SubElement(b105, "value")

b107 = ET.SubElement(b106, "boolean")
b107.text = "true"

#---#

b108 = ET.SubElement(b41, "option")
b108.set('name', 'ciavg')

b109 = ET.SubElement(b108, "value")

b110 = ET.SubElement(b109, "boolean")
b110.text = "false"

#---#

b111 = ET.SubElement(b41, "option")
b111.set('name', 'count')

b112 = ET.SubElement(b111, "value")

b113 = ET.SubElement(b112, "boolean")
b113.text = "true"

#---#

b114 = ET.SubElement(b41, "option")
b114.set('name', 'firstval')

b115 = ET.SubElement(b114, "value")

b116 = ET.SubElement(b115, "boolean")
b116.text = "false"

#---#

b117 = ET.SubElement(b41, "option")
b117.set('name', 'lastval')

b118 = ET.SubElement(b117, "value")

b119 = ET.SubElement(b118, "boolean")
b119.text = "false"

#---#

b120 = ET.SubElement(b41, "option")
b120.set('name', 'max')

b121 = ET.SubElement(b120, "value")

b122 = ET.SubElement(b121, "boolean")
b122.text = "true"

#---#

b123 = ET.SubElement(b41, "option")
b123.set('name', 'min')

b124 = ET.SubElement(b123, "value")

b125 = ET.SubElement(b124, "boolean")
b125.text = "true"

#---#

b126 = ET.SubElement(b41, "option")
b126.set('name', 'ssquare')

b127 = ET.SubElement(b126, "value")

b128 = ET.SubElement(b127, "boolean")
b128.text = "false"

#---#

b129 = ET.SubElement(b41, "option")
b129.set('name', 'ssqdev')

b130 = ET.SubElement(b129, "value")

b131 = ET.SubElement(b130, "boolean")
b131.text = "false"

#---#

b132 = ET.SubElement(b41, "option")
b132.set('name', 'stddev')

b133 = ET.SubElement(b132, "value")

b134 = ET.SubElement(b133, "boolean")
b134.text = "false"

#---#

b135 = ET.SubElement(b41, "option")
b135.set('name', 'sum')

b136 = ET.SubElement(b135, "value")

b137 = ET.SubElement(b136, "boolean")
b137.text = "false"

#---#

b138 = ET.SubElement(b41, "option")
b138.set('name', 'variance')

b139 = ET.SubElement(b138, "value")

b140 = ET.SubElement(b139, "boolean")
b140.text = "false"

#---#

b141 = ET.SubElement(b41, "option")
b141.set('name', 'firstupdate')

b142 = ET.SubElement(b141, "value")

b143 = ET.SubElement(b142, "boolean")
b143.text = "false"

#---#

b144 = ET.SubElement(b41, "option")
b144.set('name', 'interval')

b145 = ET.SubElement(b144, "value")

b146 = ET.SubElement(b145, "boolean")
b146.text = "false"

#---#

b147 = ET.SubElement(b41, "option")
b147.set('name', 'lastupdate')

b148 = ET.SubElement(b147, "value")

b149 = ET.SubElement(b148, "boolean")
b149.text = "false"

#---#

b150 = ET.SubElement(b41, "option")
b150.set('name', 'untimedavg')

b151 = ET.SubElement(b150, "value")

b152 = ET.SubElement(b151, "boolean")
b152.text = "true"

#---#

b153 = ET.SubElement(b41, "option")
b153.set('name', 'untimedciavg')

b154 = ET.SubElement(b153, "value")

b155 = ET.SubElement(b154, "boolean")
b155.text = "false"

#---#

b156 = ET.SubElement(b41, "option")
b156.set('name', 'untimedcount')

b157 = ET.SubElement(b156, "value")

b158 = ET.SubElement(b157, "boolean")
b158.text = "true"

#---#

b159 = ET.SubElement(b41, "option")
b159.set('name', 'untimedfirstval')

b160 = ET.SubElement(b159, "value")

b161 = ET.SubElement(b160, "boolean")
b161.text = "false"

#---#

b162 = ET.SubElement(b41, "option")
b162.set('name', 'untimedlastval')

b163 = ET.SubElement(b162, "value")

b164 = ET.SubElement(b163, "boolean")
b164.text = "false"

#---#

b165 = ET.SubElement(b41, "option")
b165.set('name', 'untimedmax')

b166 = ET.SubElement(b165, "value")

b167 = ET.SubElement(b166, "boolean")
b167.text = "true"

#---#

b168 = ET.SubElement(b41, "option")
b168.set('name', 'untimedmin')

b169 = ET.SubElement(b168, "value")

b170 = ET.SubElement(b169, "boolean")
b170.text = "true"

#---#

b171 = ET.SubElement(b41, "option")
b171.set('name', 'untimedssquare')

b172 = ET.SubElement(b171, "value")

b173 = ET.SubElement(b172, "boolean")
b173.text = "false"

#---#

b174 = ET.SubElement(b41, "option")
b174.set('name', 'untimedssqdev')

b175 = ET.SubElement(b174, "value")

b176 = ET.SubElement(b175, "boolean")
b176.text = "false"

#---#

b177 = ET.SubElement(b41, "option")
b177.set('name', 'untimedstddev')

b178 = ET.SubElement(b177, "value")

b179 = ET.SubElement(b178, "boolean")
b179.text = "false"

#---#

b180 = ET.SubElement(b41, "option")
b180.set('name', 'untimedsum')

b181 = ET.SubElement(b180, "value")

b182 = ET.SubElement(b181, "boolean")
b182.text = "true"

#---#

b183 = ET.SubElement(b41, "option")
b183.set('name', 'untimedvariance')

b184 = ET.SubElement(b183, "value")

b185 = ET.SubElement(b184, "boolean")
b185.text = "false"

#---#

b186 = ET.SubElement(m2, "binders")

b187 = ET.SubElement(b186, "cpnbinder")
b187.set('id', 'ID2222')
b187.set('x', '335')
b187.set('y', '94')
b187.set('width', '1353')
b187.set('height', '738')

b188 = ET.SubElement(b187, "sheets")

b189 = ET.SubElement(b188, "cpnsheet")
b189.set('id', 'ID2215')
b189.set('panx', '0.000000')
b189.set('pany', '-63.000000')
b189.set('zoom', '1.000000')
b189.set('instance', 'ID2149')

b190 = ET.SubElement(b189, "zorder")

b191 = ET.SubElement(b190, "position")
b191.set('value', '0')

b192 = ET.SubElement(b187, "zorder")

b193 = ET.SubElement(b192, "position")
b193.set('value', '0')

#---#

b194 = ET.SubElement(m2, "monitorblock")
b194.set('name', 'Monitors')

#---# 3

b195 = ET.SubElement(m2, "IndexNode")
b195.set('expanded', 'true')

b196 = ET.SubElement(b195, "IndexNode")
b196.set('expanded', 'false')

b197 = ET.SubElement(b195, "IndexNode")
b197.set('expanded', 'false')

b198 = ET.SubElement(b195, "IndexNode")
b198.set('expanded', 'false')

#---# 5

b199 = ET.SubElement(b198, "IndexNode")
b199.set('expanded', 'false')

b200 = ET.SubElement(b198, "IndexNode")
b200.set('expanded', 'false')

b201 = ET.SubElement(b198, "IndexNode")
b201.set('expanded', 'false')

b202 = ET.SubElement(b198, "IndexNode")
b202.set('expanded', 'false')

b203 = ET.SubElement(b198, "IndexNode")
b203.set('expanded', 'false')

#---#

b204 = ET.SubElement(b203, "IndexNode")
b204.set('expanded', 'false')

#---# 15

b205 = ET.SubElement(b204, "IndexNode")
b205.set('expanded', 'false')

b206 = ET.SubElement(b205, "IndexNode")
b206.set('expanded', 'false')

b207 = ET.SubElement(b205, "IndexNode")
b207.set('expanded', 'false')

b208 = ET.SubElement(b205, "IndexNode")
b208.set('expanded', 'false')

b209 = ET.SubElement(b205, "IndexNode")
b209.set('expanded', 'false')

b210 = ET.SubElement(b205, "IndexNode")
b210.set('expanded', 'false')

b211 = ET.SubElement(b205, "IndexNode")
b211.set('expanded', 'false')

b212 = ET.SubElement(b205, "IndexNode")
b212.set('expanded', 'false')

b213 = ET.SubElement(b205, "IndexNode")
b213.set('expanded', 'false')

b214 = ET.SubElement(b205, "IndexNode")
b214.set('expanded', 'false')

b215 = ET.SubElement(b205, "IndexNode")
b215.set('expanded', 'false')

b216 = ET.SubElement(b205, "IndexNode")
b216.set('expanded', 'false')

b217 = ET.SubElement(b205, "IndexNode")
b217.set('expanded', 'false')

b218 = ET.SubElement(b205, "IndexNode")
b218.set('expanded', 'false')

b219 = ET.SubElement(b205, "IndexNode")
b219.set('expanded', 'false')

b220 = ET.SubElement(b205, "IndexNode")
b220.set('expanded', 'false')

#---# 12 

b221 = ET.SubElement(b204, "IndexNode")
b221.set('expanded', 'false')

b222 = ET.SubElement(b221, "IndexNode")
b222.set('expanded', 'false')

b223 = ET.SubElement(b221, "IndexNode")
b223.set('expanded', 'false')

b224 = ET.SubElement(b221, "IndexNode")
b224.set('expanded', 'false')

b225 = ET.SubElement(b221, "IndexNode")
b225.set('expanded', 'false')

b226 = ET.SubElement(b221, "IndexNode")
b226.set('expanded', 'false')

b227 = ET.SubElement(b221, "IndexNode")
b227.set('expanded', 'false')

b228 = ET.SubElement(b221, "IndexNode")
b228.set('expanded', 'false')

b229 = ET.SubElement(b221, "IndexNode")
b229.set('expanded', 'false')

b230 = ET.SubElement(b221, "IndexNode")
b230.set('expanded', 'false')

b231 = ET.SubElement(b221, "IndexNode")
b231.set('expanded', 'false')

b232 = ET.SubElement(b221, "IndexNode")
b232.set('expanded', 'false')

b233 = ET.SubElement(b221, "IndexNode")
b233.set('expanded', 'false')

#---# 12

b234 = ET.SubElement(b203, "IndexNode")
b234.set('expanded', 'false')

b235 = ET.SubElement(b234, "IndexNode")
b235.set('expanded', 'false')

b236 = ET.SubElement(b234, "IndexNode")
b236.set('expanded', 'false')

b237 = ET.SubElement(b234, "IndexNode")
b237.set('expanded', 'false')

b238 = ET.SubElement(b234, "IndexNode")
b238.set('expanded', 'false')

b239 = ET.SubElement(b234, "IndexNode")
b239.set('expanded', 'false')

b240 = ET.SubElement(b234, "IndexNode")
b240.set('expanded', 'false')

b241 = ET.SubElement(b234, "IndexNode")
b241.set('expanded', 'false')

b242 = ET.SubElement(b234, "IndexNode")
b242.set('expanded', 'false')

b243 = ET.SubElement(b234, "IndexNode")
b243.set('expanded', 'false')

b244 = ET.SubElement(b234, "IndexNode")
b244.set('expanded', 'false')

b245 = ET.SubElement(b234, "IndexNode")
b245.set('expanded', 'false')

b246 = ET.SubElement(b234, "IndexNode")
b246.set('expanded', 'false')

#---# 5

b247 = ET.SubElement(b198, "IndexNode")
b247.set('expanded', 'false')

b248 = ET.SubElement(b247, "IndexNode")
b248.set('expanded', 'false')

b249 = ET.SubElement(b247, "IndexNode")
b249.set('expanded', 'false')

b250 = ET.SubElement(b247, "IndexNode")
b250.set('expanded', 'false')

b251 = ET.SubElement(b247, "IndexNode")
b251.set('expanded', 'false')

b252 = ET.SubElement(b247, "IndexNode")
b252.set('expanded', 'false')

#---# 2

b253 = ET.SubElement(b195, "IndexNode")
b253.set('expanded', 'false')

b254 = ET.SubElement(b195, "IndexNode")
b254.set('expanded', 'true')

#---# 3

b255 = ET.SubElement(b254, "IndexNode")
b255.set('expanded', 'false')

b256 = ET.SubElement(b255, "IndexNode")
b256.set('expanded', 'true')

b257 = ET.SubElement(b255, "IndexNode")
b257.set('expanded', 'true')

b258 = ET.SubElement(b255, "IndexNode")
b258.set('expanded', 'true')

#---# 8

b259 = ET.SubElement(b254, "IndexNode")
b259.set('expanded', 'true')

b260 = ET.SubElement(b259, "IndexNode")
b260.set('expanded', 'false')

b261 = ET.SubElement(b259, "IndexNode")
b261.set('expanded', 'false')

b262 = ET.SubElement(b259, "IndexNode")
b262.set('expanded', 'false')

b263 = ET.SubElement(b259, "IndexNode")
b263.set('expanded', 'false')

b264 = ET.SubElement(b259, "IndexNode")
b264.set('expanded', 'false')

b265 = ET.SubElement(b259, "IndexNode")
b265.set('expanded', 'false')

b266 = ET.SubElement(b259, "IndexNode")
b266.set('expanded', 'true')

b267 = ET.SubElement(b259, "IndexNode")
b267.set('expanded', 'true')

#---# 2

b268 = ET.SubElement(b195, "IndexNode")
b268.set('expanded', 'false')

b269 = ET.SubElement(b195, "IndexNode")
b269.set('expanded', 'true')

#Código principal do projeto Mapeamento de Esquemas Moise para Redes de Petri

# Importação de bibliotecas
# import xml.dom.minidom

# # Função que faz a leitura do arquivo XML
# def read_xml(archive):
#     document = xml.dom.minidom.parse(archive)
#     return document

# # Função que faz a separação dos grupos contidos no documento XML
# def get_groups(document, file):
#     groups = document.getElementsByTagName("group-specification")
    
#     for element in groups:
#         print(element)
#         gp = element.getAttribute("id")
#         # print("\nGroup: %s" % (gp))
#         file.write("\n{\n")
#         file.write("Group: %s" % (gp))
    
#         roles = element.getElementsByTagName("role")
#         for role in roles:
#             role_id = role.getAttribute("id")
#             role_min = role.getAttribute("min")
#             role_max = role.getAttribute("max")
#             # print("role: %s " % (role_id))
#             # print("min: %s " % (role_min))
#             # print("max: %s " % (role_max))
#             file.write("\n role: %s, " % (role_id))
#             file.write("min: %s, " % (role_min))
#             file.write("max: %s" % (role_max))
#         file.write("\n}\n")

#     return file
# # Função que faz a separação dos planos contidos no documento XML
# def get_plans(document, file, list):
#     plans = document.getElementsByTagName("plan")
#     plans.reverse()
    
#     for element in plans:
#         op = element.getAttribute("operator")
#         # print("\nOperator: %s" % (op))
#         file.write("\n{\n")
#         file.write("Operator: %s" % (op))
    
#         goals = element.getElementsByTagName("goal")
#         for goal in goals:
#             goal_id = goal.getAttribute("id")
#             file.write("\n goal: %s" % (goal_id))
#             list.append(goal_id)
#             element.removeChild(goal)
#         file.write("\n}\n")    
    
#     goals = document.getElementsByTagName("goal")[0]
#     first = goals.getAttribute("id")
#     # print("\nInitial goal: %s" % (first))
#     file.write("\nFirst goal: %s" % (first))
#     list.append(first)

#     return file, list

def create_id():
  id = "ID" + str(random.randint(1000000000, 9999999990))
  return id

def update_id(id):
  last_two_digits = id[-2:]
  if last_two_digits == '99':
    id = id[:-2] + '00'
  else:
    id = id[:-1] + str(int(id[-1]) + 1)
  return id

# # Execução das funções
# file = open("structures.xml", "w")
# goals = ['start']
# document = read_xml("wp.xml")
# file = get_groups(document, file)
# file, goals = get_plans(document, file, goals)
# print(goals)
# size = len(goals)
# file.close()

import xml.dom.minidom

# Função que limpa os nós de texto e novas linhas deixando só os nodos de interesse [goals e plans]
def clear_node(branch):
    n = 0
    while n < len(branch):
        if branch[n].nodeName == "#text":
            branch[n].parentNode.removeChild(branch[n])
        n+=1
    return branch

class Missions():
    def __init__(self, data):
        self.data = data
        self.mission = None

def find_mission(goal):
    mission = ""
    for i in range(0, len(goals_missions)):
        for j in range(0, len(goals_missions[i])):
            if goals_missions[i][j].data.getAttribute("id") == goal.getAttribute("id"):
                # print(" Mission: ", goals_missions[i][j].mission)
                mission = goals_missions[i][j].mission[:4]
    return str(mission)

# document = xml.dom.minidom.parse("ST_new_2.xml") # Faz a leitura do arquivo Soccer Team XML
document = xml.dom.minidom.parse("wp.xml") # Faz a leitura do arquivo Write Paper XML

node = document.getElementsByTagName("goal")

visited = []

goal = document.getElementsByTagName("goal")[0] # Pega o primeiro nodo goal
root_tree = goal # Armazena o primeiro goal que será o nodo raiz da árvore

missions = document.getElementsByTagName("mission") # Pega todos os nodos mission
goals_missions = []

for i in range(0, len(missions)):
    browser = []
    clear_node(missions[i].childNodes)
    for j in range(0, len(missions[i].childNodes)):
        current = Missions(missions[i].childNodes[j])
        current.mission = missions[i].getAttribute("id")
        browser.append(current)
    goals_missions.append(browser)

n = 0

while n < len(node):
    if (node[n].parentNode.nodeName != "plan" and node[n].parentNode.nodeName != "scheme"):
        node[n].parentNode.removeChild(node[n])
    n+=1

node = root_tree

# Leitura da Árvora Funcionando

id = create_id()
generate_place("start", "BOOL", id)

while True:
    if node.hasChildNodes() == True:
        clear_node(node.childNodes)
        node = node.childNodes[0]
    elif node.hasChildNodes() == False:
        if (node.nodeName == "goal"):
            print("* Leu o Nó: {}".format(node.getAttribute("id")))
            id = create_id()
            if (find_mission(node) == ""):
                string = node.getAttribute("id")
            else:
                string = node.getAttribute("id") + "\n(" + find_mission(node) + ")"
            print(string)
            generate_place(string, "RG", id)
        elif (node.nodeName == "plan"):
            print("* Leu o Plano: {}".format(node.getAttribute("operator")))
        parent = node.parentNode # Armazena o nodo pai
        node.parentNode.removeChild(node) # Remove o nodo atual
        node = parent
    if root_tree.hasChildNodes() == False:
        id = create_id()
        if (find_mission(node) == ""):
                string = node.getAttribute("id")
        else:
            string = node.getAttribute("id") + "\n(" + find_mission(node) + ")"
        print(string)
        generate_place(string, "RG", id)
        print ("* Fim da árvore")
        id = create_id()
        generate_place("end", "BOOL", id)
        break

# for i in range(size):
#   id = create_id()
#   generate_place(goals[i], "RG", id)

tree = ET.ElementTree(root)
ET.indent(tree, space="\t", level=0)
with open("CPN_Test.cpn", "wb") as files:
  tree.write(files, encoding="utf-8")