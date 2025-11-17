from email.policy import default
from pathlib import Path
import pandas as pd
import tarfile
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
from sklearn.base import BaseEstimator
from sklearn.metrics.pairwise import rbf_kernel

# 显示所有列
pd.set_option('display.max_columns', None)
# 可以根据需要调整列宽
pd.set_option('display.max_colwidth', None)  # 不限制列宽
pd.set_option('display.width', 1000)  # 调整显示宽度
np.set_printoptions(precision=3,suppress= True,threshold=np.inf,linewidth=1000)
def load_housing_data():
    tarball_path = Path("datasets/housing.tgz")
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, tarball_path)
    with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets",filter = 'data')
    return pd.read_csv(Path("datasets/housing/housing.csv"))

housing = load_housing_data()
# print(housing.head())
# print(housing.info())
# print(housing['ocean_proximity'].values_count())
# 设置matplotlib图表的字体和标签大小配置
plt.rc('font', size=14)              # 控制字体基本大小
plt.rc('axes', labelsize=14, titlesize=14)  # 控制坐标轴标签和标题大小
plt.rc('legend', fontsize=14)        # 控制图例字体大小
plt.rc('xtick', labelsize=10)        # 控制x轴刻度标签大小
plt.rc('ytick', labelsize=10)        # 控制y轴刻度标签大小
# 绘制住房数据集中各数值属性的直方图，bins参数指定每个直方图的柱子数量为50，figsize参数指定图像大小为12x8英寸
housing.hist(bins=50, figsize=(12, 8))
# plt.show()
#plt.show()

#region[用纯随机采样的方式划分训练集和测试集]
def shuffle_and_split_data(data, test_ratio):
    """
    随机打乱数据并按比例分割成训练集和测试集
    
    参数:
    data: 需要分割的DataFrame数据
    test_ratio: 测试集所占比例
    
    返回:
    train_set, test_set: 分别为训练集和测试集的DataFrame
    """
    # 生成随机排列的索引数组，用于打乱数据
    shuffled_indices = np.random.permutation(len(data))
    
    # 计算测试集的大小（取整数）
    test_set_size = int(len(data) * test_ratio)
    
    # 取前test_set_size个索引作为测试集索引
    test_indices = shuffled_indices[:test_set_size]
    
    # 剩余的索引作为训练集索引
    train_indices = shuffled_indices[test_set_size:]
    
    # 根据索引分别选取训练集和测试集数据并返回
    return data.iloc[train_indices], data.iloc[test_indices]
#将20%的数据集划分成训练集和测试集
# train_set, test_set = shuffle_and_split_data(housing, 0.2)  #生成训练集和测试集
# print('训练集数据量：',len(train_set),'测试集数据量：',len(test_set))


# 导入crc32函数，用于创建稳定的测试集分割
# crc32是一种哈希算法，可以为相同的输入产生一致的哈希值
# 这样可以确保每次运行代码时，相同的数据总是被分到相同的集合中
from zlib import crc32

def is_id_in_test_set(identifier, test_ratio):
    """
    检测哈希值是否在测试集里面
    """
    return crc32(np.int64(identifier)) < test_ratio * 2**32

def split_data_with_id_hash(data, test_ratio, id_column):
    """
    用哈希值来分类数据，一类为测试集，一类为训练集
    """
    # 提取数据中指定ID列的所有值
    ids = data[id_column]
    
    # 对每个ID应用is_id_in_test_set函数，判断是否应该分配到测试集
    # 结果是一个布尔序列，True表示对应ID应该在测试集中
    # 对每个ID应用is_id_in_test_set函数，判断是否应该分配到测试集
    # apply()方法将lambda函数应用于ids序列中的每个元素
    # lambda id_: is_id_in_test_set(id_, test_ratio)是一个匿名函数，接收一个id_参数
    # 并调用is_id_in_test_set函数判断该id是否应该在测试集中
    # 最终返回一个布尔序列，True表示对应的ID应该在测试集中
    in_test_set = ids.apply(lambda id_: is_id_in_test_set(id_, test_ratio))
    
    # 使用布尔索引分离训练集和测试集：
    # ~in_test_set表示不在测试集中的样本（即训练集）
    # in_test_set表示在测试集中的样本
    return data.loc[~in_test_set], data.loc[in_test_set]

# housing_with_id = housing.reset_index() # 添加索引列，这个索引列默认名称为Index,这里将原housing数据集改造为了新的housing_with_id
# #相当于train_set=data.loc[~in_test_set],test_set=data.loc[in_test_set]
# train_set, test_set = split_data_with_id_hash(housing_with_id, 0.2, "index")#分割训练集和测试集
# print(train_set.head())
#不使用哈希值作为标识符的替代办法：自己选一个最稳定的特征来构建唯一标识符：
# housing_with_id['id'] = housing['longitude'] * 1000 + housing['latitude']
# train_set, test_set = split_data_with_id_hash(housing_with_id, 0.2, "id")

