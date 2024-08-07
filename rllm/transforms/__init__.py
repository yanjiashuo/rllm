from .base_transform import BaseTransform
from .compose import Compose
from .normalize_features import NormalizeFeatures
from .svd_feature_reduction import SVDFeatureReduction
from .remove_training_classes import RemoveTrainingClasses

from .add_remaining_self_loops import AddRemainingSelfLoops
from .remove_self_loops import RemoveSelfLoops
from .knn_graph import KNNGraph
from .gcn_norm import GCNNorm
from .build_homo_graph import build_homo_graph

general_transforms = [
    'BaseTransform',
    'Compose',
    'NormalizeFeatures',
    'SVDFeatureReduction',
    'RemoveTrainingClasses',
]

graph_transforms = [
    'AddRemainingSelfLoops',
    'RemoveSelfLoops',
    'KNNGraph',
    'GCNNorm',
]

graph_builders = [
    'build_homo_graph',
]


__all__ = general_transforms + graph_transforms + graph_builders

