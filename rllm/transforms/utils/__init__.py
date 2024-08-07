from .normalize_features import normalize_features
from .svd_feature_reduction import svd_feature_reduction
from .remove_training_classes import remove_training_classes

from .add_remaining_self_loops import add_remaining_self_loops
from .remove_self_loops import remove_self_loops
from .knn_graph import knn_graph
from .gcn_norm import gcn_norm

general_func = [
    'normalize_features',
    'svd_feature_reduction',
    'remove_training_classes',
]


graph_func = [
    'add_remaining_self_loops',
    'remove_self_loops',
    'knn_graph',
    'gcn_norm'
]

__all__ = general_func + graph_func