from sklearn.model_selection import train_test_split
#也可以直接用scikit-learn的train_test_split函数来划分数据集与训练集，其效果和上面自定义的shuffle_and_split_data()一样
# train_set,test_set = train_test_split(housing, test_size=0.2, random_state=42)
#endregion

#region[用分层抽样的方法来划分测试集和训练集]
#由于经验得知，收入对于房价的重要性很高，因此需保证训练数据的收入水平分布与测试集的分布相似，故要以收入水平为基准进行分层抽烟
#由于收入是连续函数，需先将它分割成不同区间以分类。pandas的cut()函数就可以做到这件事
#将收入根据设置的bins分成5个类别
housing['income_cat'] = pd.cut(housing['median_income'],bins=[0.,1.5,3.0,4.5,6.,np.inf],labels=[1,2,3,4,5])
#
# #创建一个显示不同收入类别数量分布的条形图，x轴标签水平显示，并带有网格线以方便查看数据。
# housing["income_cat"].value_counts().sort_index().plot.bar(rot=0, grid=True)
# plt.xlabel("Income category")
# plt.ylabel("Number of districts")
# plt.show()

from sklearn.model_selection import StratifiedShuffleSplit
#选择StratifiedShuffleSplit拆分器
splitter = StratifiedShuffleSplit(n_splits=10, test_size=0.2, random_state=42)#做10次拆分，每次拆分比例是8：2
strat_splits = [] #记录这10次拆分后的训练集和测试集
for train_index, test_index in splitter.split(housing, housing["income_cat"]):
    strat_train_set_n = housing.iloc[train_index]
    strat_test_set_n = housing.iloc[test_index]
    strat_splits.append([strat_train_set_n, strat_test_set_n])
strat_train_set, strat_test_set = strat_splits[0]#暂时只使用第一次拆分,此时strat_train_set和strat_test_set为第一次拆分后的训练集和测试集,它们都是DF对象

#或者使用单次拆分器train_test_split(stratify=收入类别)做10次单次拆分也可以
# strat_train_set, strat_test_set = train_test_split(
#     housing, test_size=0.2, stratify=housing["income_cat"], random_state=42)
# print(strat_test_set['income_cat'].value_counts()/len(strat_train_set))#验证测试集和训练集的比列是否为2：8,来说明拆分器是否有效工作

#由于housing['income_cat'] 这一列数据只是用于生成测试集和训练集的，在生成了之后就不会再使用了，因此将其删除
for set_ in (strat_train_set, strat_test_set): #在DF对象元组里面遍历，set_先指向strat_train_set操作，然后set_再指向strat_test_set操作
    set_.drop("income_cat", axis=1, inplace=True) #inplace=True表示直接在原数据集上进行操作
#endregion

housing = strat_train_set.copy()#制作训练集原始副本

#region[可视化地理信息]
# housing.plot(kind="scatter", x="longitude", y="latitude",grid= True,alpha=0.2)
# #设置alpha参数的话，数据点越密集，颜色越深
# #plt.show()
#
# #每个圆圈的半径代表该地区的人口数量（选项S），散点的颜色（选项C）=median_housing_value表示用房价中位数决定点的颜色，数值越高颜色越深
# #lable就是标签
# housing.plot(kind="scatter", x="longitude", y="latitude", grid=True,
#              s=housing["population"] / 100, label="population",
#              c="median_house_value", cmap="jet", colorbar=True,
#              legend=True, sharex=False, figsize=(10, 7))
#plt.show()
#endregion
#region[寻找相关性]
#寻找各特征的相关性。用可视化图表可以预先猜测一下有相关关系的特征
# corr_matrix = housing.corr()
# print(corr_matrix["median_house_value"].sort_values(ascending=False))#降序排列，找出最相关的特征
# #根据图片可以看出来预测房价中位数最有希望的属性似乎是收入中位数，因此可以放大散点图来仔细观察,放大散点图的意思是单独生成一个大一点的散点图来观察
# housing.plot(kind="scatter", x="median_income", y="median_house_value",
#              alpha=0.1, grid=True)
# plt.show()
#endregion
#region[创建新特征来更好的探索与目标属性的相关性]
# housing["rooms_per_house"] = housing["total_rooms"] / housing["households"]
# housing["bedrooms_ratio"] = housing["total_bedrooms"] / housing["total_rooms"]
# housing["people_per_house"] = housing["population"] / housing["households"]
# corr_matrix = housing.corr(numeric_only=True)
# print(corr_matrix["median_house_value"].sort_values(ascending=False))
#endregion[]
#region[正式数据准备]
#恢复干净的训练集为机器学习算法准备数据
housing = strat_train_set.drop("median_house_value", axis=1) #通过删除目标列的方式将数据和目标属性分开
# print(housing.head())
housing_labels = strat_train_set["median_house_value"].copy() #给机器学习算法准备标签
#region[清洗数值型数据]
#由于大多数机器学习算法无法处理缺失值，因此需要对数据进行清理，这个数据集里total_bedrooms列有207个缺失值，因此需要处理
# housing.dropna(subset=["total_bedrooms"], inplace=True)    # 方法一,去掉相应的地区
# housing.drop("total_bedrooms", axis=1)       # 方法二，去掉整个属性
# median = housing["total_bedrooms"].median()  # 方法三，将缺失值设为均值来代替
# housing["total_bedrooms"].fillna(median, inplace=True)
#最好使用sklearn.impute.SimpleImputer类来处理缺失值，好处是它将存储每个特征的中位数
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy="median") #创建了一个中位数策略的缺失值填充器，它会用每列的中位数来填充该列的缺失值
#由于只能根据数值属性来计算中位数，因此需要创建仅包含数值属性的数据副本，（此处就排除ocean_proximity列）
housing_num = housing.select_dtypes(include=[np.number])
imputer.fit(housing_num)#fit()计算housing_num数据集的每一列的中位数，将这些中位数存储在填充器内部供后续使用，
# print(imputer.statistics_)
X = imputer.transform(housing_num) #X是housing_num完成了中位数填充后的数据集的数组形式
#将X恢复成DataFrame结构
housing_tr = pd.DataFrame(X, columns=housing_num.columns,
                          index=housing_num.index)
#endregion[]
#region[清洗文本性数据]
housing_cat = housing[['ocean_proximity']]#这个数据集只有ocean_proximity这一列是文本型数据
# from sklearn.preprocessing import OrdinalEncoder #用有序编码来对文本数据转换
# ordinal_encoder = OrdinalEncoder() #创建一个有序编码器（类实例）
# #利用fit_transform方法将fit()和transform()结合起来使用，过程是识别housing_cat里的所有唯一类别值并为其分配一个整数(fit做的事)，最后根据整数将类值映射为独热编码（transform做的事）
# housing_cat_encoded = ordinal_encoder.fit_transform(housing_cat)
# # print(housing_cat_encoded[:8]) #输出有序编码数组的前8行
# # print(ordinal_encoder.categories_) #输出ocean_proximity列的所有类别，因为只有这一个特征，故输出一个一维数组
#但是此数据集ocean_proximity列的类别是无序的，用独热编码更适合
#进行独热编码
from sklearn.preprocessing import OneHotEncoder
#默认情况下OneHotEncoder会返回稀疏矩阵，可以调用toarray()方法将其转为Numpy数组
cat_encoder = OneHotEncoder(sparse_output= False)#sparse_output=False表示不返回稀疏矩阵
housing_cat_1hot = cat_encoder.fit_transform(housing_cat)
#endregion[]
#region[进行特征缩放]
#为什么要进行特征缩放？此数据集的房间数分布在[6,39320],而收入中位数仅分布在[0,15]。这会导致训练集的房间数特征比收入中位数特征有更高的权重，从而导致收入中位数特征被过度地影响，从而导致模型性能下降

#region[使用归一化方法即最小-最大缩放方法]
from sklearn.preprocessing import MinMaxScaler
min_max_scaler =MinMaxScaler(feature_range=(-1,1))
housing_num_min_max_scaled = min_max_scaler.fit_transform(housing_num)
#endregion[]
#region[使用标准化方法]
from sklearn.preprocessing import StandardScaler
standard_scaler = StandardScaler()
housing_num_std_scaled = standard_scaler.fit_transform(housing_num)
#endregion[]
#region[特征缩放]
#由于population这个特征是重尾分布，因此创建一个对数转换器，使其的分布尽量对称。对称的分布几乎没有太多的异常值，因此对特征进行变换。
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.cluster import KMeans
from sklearn.preprocessing import FunctionTransformer
from sklearn.metrics.pairwise import rbf_kernel

class ClusterSimilarity(BaseEstimator, TransformerMixin):
    def __init__(self, n_clusters=10, gamma=1.0, random_state=None):
        self.n_clusters = n_clusters
        self.gamma = gamma
        self.random_state = random_state

    def fit(self, X, y=None, sample_weight=None):
        self.kmeans_ = KMeans(n_clusters=self.n_clusters, random_state=self.random_state)
        self.kmeans_.fit(X, sample_weight=sample_weight)
        return self

    def transform(self, X):
        return rbf_kernel(X, self.kmeans_.cluster_centers_, gamma=self.gamma)

    def get_feature_names_out(self, input_features=None):
        return [f"Cluster_{i}_similarity" for i in range(self.n_clusters)]


cluster_simil = ClusterSimilarity(n_clusters=10, gamma=1.0, random_state=42)
similarities = cluster_simil.fit_transform(housing[["latitude", "longitude"]], sample_weight=housing_labels) #用样本标签作为样本权重
#endregion[]
#endregion[]
#region[创建一个数据转换流水线]
#这个pipeline工作流程：数据首先进入SimpleImputer，处理缺失值。处理后的数据接着进入StandardScaler，进行标准化。
from sklearn.pipeline import Pipeline, make_pipeline

num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy="median")),("standardize",StandardScaler())
])
#使用make_pipeline创建流水线和使用Pipeline创建流水线大致都是一样，区别在于make_pipeline会自动将输入的转换器名称作为输出的转换器的名称而pipeline可以自定义这些步骤名字
# from sklearn.pipeline import make_pipeline
# num_pipeline = make_pipeline(SimpleImputer(strategy="median"),StandardScaler())

# 导入ColumnTransformer，用于对不同类型的列应用不同的转换
from sklearn.compose import ColumnTransformer, make_column_selector

#分别对数值类型特征和分类型特征建立流水线处理
# 定义数值型特征列名列表
num_attribs = ['longitude','latitude','housing_median_age','total_rooms',
               'total_bedrooms','population','households','median_income']

# 定义分类型特征列名列表
cat_attribs = ['ocean_proximity']

# 创建分类特征处理管道：
# 1. 使用most_frequent策略填充缺失值（用出现最频繁的值填充）
# 2. 使用OneHotEncoder进行独热编码，handle_unknown="ignore"表示忽略训练时未见过的类别
cat_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

# 创建完整的预处理流水线：
# 使用ColumnTransformer将数值型特征和分类型特征分别用对应的管道处理
# "num"表示数值型特征处理管道，使用之前定义的num_pipeline
# "cat"表示分类型特征处理管道，使用上面定义的cat_pipeline
preprocessing = ColumnTransformer([
    ("num", num_pipeline, num_attribs),
    ("cat", cat_pipeline, cat_attribs),
])

housing_prepared = preprocessing.fit_transform(housing)#会返回一个numpy数组，形状为(20640, 16)。
print(preprocessing.get_feature_names_out())
#可以再利用ColumnTransformer的get_feature_names_out方法获取特征名称，将其变回DataFrame数据。

#endregion[]
def column_ratio(x):
    return x[:, [0]] / x[:, [1]]

def ratio_name(function_transformer, feature_names_in):
    # 检查输入特征数量，如果是2个特征则返回比率特征名，否则为每个特征添加前缀
    if len(feature_names_in) == 2:
        return ['ratio']  # 比率特征
    else:
        return [f'log_{name}' for name in feature_names_in]  # 对数特征

def ratio_pipeline():
    return make_pipeline(SimpleImputer(strategy="median"),
                         FunctionTransformer(column_ratio, feature_names_out=ratio_name),
                         StandardScaler())

log_pipeline = make_pipeline(
    SimpleImputer(strategy="median"),
    FunctionTransformer(np.log, feature_names_out=ratio_name),
    StandardScaler()
)
cluster_simil = ClusterSimilarity(n_clusters=10, gamma=1.0, random_state=42)
default_num_pipeline = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())
preprocessing = ColumnTransformer([
    ("bedrooms", ratio_pipeline(), ["total_bedrooms", "total_rooms"]),
    ("rooms_per_household", ratio_pipeline(), ["total_rooms", "households"]),
    ("people_per_household", ratio_pipeline(), ["population", "households"]),
    ("geo", cluster_simil, ["latitude", "longitude"]),
    ("log", log_pipeline, ["total_bedrooms", "total_rooms", "population", "households", "median_income"]),
    ("cat", cat_pipeline, make_column_selector(dtype_include= object)),
 ],
remainder=default_num_pipeline
)
housing_prepared = preprocessing.fit_transform(housing)

#endregion[]
#region[开始找最优参数——利用线性模型]
from sklearn.linear_model import LinearRegression
lin_reg = make_pipeline(preprocessing, LinearRegression())
lin_reg.fit(housing, housing_labels)

housing_predictions = lin_reg.predict(housing)
# 这行代码的作用是获取housing_predictions数组中前5个元素，并将它们四舍五入到百位（即小数点后两位为0）
# round(-2)表示四舍五入到倒数第二位，也就是十位，即以百为单位进行四舍五入
# 例如：如果预测值是123456.78，round(-2)后会变成123500.00
from sklearn.metrics import mean_squared_error
import numpy as np
lin_rmse = np.sqrt(mean_squared_error(housing_labels, housing_predictions))
print(lin_rmse)